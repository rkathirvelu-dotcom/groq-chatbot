# Groq Chatbot

A simple Python chatbot that uses the Groq API to answer questions in an interactive loop.

## Setup

### 1. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API key
- Get a free API key at https://console.groq.com/keys
- Copy `.env.example` to `.env` and add your key:
```bash
cp .env.example .env
```

## Running

```bash
python main.py
```

Type `quit` to exit the chatbot.

## Model
This uses `llama-3.3-70b-versatile` by default. You can change the model in `main.py` to any supported Groq model:
- `llama-3.3-70b-versatile` (latest, default)
- `llama-3.1-8b-instant` (faster, lightweight)
- `mixtral-8x7b-32768` (large context)
