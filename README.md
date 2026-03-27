---
title: TruthLens AI
emoji: 🕵️
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

# TruthLens AI - Fake News Detector
### 🚀 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/suneeth13/FakeNews)

TruthLens AI is a modern, full-stack application that leverages **Google Gemini Pro** to verify news headlines and articles. It provides real-time "Real/Fake" classification along with a detailed factual justification.

## ✨ Features
- **AI-Powered Verification**: Uses Gemini 1.5/2.0 for high-accuracy news analysis.
- **Detailed Reasoning**: Explains *why* a piece of news is flagged, citing factual context.
- **Modern UI**: A premium, glassmorphism-inspired interface built with Vanilla CSS and JavaScript.
- **FastAPI Backend**: High-performance Python backend for seamless model interaction.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, Uvicorn
- **AI**: Google Gemini Pro (Generative AI SDK)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Environment**: Python Dotenv

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google AI Studio API Key (Get it [here](https://aistudio.google.com/))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Suneeth13/Fake-News-Detector.git
   cd Fake-News-Detector
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

### Running the App
Start the FastAPI server:
```bash
python -m uvicorn backend.main:app --reload
```
Open your browser and navigate to `http://127.0.0.1:8000`.

## 📂 Project Structure
- `backend/main.py`: Main FastAPI application.
- `frontend/`: UI assets (HTML, CSS, JS).
- `ml/predict_gemini.py`: Logic for Gemini AI interaction.
- `.env.example`: Template for environment variables.
- `Dockerfile`: Containerization configuration.

## 🌐 Deployment

### Option 1: Hugging Face Spaces (Recommended for AI)
1. Create a new **Space** on [Hugging Face](https://huggingface.co/new-space).
2. Choose **Docker** as the SDK.
3. Connect your GitHub repository (`Suneeth13/Fake-News-Detector`).
4. Go to **Settings** > **Variables and Secrets** and add `GEMINI_API_KEY` as a **Secret**.
5. The app will automatically build and deploy!

### Option 2: Render
1. Create a new **Web Service** on [Render](https://dashboard.render.com/).
2. Connect your GitHub repository.
3. Choose **Docker** as the Environment.
4. Add `GEMINI_API_KEY` in the **Environment Variables** section.
5. Deploy!

## 📜 License
This project is for educational purposes and shows strong NLP understanding and AI integration.
