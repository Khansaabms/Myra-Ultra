# MYRA for Termux & Linux

> **Phone UI:** run `myra-termux` on Termux — it opens a full voice + chat UI in your phone browser (MYRA's photo, Gemini Live voice that keeps listening, tool cards, permission prompts, 148+ languages).

MYRA AI assistant for your Android phone ([Termux](https://termux.dev)) and Linux computers. Powered by Google Gemini.
Chat or talk in **148+ languages**, and let MYRA control your device.

- **Termux (Android):** torch, battery, SMS, calls, apps, volume, brightness, clipboard, location, URLs, voice in/out.
- **Linux:** battery, notifications, open apps/URLs, volume (`pactl`), brightness (`brightnessctl`), clipboard (`xclip`/`wl-clipboard`), spoken replies (`espeak-ng`).

## Install

```
pkg update && pkg install python termux-api
pip install myra-termux
myra-termux --setup
myra-termux
```

Also install the **Termux:API** app (F-Droid) for phone control and voice.

Get a free Gemini API key at https://aistudio.google.com/apikey

## Linux (text/CLI version)

For the full MYRA desktop app with the same UI as Windows on Linux, install **`myra-linux`** instead (`pipx install myra-linux`).
The text-only CLI below works on any Linux, including servers/SSH.

```
sudo apt install python3-pip xclip libnotify-bin espeak-ng   # optional helpers
pip install myra-termux        # (use `pipx install myra-termux` on newer distros)
myra-termux --setup
myra-termux
```

The backend (Termux or Linux) is detected automatically (override with `MYRA_BACKEND=linux|termux`).

## Live voice

Tap the orb once: MYRA connects to Gemini Live and keeps listening (hands-free) - speak, she answers in her own voice, then listens again. Tap again to stop. Turn on *Headphones* in settings to interrupt her mid-sentence. Chrome needs mic permission.

## Phone automation tools (Termux)

Apps by name (WhatsApp, Instagram, Spotify, YouTube, camera, settings...), YouTube/Spotify search, WhatsApp chat with your message filled in,
Google Maps navigation, alarm and timer, dialer, contacts lookup ("Mummy ko SMS bhejo"), SMS, calls, camera photo, Wi-Fi, torch, volume,
brightness, clipboard, location, notifications, share, download, media player.
SMS, calls and WhatsApp always ask your permission first (Allow/Deny card in the UI).

Android does not let apps tap inside other apps without root/ADB, so Spotify/YouTube open the search and you tap the result; WhatsApp opens the
chat with your message and you press Send. MYRA tells you this honestly instead of pretending.

The UI listens on 127.0.0.1 only, and every request needs a random token from the link printed in Termux.

## Update

```
pip install --upgrade myra-termux
```

## Usage

| Command | What it does |
|---|---|
| `myra-termux` | **Phone UI** in your browser (on Termux) / terminal chat (on Linux) |
| `myra-termux web` | Phone UI (add `--port 9000` or `--no-open`) |
| `myra-termux chat` | Terminal chat |
| `myra-termux alias` | Create the `myra` shortcut (then just type `myra`) |
| `myra-termux --voice` | Speak and listen (Termux:API) |
| `myra-termux --language Tamil` | Set language (any of 148+; `auto` = Hinglish) |
| `myra-termux --languages` | List all languages |
| `myra-termux --name Rahul` | Set your name |
| `myra-termux --ask "battery kitni hai?"` | One-shot question |

You can also say it naturally: "speak Spanish", "tamil me bolo", "mera naam Rahul hai", "torch on karo", "mummy ko SMS bhejo".

SMS and calls always ask for your confirmation first.

## Notes

- Your API key is stored in `~/.myra_termux/config.json` (user-only permissions). Env var `GEMINI_API_KEY` also works.
- Voice quality varies by language; big languages (Hindi, English, Spanish, Japanese, Tamil...) are best.
- This package is pure Python with no dependencies.
