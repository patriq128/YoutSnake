<p float="left">
  <img src="Images/Yout.png" width="250" height="250" style="margin-right: 20px;" />
  <img src="Images/Snake.png" width="250" height="250" />
</p>

YoutSnake is a terminal-based media downloader written in Python.  
It provides a clean CLI interface for downloading audio (MP3) from supported platforms using `yt-dlp`, with automatic dependency handling and basic OS detection.

The project is designed as a modular tool and is planned to be extended with configuration files, advanced sorting, and video download support.

---

## Features

- Terminal-based interactive menu
- Download audio as MP3 using `yt-dlp`
- Playlist and multiple-link support
- Automatic installation of required dependencies
- Cross-platform support:
  - Windows
  - Linux
  - macOS
  - Termux (Android)
- Colored CLI output and custom ASCII interface

---

## Planned Features

- Configuration file with advanced settings
- MP4 video download support
- Automatic file sorting and organization
- Quality and format selection
- Improved error handling and logging

---

## Requirements

- Python 3.9 or newer
- pip (Python package manager)
- FFmpeg (required by `yt-dlp` for audio extraction)

---

## Installation

```bash
git clone https://github.com/patriq128/YoutSnake.git
```
---

## Run

```bash
cd YoutSnake
python YoutSnake.py
```

If `yt-dlp` is not installed, YoutSnake will automatically offer to install it.

---

## Usage

After launching the script, you will be presented with an interactive terminal menu.

- Select an option by typing its number
- Paste one or more links and press Enter
- Type `ok` to start downloading
- Type `exit` at any time to quit

Downloaded files are saved into the `Music/` directory.

---

## Warning

This project is intended **for personal and educational use only**.

Downloading copyrighted content without permission may violate local laws or the terms of service of the content provider.  
The author of this project is **not responsible** for any misuse of this software.

You are solely responsible for how you use this tool.

---

## Support me

If you like this project (or not ), feel free to support me on Ko-fi.
I'm a student working on future projects and every support help :3

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X8X01GCK06)
