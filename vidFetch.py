import os
import re
import httpx
from bs4 import BeautifulSoup
import logging
import shlex
from curlSetup import CurlInstaller

logging.basicConfig(
    filename='app.log',  
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

DOWNLOAD_DIR = "downloads"

if DOWNLOAD_DIR not in os.listdir():
    os.mkdir(DOWNLOAD_DIR)

SITES = ["spankbang", "xfree"]
class VideoDownloader:
    def __init__(self, video_page_url, file_name=None):
        self.video_page_url = video_page_url
        self.file_name = file_name
        self.flag = None
        if SITES[0] in video_page_url:
            self.site = "https://"+SITES[0]+".com/"
            self.flag = 0
        elif SITES[1] in video_page_url:
            self.site = "https://"+SITES[1]+".com/"
            self.flag = 1
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Referer": f"{self.site}",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }
        self.session = httpx.Client(headers=self.headers)
        self.curl_installer = CurlInstaller()

    def extract_vdownload_link(self):
        response = self.session.get(self.video_page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        vdownload_link = None
        if self.flag == 0:
            video_container = soup.find('div', id='video_container')
            if video_container:
                video_tag = video_container.find('video', id='main_video_player')
                if video_tag:
                    source_tag = video_tag.find('source')
                    if source_tag:
                        vdownload_link = source_tag.get('src')
        elif self.flag == 1:
            pattern = re.compile('/xfree-prod/(.+?)/full.mp4')
            matches = re.findall(pattern, response.content.decode("UTF-8"))
            if matches:
                vdownload_link = f"https://cdn.xfree.com/xfree-prod/{matches[0]}/full.mp4"
        return vdownload_link

    def downloader(self, video_url):
        if not self.curl_installer.is_curl_installed():
            print("curl is not installed. Installing curl...")
            self.curl_installer.install_curl()
        else:
            print("curl is already installed.")
        if "title=" in self.video_page_url:
            self.file_name=self.video_page_url.split("title=")[1]
        elif "id=" in self.video_page_url:
            self.file_name=self.video_page_url.split("id+")[1]
        name = self.file_name if self.file_name else self.video_page_url.split("video/")[1]
        name = name.replace("+", "_").replace(" ", "_").replace("/", "_").replace("\\", "_").replace("-", "_")
        if os.path.exists(f"{DOWNLOAD_DIR}/{name}.mp4"):
            name = f"{name}_{int(os.path.getmtime(f'{name}.mp4'))}"
        safe_name = shlex.quote(name)
        
        os.system(f'curl -o {DOWNLOAD_DIR}/{safe_name}.mp4 "{video_url}"')

        logging.info(f"Downloaded video '{DOWNLOAD_DIR}/{name}' from URL: {video_url}")

    def run(self):
        video_link = self.extract_vdownload_link()
        if video_link:
            print(f"Video link extracted: {video_link}")
            self.downloader(video_link)
        else:
            print("Failed to extract the video link.")
            logging.error(f"Failed to extract video link from URL: {self.video_page_url}")

class PlaylistDownloader:
    def __init__(self, playlist_link):
        self.base_url = playlist_link
        self.session = httpx.Client()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Referer": "https://spankbang.com/",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }
        self.session.headers.update(self.headers)
        self.process_playlist()

    def extract_vdo_link(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        video_items = soup.find_all('div', class_='video-item')
        href_values = {}
        for item in video_items:
            a_tag = item.find('a', class_='thumb')
            if a_tag and 'href' in a_tag.attrs and 'title' in a_tag.attrs:
                href_values[str(a_tag['title'])] = f"https://spankbang.com{a_tag['href']}"
        return href_values

    def process_playlist(self):
        page_number = 1
        while True:
            url = self.base_url if page_number == 1 else f"{self.base_url}/{page_number}"
            print(f"Processing page: {url}")
            video_links = self.extract_vdo_link(url)
            if not video_links:
                print(f"No videos found on page {page_number}.")
                logging.info(f"No videos found on page {page_number}.")
                break

            for title, video_link in video_links.items():
                if self.base_url.split("/")[3] in video_link:
                    print(f"Processing video: {video_link} with title: {title}")
                    logging.info(f"Processing video: {video_link} with title: {title}")
                    video_downloader = VideoDownloader(video_link, title)
                    video_downloader.run()

            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            if soup.find('div', id='error_pages'):
                print(f"No more pages after page {page_number}.")
                logging.info(f"No more pages after page {page_number}.")
                break
            
            page_number += 1

if __name__ == "__main__":
    link = input("Enter the video or playlist URL: ")
    if "playlist" in link:
        PlaylistDownloader(link)
    else:
        VideoDownloader(link).run()
