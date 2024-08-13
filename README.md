# prn-dl

V 0.04

 ![image](https://github.com/user-attachments/assets/f948b72d-da6c-494e-b0a3-522d6cc36de8)

 ![image](https://github.com/user-attachments/assets/873c8ec4-cc04-4e15-9a9e-51c5ed1be061)


___

**prn-dl** is a Python-based cli tool for extracting and downloading video content from an adult sites -> 

1. [spankbang](https://spankbang.com).
2. [xfree](https://www.xfree.com).

   This tool enables users to easily retrieve video links and save videos locally with minimal setup.

## Features

### V 0.03

* **Video Downloading:**

  
  1. Extracts video download links from specified web pages.
  2. Downloads videos using `curl`, supporting various video formats.
* **User Interface:**
  1. Simple command-line interface for ease of use.
* **Platform Support:**
  1. Supports Windows (untested) and Linux (both Arch & Debian).
* **Additional Tools:**
  1. Added `curlSetup.py` for automating `curl` download and installation.
* **Playlist Management:**
  1. Playlist Downloader.
  2. Playlist downloading with multiple webpage support.
* **Logging:**
  1. Download History Log.

### V 0.04

* **X-free**
  
  1. Now supports downloading videos from xfree

### V 1.0 (Probable Features)

#### 1. Front-end

* **User Interface:**
  * Simple and intuitive design for ease of use.
  * Responsive layout for various screen sizes and devices.
  * Video and playlist integration:
    * Interface for users to input video or playlist URLs.
    * Display of progress and status updates for downloads.
* **Error Handling:**
  * User-friendly error messages and notifications.
* **Download Management:**
  * Options for custom file naming.
  * Display list of downloaded videos with options to view or delete.


## Files

* `requirements.txt`: Lists the Python dependencies required for the project.
* `spnkgbng.py`: Contains the `VideoDownloader` class which handles the extraction and downloading of videos.
* `main.py`: The main script that prompts the user for a video URL and initiates the download process.
* `curlSetup.py` : Contains `curlDownloader` class which handles the curl download and installation for various system. (added in version 0.02)
* `app.log` : will contain logs of downloads (automatically created)

## Installation


1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ky13-troj/prn-dl.git
   cd prn-dl
   ```

   or, you can downoad the [zipfile](https://github.com/ky13-troj/prn-dl/archive/refs/heads/main.zip)
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
