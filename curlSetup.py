import os
import platform
import shutil
import subprocess
import sys
import requests
import zipfile

class CurlInstaller:
    def __init__(self):
        self.os_system = platform.system()

    def is_curl_installed(self):
        """Check if curl is installed."""
        return shutil.which('curl') is not None

    def download_curl_windows(self):
        """Download and install curl on Windows."""
        curl_url = 'https://curl.se/windows/dl-7.83.1/curl-7.83.1-win64-mingw.zip'
        zip_path = 'curl.zip'
        extract_path = 'curl'

        print("Downloading curl for Windows...")
        response = requests.get(curl_url, stream=True)
        response.raise_for_status()

        with open(zip_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print("Extracting curl...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        curl_executable = os.path.join(extract_path, 'curl-7.83.1-win64-mingw', 'bin', 'curl.exe')
        destination_path = os.path.join(os.getenv('SYSTEMROOT'), 'System32')

        print(f"Copying curl to {destination_path}...")
        shutil.copy(curl_executable, destination_path)
        
        print("Cleaning up...")
        os.remove(zip_path)
        shutil.rmtree(extract_path)
        
        print("curl installed successfully on Windows.")

    def install_curl_linux(self):
        """Install curl on Linux based on distribution."""
        distro = ""
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if "ID=" in line:
                        distro = line.strip().split('=')[1].strip('"')
                        break
        except FileNotFoundError:
            print("Could not determine the Linux distribution.")
            return
        
        if distro in ["ubuntu", "debian"]:
            print("Installing curl on Debian/Ubuntu...")
            os.system('sudo apt update && sudo apt install -y curl')
        elif distro in ["arch", "manjaro"]:
            print("Installing curl on Arch/Manjaro...")
            os.system('sudo pacman -Syu --noconfirm curl')
        else:
            print(f"Your distribution '{distro}' is not directly supported by this script. Please install curl manually.")

    def install_curl(self):
        """Main method to check and install curl based on OS."""
        if self.is_curl_installed():
            print("curl is already installed.")
        else:
            if self.os_system == "Windows":
                self.download_curl_windows()
            elif self.os_system == "Linux":
                self.install_curl_linux()
            else:
                print(f"Your operating system '{self.os_system}' is not supported by this script. Please install curl manually.")

if __name__ == "__main__":
    installer = CurlInstaller()
    installer.install_curl()
