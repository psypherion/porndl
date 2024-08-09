from spnkbng import VideoDownloader

def main():
    link = input("Enter the video page URL: ")
    downloader = VideoDownloader(link)
    downloader.run()

if __name__ == "__main__":
    main()
