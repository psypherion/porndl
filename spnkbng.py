import httpx
from bs4 import BeautifulSoup
import os
from curlSetup import CurlInstaller  

class VideoDownloader:
    def __init__(self, video_page_url):
        self.video_page_url = video_page_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Referer": "https://spankbang.com/",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }
        self.session = httpx.Client(headers=self.headers)
        self.curl_installer = CurlInstaller()  

    def extract_vdownload_link(self):
        response = self.session.get(self.video_page_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        video_container = soup.find('div', id='video_container')
        if video_container:
            video_tag = video_container.find('video', id='main_video_player')
            if video_tag:
                source_tag = video_tag.find('source')
                if source_tag:
                    vdownload_link = source_tag.get('src')
                    return vdownload_link

        return None

    def downloader(self, video_url, name):
        
        if not self.curl_installer.is_curl_installed():
            print("curl is not installed. Installing curl...")
            self.curl_installer.install_curl()
        else:
            print("curl is already installed.")

        # Download the video using curl
        os.system(f'curl -o {name}.mp4 "{video_url}"')

    def run(self):
        video_link = self.extract_vdownload_link()
        if video_link:
            print(f"Video link extracted: {video_link}")
            name = self.video_page_url.split("video/")[1]
            if "+" in name:
                name = name.replace("+", "_")
            self.downloader(video_link, name)
        else:
            print("Failed to extract the video link.")

class PlaylistDownloader:
    pass

if __name__ == "__main__":
    link = input("Enter the video page URL: ")
    video_downloader = VideoDownloader(link)
    video_downloader.run()
