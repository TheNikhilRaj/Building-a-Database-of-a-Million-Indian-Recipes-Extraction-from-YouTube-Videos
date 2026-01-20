# Building a Database of a Million Indian Recipes
## Extraction from YouTube Videos

[![NPTEL Winter Internship](https://img.shields.io/badge/NPTEL-Winter%20Internship%202025-blue)](https://nptel.ac.in/)
[![Ashoka University](https://img.shields.io/badge/Mentor-Ashoka%20University-green)](https://www.ashoka.edu. in/)

---

## 📋 Project Overview

A scalable pipeline for extracting, translating, and structuring cooking recipes from YouTube videos featuring Indian regional cuisines.  This project converts unstructured multilingual video content into machine-readable structured data (JSON format) suitable for database construction.

**Project Duration:** October 2025 - January 2026  
**Team:** Nikhil Raj & Sai Deepika  
**Mentors:** Prof.  Lipika Dey & Prof.  Partha Pratim Das, Ashoka University  
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
├── Indian Rajasthani Village Food Cooking Recipe-Metadata-Excel-File.xlsx
├── Rural Recipes-Metadata-Excel-File.xlsx
├── Thasneen (South Indian) Recipes-Metadata-Excel-File.xlsx
├── Vismai Food (SIMPLY SOUTH) Recipes-Metadata-Excel-File.xlsx
│
└── README.md
```

---

## 📊 Dataset Summary

| Channel Name | Language | Total Videos | JSON Files | Status |
|--------------|----------|--------------|------------|--------|
| Rural Recipes (Banglanatak) | Bengali/Hindi | -- | -- | ✅ Completed |
| Indian Rajasthani Village Food | Rajasthani/Hindi | -- | -- | ✅ Completed |
| Thasneen (South Indian) | Malayalam/Tamil | -- | -- | ✅ Completed |
| Vismai Food (SIMPLY SOUTH) | Telugu | -- | -- | ✅ Completed |

> **Note:** Please update the actual counts from your data. 

---

## 🔧 Tools & Technologies Used

| Tool | Purpose | Link |
|------|---------|------|
| **Tactiq** | YouTube transcript extraction | [tactiq.io](https://tactiq.io/) |
| **Google Gemini AI** | Translation & metadata extraction | [gemini.google.com](https://gemini.google.com/) |
| **MW Metadata Tool** | Video metadata extraction | Browser-based |

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
  "publish_date":  "2024-03-15",
  "view_count": 125000,
  "like_count": 5200,
  "ingredients": [
    "Rohu fish - 500g",
    "Mustard oil - 4 tbsp",
    "Turmeric powder - 1 tsp",
    "Green chilies - 4",
    "Mustard paste - 2 tbsp"
  ],
  "transcript_original": "আজ আমরা রান্না করব একটা traditional মাছের ঝোল.. .",
  "transcript_english":  "Today we will cook a traditional fish curry...",
  "metadata":  {
    "extraction_date":  "2026-01-15",
    "pipeline_version": "1.0"
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

### Option 3: Programmatic Access

```python
import json
import os

# Load all recipes from a channel
channel_folder = "Rural Recipes"
recipes = []

for filename in os.listdir(channel_folder):
    if filename.endswith('.json'):
        with open(os.path. join(channel_folder, filename), 'r', encoding='utf-8') as f:
            recipe = json.load(f)
            recipes.append(recipe)

print(f"Loaded {len(recipes)} recipes")

# Example: Print all recipe titles
for recipe in recipes: 
    print(recipe. get('title', 'No title'))
```

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
│ Video Discovery │  ← List all videos in channel
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
│   Transcript    │  ← Speech-to-text using Tactiq
│   Extraction    │     (leverages YouTube auto-captions)
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
│   Structuring   │     standardized format
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Quality Check  │  ← Manual verification
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Final Output   │  ← Structured JSON files
└─────────────────┘
```

---

## 🔄 Reproducing the Pipeline

### Step 1: Install Tactiq Extension

1. Go to [Chrome Web Store](https://chrome.google.com/webstore)
2. Search for "Tactiq"
3. Click "Add to Chrome"

### Step 2: Extract Transcript

1. Open a YouTube recipe video
2. Click Tactiq icon in browser toolbar
3. Wait for transcript to load
4. Click "Export" → Select TXT or JSON format

### Step 3: Extract Metadata (Using Gemini AI)

Use this prompt in [Gemini AI](https://gemini.google.com/):

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

### Step 4: Translate Transcript (Using Gemini AI)

Use this prompt:

```
Translate the following cooking recipe transcript from [LANGUAGE] to English. 

Guidelines:
1. Preserve ingredient names that don't have English equivalents - transliterate them
2. Keep traditional measurements as-is (e.g., "one fistful")
3. Maintain the conversational tone
4. Add [transliteration] for cultural terms

Transcript: 
[PASTE_TRANSCRIPT]
```

### Step 5: Create Structured JSON

Combine metadata, original transcript, and translation into the JSON schema shown above.

---

## 📈 Evaluation Methodology

### Back-Translation Evaluation

```
Original (A) → English (B) → Back-translate (A')
                    ↓
            Compare A and A'
            using BLEU, ROUGE, BERTScore
```

### Hallucination Detection

For ingredient list `L` from video description: 
- **Hit:** Ingredients in `L` that appear in transcript
- **Miss:** Ingredients in `L` not found in transcript
- **Hallucination:** Items in transcript not in `L`

---

## 📂 Additional Resources

- **Full Dataset (Google Drive):** [Click Here](https://drive.google.com/drive/folders/1kyAQaV5eYWCy8YCyMgc9ebVtzTRi_ifo)
- **Project Report:** [Attached in submission email]

---

## 🔮 Future Scope

- [ ] Automated pipeline with reduced manual intervention
- [ ] Fine-tuned ASR models for Indian languages
- [ ] Multimodal integration (visual ingredient extraction)
- [ ] Recipe Knowledge Graph construction
- [ ] Mobile application for browsing recipes

---

## 👥 Team

| Name | Role | Contact |
|------|------|---------|
| **Nikhil Raj** | Pipeline Development, Metadata Extraction | nikhilrjraj7890@gmail.com |
| **Sai Deepika** | Transcript Processing, Translation | saideepika1326@gmail.com |

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

1. Vaswani, A., et al. (2017). "Attention is All You Need." *NeurIPS*
2. Radford, A., et al. (2022). "Whisper:  Robust Speech Recognition." *OpenAI*
3. Tactiq YouTube Transcript Tool - https://tactiq.io/
4. Google Gemini AI - https://gemini.google.com/
