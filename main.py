from spnkbng import VideoDownloader

def main():
    link = input("Enter the link: ")
    downloader = VideoDownloader(link)
    downloader.run()

if __name__ == "__main__":
    main()
