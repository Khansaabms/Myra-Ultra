# MYRA ULTRA v8.0 — AI Voice Assistant + MYRA Coder

```
  ⬡ MYRA ULTRA  |  AI Voice Assistant  +  MYRA Coder AI Website Builder
  Voice se bolo → MYRA sunti hai → Website ban jaati hai → Live deploy!
```

## Quick Start

### Step 1: Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: MYRA Coder Setup
```bash
# Install Node.js 18+ first: https://nodejs.org
python setup_myra_coder.py
```

### Step 3: Run MYRA
```bash
python aria.py
```

### Step 4: Website banao!
MYRA se bolo:
- "gaming website banao dark theme ke saath"
- "portfolio website bana mere liye"
- "restaurant ka website create karo"

**MYRA Coder panel automatically khulega!**

---

## Architecture

```
MYRA ULTRA v8.0
├── aria.py                      # Main MYRA window (PyQt5)
├── myra_coder_integration.py    # MYRA Coder Python bridge
├── myra_coder/                  # Node.js AI coding engine (renamed HunterCode)
│   ├── src/agent.ts             # Core AI agent
│   ├── src/run.ts               # Headless runner
│   ├── src/providers/gemini.ts  # Gemini provider
│   └── dist/                    # Compiled JS (after build)
├── website_builder/             # WebForge (existing python builder)
├── Projects/                    # Generated websites save hote hain
└── setup_myra_coder.py          # One-click setup
```

## How It Works

```
User Voice Command
      ↓
MYRA Voice Recognition (Gemini WebSocket)
      ↓
_is_website_command() check
      ↓
MyraCoderOverlay.show_panel(task)  ← MYRA UI pe panel aata hai
      ↓
node dist/run.js --progress-file tmp.jsonl
      ↓
AI agent → tools → files create hote hain
      ↓ (live streaming via JSON progress file)
Qt signals → live UI update
      ↓
Done → MYRA bolti hai congratulations!
```

## Configuration

`.env` file:
```
GEMINI_API_KEY=your_key
GITHUB_TOKEN=ghp_...    (for WebForge deploy)
VERCEL_TOKEN=vcp_...    (for WebForge deploy)
```

## EXE Build

```bash
python setup_myra_coder.py  # build Node.js first
pyinstaller MYRA_ULTRA.spec
```

Note: Target PC pe Node.js 18+ install hona chahiye EXE ke liye.

## Troubleshooting

- **"MYRA Coder build nahi mili"**: `cd myra_coder && npm install && npm run build`
- **"Node.js nahi mila"**: https://nodejs.org install karo
- **"API key error"**: `.env` mein `GEMINI_API_KEY` add karo

---
MYRA ULTRA v8.0 | MYRA Coder powered by HunterCode engine (MIT License)
