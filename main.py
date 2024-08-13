from vidFetch import VideoDownloader, PlaylistDownloader

def main():
    link = input("Enter the URL: ")
    
    if "playlist" in link:
        print("Detected a playlist URL.")
        downloader = PlaylistDownloader(link)
    else:
        print("Detected a single video URL.")
        downloader = VideoDownloader(link)
    
    downloader.run()

if __name__ == "__main__":
    main()
