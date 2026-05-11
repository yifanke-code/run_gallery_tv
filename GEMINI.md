# run_gallery_tv

A Python-based video playlist manager and player using PySide6 and VLC media player. This project is designed to manage and display video content in a gallery or TV-like setup.

## Project Overview

The project consists of two main components:
1.  **Playlist Manager (`run_gallery_tv.py`)**: A GUI application to browse a directory of MP4 files, create and organize multiple playlists (lists 0-4), and trigger playback in VLC.
2.  **Full-screen Player (`run_gallery_tv_s.py`)**: A frameless, full-screen GUI intended for display output. It supports keyboard shortcuts for switching between playlists and monitors VLC to ensure it stays running.

### Key Technologies
- **Language**: Python 3
- **GUI Framework**: PySide6 (Qt for Python)
- **Playback Engine**: VLC Media Player (external process)
- **Configuration**: JSON-based storage (`run_gallery_tv.json`)

## Building and Running

### Prerequisites
- Python 3.x
- VLC Media Player installed at `C:\Program Files\VideoLAN\VLC\vlc.exe` (or adjusted in the scripts).

### Installation
Install the required Python packages:
```bash
pip install PySide6 python-vlc psutil pandas pyperclip
```

### Running the Manager
To manage playlists and directory settings:
```bash
python run_gallery_tv.py
```

### Running the Player
To start the full-screen display version:
```bash
python run_gallery_tv_s.py
```

## Project Structure

- `run_gallery_tv.py`: Main entry point for the playlist management interface.
- `run_gallery_tv_s.py`: Main entry point for the full-screen playback interface.
- `run_gallery_tv_ui.ui` / `run_gallery_tv_ui_ui.py`: UI definitions for the manager interface.
- `run_gallery_tv_s.ui` / `run_gallery_tv_s_ui.py`: UI definitions for the player interface.
- `run_gallery_tv.json`: Configuration file storing the video directory path and playlist contents.
- `dimension.setting`: (Optional) Local configuration for GUI component dimensions.
- `start_1.jpg`: Splash screen or background image for the player.

## Development Conventions

- **UI Updates**: The `.py` UI files are generated from `.ui` files using `pyside6-uic`. Avoid editing `*_ui.py` files directly; modify the `.ui` files in Qt Designer instead.
- **Configuration**: Playlists and the working directory are persisted in `run_gallery_tv.json`.
- **Playback**: Playback is handled by spawning VLC as a separate process with specific command-line arguments (e.g., `--one-instance`, `--loop`, `--fullscreen`).

## Usage

### Management Interface
- **Path**: Click the button to select the directory containing MP4 files.
- **Playlists**: Add files from the main list to any of the 4 sub-lists. Use "Up" and "Down" to reorder.
- **Play**: Click the play icon/button to start the playlist in VLC.

### Player Interface (Key Bindings)
- `1` - `4`: Play the respective playlist.
- `0` or `A`: Play the combined playlist (`list0`) in a loop.
- `K`: Close the application.
- `8`: Check if VLC is running.
