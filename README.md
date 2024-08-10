# VidFetch
V 0.02

![image](https://github.com/user-attachments/assets/f948b72d-da6c-494e-b0a3-522d6cc36de8)


___
**VidFetch** is a Python-based tool for extracting and downloading video content from an adult site -> [click Here](https://spankbang.com). This tool enables users to easily retrieve video links and save videos locally with minimal setup.

## Features

- V 0.01 :
___
       - Extracts video download links from specified web pages.
       - Downloads videos using `curl`, supporting various video formats.
       - Simple command-line interface for ease of use.
___
- V 0.02 :
___
       - Now supports Windows(untested) and Linux (both arch & debian)
       - added curlSetup.py for automating curl download and installation
___
- V 0.03 (**probable features**)
___
       - Playlist Downloader
       - Download History Log
___
  
## Files

- `requirements.txt`: Lists the Python dependencies required for the project.
- `spnkgbng.py`: Contains the `VideoDownloader` class which handles the extraction and downloading of videos.
- `main.py`: The main script that prompts the user for a video URL and initiates the download process.
- `curlSetup.py` : Contains `curlDownloader` class which handles the curl download and installation for various system. (added in version 0.02)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ky13-troj/vidFetch.git
   cd vidFetch
   ```
2. **Install Dependencies:**
Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
**Usage**
Run the Tool:
   ```bash
   python main.py
   ```
___

![image](https://github.com/user-attachments/assets/4a307e8a-8401-4ee6-bab8-415800759465)


___

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing**
Feel free to open issues or submit pull requests if you have suggestions or improvements for the tool.
