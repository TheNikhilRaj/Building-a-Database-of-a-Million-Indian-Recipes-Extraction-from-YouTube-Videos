import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# -----------------------------
# 1) Files
# -----------------------------
files = [
    "Indian Rajasthani Village Food Cooking Recipe-Metadata-Excel-File.xlsx",
    "Rural Recipes-Metadata-Excel-File.xlsx",
    "Thasneen (South Indian) Recipes-Metadata-Excel-File.xlsx",
    "Vismai Food (SIMPLY SOUTH) Recipes-Metadata-Excel-File.xlsx"
]

# -----------------------------
# 2) Synonyms
# -----------------------------
synonyms = {
    'namak': 'salt', 'lobon': 'salt', 'mith': 'salt', 'salt (to taste)': 'salt',
    'black salt': 'salt', 'pani': 'water', 'water (paani)': 'water', 'water.': 'water',
    'gehu ka atta': 'wheat flour', 'wheat flour (gehu ka atta)': 'wheat flour',
    'maida': 'all-purpose flour', 'all purpose flour': 'all-purpose flour',
    'haldi': 'turmeric powder', 'turmeric': 'turmeric powder',
    'lal mirch': 'red chili powder', 'red chilli powder': 'red chili powder',
    'mirchi': 'red chili powder',
    'jeera': 'cumin seeds', 'cumin': 'cumin seeds',
    'hing': 'asafoetida', 'saunf': 'fennel seeds'
}

# -----------------------------
# 3) Clean Function
# -----------------------------
def clean_ingredients(text):
    if pd.isna(text):
        return []
    text = str(text).lower().replace(";", ",")
    items = [i.strip() for i in text.split(",") if i.strip()]
    normalized = []
    for ing in items:
        ing = re.sub(r'\(.*?\)', '', ing).strip()
        ing = synonyms.get(ing, ing)
        if ing:
            normalized.append(ing)
    return normalized

# -----------------------------
# 4) Read and Combine
# -----------------------------
all_data = []
for f in files:
    df = pd.read_excel(f)
    df['File'] = f.split(".")[0]
    df['Ingredients_English'] = df['Ingredients Detected'].apply(clean_ingredients)
    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

# -----------------------------
# Q1: Top 20 Ingredients (Overall)
# -----------------------------
all_ing = [ing for lst in final_df['Ingredients_English'] for ing in lst]
global_counts = Counter(all_ing)

top20 = pd.DataFrame(global_counts.most_common(20), columns=['Ingredient', 'Frequency'])
print("\n========== TOP 20 INGREDIENTS (OVERALL) ==========")
print(top20.to_string(index=False))

# -----------------------------
# Q2: Unique Ingredients per File
# -----------------------------
file_docs = final_df.groupby('File')['Ingredients_English'].apply(lambda x: [i for sub in x for i in sub]).reset_index()

unique_results = {}
for i, row in file_docs.iterrows():
    file_name = row['File']
    counts = Counter(row['Ingredients_English'])

    other_ing = []
    for j, row2 in file_docs.iterrows():
        if row2['File'] != file_name:
            other_ing += row2['Ingredients_English']

    unique_counts = {k: v for k, v in counts.items() if k not in other_ing}
    unique_results[file_name] = pd.DataFrame(Counter(unique_counts).most_common(10),
                                            columns=['Ingredient', 'Frequency'])

# Print unique results
print("\n========== UNIQUE INGREDIENTS PER FILE ==========")
for file_name, df_unique in unique_results.items():
    print(f"\n--- {file_name} ---")
    print(df_unique.to_string(index=False))

# -----------------------------
# Q3: Word Clouds (Overall + Per File)
# -----------------------------

# 1) Overall Word Cloud
wc_overall = WordCloud(width=1200, height=600).generate_from_frequencies(global_counts)
wc_overall.to_file("overall_wordcloud.png")

plt.figure(figsize=(12, 6))
plt.imshow(wc_overall, interpolation='bilinear')
plt.axis('off')
plt.title("Overall Word Cloud (All Files Combined)")
plt.show()

# 2) Word Clouds for each file
for i, row in file_docs.iterrows():
    file_name = row['File']
    counts = Counter(row['Ingredients_English'])

    wc = WordCloud(width=1200, height=600).generate_from_frequencies(counts)
    wc.to_file(f"{file_name}_wordcloud.png")

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud - {file_name}")
    plt.show()

# -----------------------------
# Save Excel
# -----------------------------
final_df.to_excel("Combined_English_Ingredients.xlsx", index=False)
print("\nSaved: Combined_English_Ingredients.xlsx")
