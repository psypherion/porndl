# VidFetch
V 0.03

![image](https://github.com/user-attachments/assets/f948b72d-da6c-494e-b0a3-522d6cc36de8)


___
**VidFetch** is a Python-based tool for extracting and downloading video content from an adult site -> [click Here](https://spankbang.com). This tool enables users to easily retrieve video links and save videos locally with minimal setup.

## Features

- V 0.03 :
___
        1. Extracts video download links from specified web pages.
        2. Downloads videos using `curl`, supporting various video formats.
        3. Simple command-line interface for ease of use.
        4. Now supports Windows(untested) and Linux (both arch & debian)
        5. added curlSetup.py for automating curl download and installation
        6. Playlist Downloader
        7. Download History Log
        8. Playlist Downloading multiple webpage support.
___

- V 1.0 (probable features):
___
1. Front-end:

**User Interface**:
        Simple and intuitive design for ease of use.
        Responsive layout for various screen sizes and devices.
        Video and Playlist Integration:
        Interface for users to input video or playlist URLs.
        Display of progress and status updates for downloads.
**Error Handling**:
        User-friendly error messages and notifications.
**Download Management**:
        Options for custom file naming.
        Display list of downloaded videos with options to view or delete.
___
2. Back-end:

**Video and Playlist Downloading**:
        Extraction of video download links from provided URLs.
        Handling of both single video and playlist downloads.
**Pagination Handling**:
        Support for pagination in playlists with automatic page fetching.
**Curl Integration**:
        Use of curl for video downloading with fallbacks and installation checks.
___
## Files

- `requirements.txt`: Lists the Python dependencies required for the project.
- `spnkgbng.py`: Contains the `VideoDownloader` class which handles the extraction and downloading of videos.
- `main.py`: The main script that prompts the user for a video URL and initiates the download process.
- `curlSetup.py` : Contains `curlDownloader` class which handles the curl download and installation for various system. (added in version 0.02)
- `app.log` : will contain logs of downloads (automatically created)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ky13-troj/vidFetch.git
   cd vidFetch
   ```
   or, you can downoad the [zipfile](https://github.com/ky13-troj/vidFetch/archive/refs/heads/main.zip)
2. **Install Dependencies:**
(assuming you've python installed already)Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
Run the Tool:
   ```bash
   python main.py
   ```
___

![Single Video download](https://github.com/user-attachments/assets/4a307e8a-8401-4ee6-bab8-415800759465)


___


![Now Supports Downloading Playlists](https://github.com/user-attachments/assets/8184ce6e-faae-44e0-90a1-b467d78417fe)

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing**
Feel free to open issues or submit pull requests if you have suggestions or improvements for the tool.
