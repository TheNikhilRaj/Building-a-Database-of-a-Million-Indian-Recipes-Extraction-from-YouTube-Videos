# Building a Database of a Million Indian Recipes

## Extraction from YouTube Videos

[![NPTEL Winter Internship](https://img.shields.io/badge/NPTEL-Winter%20Internship%202025-blue)](https://nptel.ac.in/)
[![Ashoka University](https://img.shields.io/badge/Mentor-Ashoka%20University-green)](https://www.ashoka.edu.in/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://python.org/)
[![License](https://img.shields.io/badge/License-Academic-orange)]()

---

## 📋 Project Overview

A scalable pipeline for extracting, translating, and structuring cooking recipes from YouTube videos featuring Indian regional cuisines. This project converts unstructured multilingual video content into machine-readable structured data (JSON format) suitable for database construction.

**Project Duration:** October 2025 - January 2026  
**Team:** Nikhil Raj & Erla Sai Deepika  
**Mentors:** Prof. Lipika Dey & Prof. Partha Pratim Das, Ashoka University  
**Program:** NPTEL Winter Internship 2025

---

## 📁 Repository Structure

```
├── Indian Rajasthani Village Food Cooking Recipe/
│   └── [Recipe JSON files]
│
├── Rural Recipes/
│   └── [Recipe JSON files]
│
├── Thasneen (South Indian) Recipes/
│   └── [Recipe JSON files]
│
├── Vismai Food (SIMPLY SOUTH) Recipes/
│   └── [Recipe JSON files]
│
├── tools/
│   └── recipe_visualizer.html          # Custom visualization tool
│
├── Indian Rajasthani Village Food Cooking Recipe-Metadata-Excel-File.xlsx
├── Rural Recipes-Metadata-Excel-File.xlsx
├── Thasneen (South Indian) Recipes-Metadata-Excel-File.xlsx
├── Vismai Food (SIMPLY SOUTH) Recipes-Metadata-Excel-File.xlsx
│
└── README.md
```

---

## 📊 Dataset Summary

| Channel Name                   | Language         | Total Videos | JSON Files | Status       |
| ------------------------------ | ---------------- | ------------ | ---------- | ------------ |
| Rural Recipes (Banglanatak)    | Bengali/Hindi    | 75           | 75         | ✅ Completed |
| Indian Rajasthani Village Food | Rajasthani/Hindi | 16           | 16         | ✅ Completed |
| Thasneen (South Indian)        | Malayalam/Tamil  | 42           | 42         | ✅ Completed |
| Vismai Food (SIMPLY SOUTH)     | Telugu           | 270          | 270        | ✅ Completed |

**Total Recipes Extracted: 403**

---

## 🔧 Tools & Technologies Used

| Tool                  | Purpose                                        | Link                                                            |
| --------------------- | ---------------------------------------------- | --------------------------------------------------------------- |
| **TurboScribe**       | YouTube transcript extraction (Speech-to-Text) | [turboscribe.ai](https://turboscribe.ai/)                       |
| **Google Gemini AI**  | Translation & metadata extraction              | [gemini.google.com](https://gemini.google.com/)                 |
| **MW Metadata Tool**  | Video metadata extraction                      | [mattw.io/youtube-metadata](https://mattw.io/youtube-metadata/) |
| **Recipe Visualizer** | Quality inspection & JSON formatting           | [Included in repo](tools/recipe_visualizer.html)                |

---

## 🛠️ Custom Tools

### Recipe Metadata Visualizer

A web-based tool for creating, viewing, and editing recipe JSON files.

**Location:** [`tools/recipe_visualizer.html`](tools/recipe_visualizer.html)

**Features:**

- 📥 **Input Tab** - Enter video metadata, ingredients, and transcripts
- 👁️ **Preview Tab** - See formatted preview of your data
- 📄 **JSON Tab** - View syntax-highlighted JSON output with copy/download
- 📂 **Load Tab** - Load existing JSON files via drag & drop
- 📊 **Stats Bar** - Real-time word counts, ingredient count, completion percentage
- 💾 **Download** - Export JSON files with proper naming
- 📋 **Copy** - One-click copy to clipboard
- 🔄 **Offline** - Works without internet connection

**How to Use:**

1. Download `tools/recipe_visualizer.html` from this repository
2. Open the file in any web browser (Chrome, Firefox, Edge)
3. Fill in the metadata fields (Video ID, Title, Channel, Language, etc.)
4. Add ingredients one by one or paste in bulk
5. Paste original transcript and English translation
6. Click "Generate JSON" to create structured output
7. Download or copy the JSON file

**Screenshot:**

![Recipe Visualizer Tool](/docs/screenshots/visualizer_screenshot.png)

---

## 📝 JSON Output Format

Each recipe is stored as a structured JSON file with the following schema:

```json
{
  "video_id": "lbhoAJVkWQk",
  "title": "Traditional Bengali Fish Curry",
  "channel": "Rural Recipes BNC",
  "url": "https://www.youtube.com/watch?v=lbhoAJVkWQk",
  "language": "Bengali",
  "duration": "12:45",
  "publish_date": "2024-03-15",
  "view_count": 125000,
  "like_count": 5200,
  "ingredients": [
    "Rohu fish - 500g",
    "Mustard oil - 4 tbsp",
    "Turmeric powder - 1 tsp",
    "Green chilies - 4",
    "Mustard paste - 2 tbsp"
  ],
  "transcript_original": "আজ আমরা রান্না করব একটা traditional মাছের ঝোল...",
  "transcript_english": "Today we will cook a traditional fish curry...",
  "metadata": {
    "extraction_date": "2026-01-15",
    "pipeline_version": "1.0",
    "extracted_by": "NPTEL Internship Team"
  }
}
```

---

## 🚀 How to Use This Dataset

### Option 1: Browse JSON Files

1. Navigate to any channel folder (e.g., `Rural Recipes/`)
2. Open any `.json` file to view the structured recipe data
3. Each JSON contains original transcript + English translation

### Option 2: Use Excel Metadata Files

1. Open any `*-Metadata-Excel-File.xlsx`
2. View consolidated metadata for all videos in that channel
3. Contains: Video ID, Title, Duration, Language, Status

### Option 3: Programmatic Access (Python)

```python
import json
import os

# Load all recipes from a channel
channel_folder = "Rural Recipes"
recipes = []

for filename in os.listdir(channel_folder):
    if filename.endswith('.json'):
        with open(os.path.join(channel_folder, filename), 'r', encoding='utf-8') as f:
            recipe = json.load(f)
            recipes.append(recipe)

print(f"Loaded {len(recipes)} recipes")

# Example: Print all recipe titles
for recipe in recipes:
    print(recipe.get('title', 'No title'))

# Example: Find all recipes with a specific ingredient
def find_recipes_with_ingredient(recipes, ingredient):
    return [r for r in recipes if any(ingredient.lower() in ing.lower() for ing in r.get('ingredients', []))]

fish_recipes = find_recipes_with_ingredient(recipes, 'fish')
print(f"Found {len(fish_recipes)} fish recipes")
```

### Option 4: Use the Visualizer Tool

1. Open `tools/recipe_visualizer.html` in your browser
2. Go to "Load JSON" tab
3. Drag and drop any JSON file from the dataset
4. View formatted data with syntax highlighting

---

## 📋 Pipeline Workflow

The extraction pipeline follows these steps:

```
┌─────────────────┐
│ YouTube Channel │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Video Discovery │  ← List all videos in channel/playlist
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Metadata     │  ← Extract title, duration, description
│   Extraction    │     using Gemini AI / MW Tool
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Transcript    │  ← Speech-to-text using TurboScribe
│   Extraction    │     (AI-powered transcription)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Translation   │  ← Regional language → English
│     Module      │     using Gemini AI
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      JSON       │  ← Combine all data into
│   Structuring   │     standardized format using Visualizer
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Quality Check  │  ← Manual verification using Visualizer
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Final Output   │  ← Structured JSON files
└─────────────────┘
```

---

## 🔄 Reproducing the Pipeline

### Step 1: Extract Transcript using TurboScribe

1. Go to [TurboScribe](https://turboscribe.ai/)
2. Sign in / Create account (free tier available)
3. Click "New Transcription"
4. Paste YouTube video URL or upload audio/video file
5. Select source language (Hindi, Bengali, Telugu, etc.)
6. Click "Transcribe"
7. Wait for processing (usually 1-5 minutes)
8. Download transcript in TXT or JSON format

**TurboScribe Features:**

- Supports 98+ languages including Indian regional languages
- High accuracy for Hindi, Bengali, Telugu, Tamil, Malayalam
- Handles background noise and multiple speakers
- Free tier: 3 free transcriptions

---

### Step 2: Extract Metadata (Using Gemini AI)

Go to [Gemini AI](https://gemini.google.com/) and use this prompt:

```
Extract metadata from this YouTube cooking video in JSON format:

Video URL: [PASTE_VIDEO_URL]

Please extract:
- video_id
- title
- channel_name
- duration
- detected_language
- ingredients (if mentioned in description)
- brief description

Output as valid JSON.
```

---

### Step 3: Translate Transcript (Using Gemini AI)

Use this prompt in Gemini AI:

```
Translate the following cooking recipe transcript from [LANGUAGE] to English.

Guidelines:
1. Preserve ingredient names that don't have English equivalents - transliterate them
2. Keep traditional measurements as-is (e.g., "one fistful", "andaaz se")
3. Maintain the conversational tone
4. Add [transliteration] for cultural/regional terms

Transcript:
[PASTE_TRANSCRIPT_FROM_TURBOSCRIBE]
```

---

### Step 4: Create Structured JSON using Visualizer

1. Open `tools/recipe_visualizer.html` in your browser
2. Fill in the **Input Data** tab:
   - Video ID, Title, Channel Name, Language
   - Duration, Publish Date, View/Like counts
   - Add ingredients (one by one or bulk paste)
   - Paste original transcript
   - Paste English translation
3. Click **"Generate JSON"**
4. Review in the **JSON Output** tab
5. Click **"Download"** to save the file

---

## 🛠️ Tools Documentation

### Tool 1: TurboScribe (Primary Transcription Tool)

**Website:** https://turboscribe.ai/

**Why TurboScribe?**

- Better accuracy for Indian regional languages compared to YouTube auto-captions
- Supports direct YouTube URL input
- Clean transcript output without timestamps clutter
- Handles poor audio quality better

**Supported Languages (Used in Project):**

| Language   | Accuracy    | Notes                    |
| ---------- | ----------- | ------------------------ |
| Hindi      | High        | Handles code-mixing well |
| Bengali    | High        | Good for rural accents   |
| Telugu     | High        | Clear transcription      |
| Tamil      | High        | Accurate                 |
| Malayalam  | Medium-High | Some dialect variations  |
| Rajasthani | Medium      | Treats as Hindi dialect  |

**Usage Limits (Free Tier):**

- 3 free transcriptions
- Up to 30 minutes per file
- Standard processing speed

---

### Tool 2: Google Gemini AI (Translation & Metadata)

**Website:** https://gemini.google.com/

**Used For:**

1. Translating regional language transcripts to English
2. Extracting structured metadata from video descriptions
3. Identifying ingredients from transcripts
4. Quality checking translations

**Best Practices:**

- Use detailed prompts with guidelines
- Specify source language explicitly
- Ask to preserve transliterated terms
- Request JSON output format for metadata

---

### Tool 3: Recipe Metadata Visualizer (Custom Built)

**Location:** `tools/recipe_visualizer.html`

**Purpose:** Quality inspection, JSON creation, and data formatting

**Key Features:**

| Feature        | Description                                  |
| -------------- | -------------------------------------------- |
| 📥 Input Data  | Enter all metadata, ingredients, transcripts |
| 👁️ Preview     | Formatted view of recipe data                |
| 📄 JSON Output | Syntax-highlighted JSON with copy/download   |
| 📂 Load JSON   | Import existing files via drag & drop        |
| 📊 Stats       | Real-time word count and completion tracking |
| 🎨 Modern UI   | Beautiful gradient design, fully responsive  |
| 🔄 Offline     | Works without internet after loading         |

---

## 📈 Evaluation Methodology

### Back-Translation Evaluation

As suggested by Prof. Lipika Dey:

```
Original Text (A)
      ↓ [Translate]
English Text (B)
      ↓ [Back-Translate]
Back-Translated Text (A')
      ↓
Compare A and A' using:
- BLEU Score
- ROUGE Score
- BERTScore
```

### Hallucination Detection

For ingredient list `L` from video description:

| Metric            | Formula                          | Meaning             |
| ----------------- | -------------------------------- | ------------------- |
| **Hit**           | Items in L ∩ Transcript          | Correctly extracted |
| **Miss**          | Items in L but not in Transcript | Missed ingredients  |
| **Hallucination** | Items in Transcript but not in L | False additions     |

---

## 📂 Additional Resources

| Resource                    | Link                                                                                   |
| --------------------------- | -------------------------------------------------------------------------------------- |
| Full Dataset (Google Drive) | [Click Here](https://drive.google.com/drive/folders/1kyAQaV5eYWCy8YCyMgc9ebVtzTRi_ifo) |
| Recipe Visualizer Tool      | [tools/recipe_visualizer.html](tools/recipe_visualizer.html)                           |
| TurboScribe                 | [turboscribe.ai](https://turboscribe.ai/)                                              |
| Google Gemini AI            | [gemini.google.com](https://gemini.google.com/)                                        |
| MW Metadata Tool            | [mattw.io/youtube-metadata](https://mattw.io/youtube-metadata/)                        |
| Project Report              | Attached in submission email                                                           |

---

## 🔮 Future Scope

- [ ] Automated pipeline with reduced manual intervention
- [ ] Fine-tuned ASR models for Indian regional languages
- [ ] Multimodal integration (visual ingredient extraction from video frames)
- [ ] Recipe Knowledge Graph construction using Neo4j
- [ ] Mobile application for browsing recipes
- [ ] Integration with nutrition databases
- [ ] Web-based dashboard for dataset exploration

---

## 👥 Team

| Name            | Role                                                        | Contact                   |
| --------------- | ----------------------------------------------------------- | ------------------------- |
| **Nikhil Raj**  | Pipeline Development, Metadata Extraction, Tool Development | nikhilrjraj7890@gmail.com |
| **Erla Sai Deepika** | Transcript Processing, Translation, Quality Assurance       | saideepika1326@gmail.com  |

---

## 🙏 Acknowledgments

- **Prof. Lipika Dey** - Professor of Computer Science, Ashoka University (Fellow INAE and AAIA)
- **Prof. Partha Pratim Das** - Ashoka University
- **NPTEL, IIT Madras** - For the internship opportunity

---

## 📄 License

This project was developed as part of **NPTEL Winter Internship 2025** under the guidance of Ashoka University.

---

## 📚 References

1. Vaswani, A., et al. (2017). "Attention is All You Need." _NeurIPS_
2. Radford, A., et al. (2022). "Whisper: Robust Speech Recognition." _OpenAI_
3. TurboScribe - AI Transcription Tool - https://turboscribe.ai/
4. Google Gemini AI - https://gemini.google.com/
5. YouTube Metadata Tool - https://mattw.io/youtube-metadata/
6. Machine Translation Evaluation Guide - https://www.machinetranslation.com/
7. Rural Recipes by Banglanatak - https://www.youtube.com/@RuralRecipes_BNC

---

<p align="center">
  <b>⭐ If you find this dataset useful, please consider starring this repository! ⭐</b>
</p>
