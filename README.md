# Building-a-Database-of-a-Million-Indian-Recipes-Extraction-from-YouTube-Videos

# Building a Scalable Pipeline for Extracting Indian Recipes from YouTube Videos

This repository documents the pipeline developed during the **NPTEL Winter Internship (Oct 2025 – Jan 2026)** for extracting, transcribing, and structuring Indian cooking recipes from YouTube videos, with a focus on regional and rural cuisines.

The pipeline converts unstructured multimedia content into structured, machine-readable recipe representations (JSON format). Due to the multilingual and noisy nature of the data, the system combines existing tools with manual and semi-automatic processing.

---

## 👥 Team
- **Nikhil Raj** – B.Tech CSE, NSIT Patna  
- **Sai Deepika**

**Guidance:**  
Prof. Partha Pratim Das  
Ashoka University, Sonipat, Haryana

---

## 📌 Overview of the Pipeline

The pipeline consists of the following stages:

1. **YouTube Channel & Video Selection**
2. **Metadata Extraction**
3. **Speech-to-Text Transcription**
4. **(Optional) Translation**
5. **Recipe Structuring into JSON**
6. **Manual Validation & Cleanup**

A detailed description of each stage is provided below.

---

## 🛠 Tools and Resources Used

### 1. Metadata Extraction
- **Tool:** `mwmetadata`
- **Purpose:**  
  Used to extract YouTube video metadata such as:
  - Video title
  - Channel name
  - Upload date
  - Duration
  - Description
  - Video URL

The metadata was exported in CSV format for further processing.

---

### 2. Transcription
- **Tool:** **TurboScribe**
- **Purpose:**  
  Used for speech-to-text transcription of YouTube videos, especially for:
  - Regional Indian languages
  - Code-mixed speech
  - Non-standard accents and rural audio

Each video transcript was saved as a **separate JSON file**.

> Note: Transcription was performed using an external tool due to better multilingual performance compared to open-source ASR models.

---

### 3. Recipe Structuring
- **Method:** Manual and semi-automatic post-processing
- **Output:** Structured JSON files

From the transcripts, the following recipe components were extracted and organized:
- Recipe name
- Ingredients list
- Preparation steps
- Cooking time (when available)
- Additional notes (tips, variations)

Each YouTube video corresponds to **one structured recipe JSON file**.

---

## 📂 Repository Structure

```text
youtube-recipe-pipeline/
│
├── README.md
│
├── metadata/
│   ├── sample_metadata.csv
│   └── metadata_description.md
│
├── transcripts/
│   ├── sample_video_01_transcript.json
│   └── sample_video_02_transcript.json
│
├── structured_recipes/
│   ├── recipe_video_01.json
│   └── recipe_video_02.json
│
├── tools_used.md
│
└── pipeline_description.md
