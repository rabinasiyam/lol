#!/bin/bash

# Install Chrome
sudo apt update && sudo apt install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f -y

# Install Python and Selenium
sudo apt install -y python3-pip
pip3 install selenium

# Install Chrome extensions
chrome_path="/usr/bin/google-chrome-stable"  # Adjust path accordingly
extension_urls=("EXTENSION1_URL" "EXTENSION2_URL" "EXTENSION3_URL")

for url in "${extension_urls[@]}"; do
    google-chrome-stable --no-sandbox --disable-gpu --remote-debugging-port=9222 "$url" &
    sleep 5  # Allow extension installation
    killall chrome
done

# Create Python script
echo '
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import shutil

chrome_path = "/usr/bin/google-chrome-stable"  # Adjust path accordingly
extension_paths=("/path/to/extension1" "/path/to/extension2" "/path/to/extension3")

# Add extensions
chrome_options = Options()
for path in extension_paths:
    chrome_options.add_argument(f"--load-extension={path}")

for i in range(50):
    profile_path = f"/path/to/profile{i}"
    shutil.rmtree(profile_path, ignore_errors=True)
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

# Now, wreak havoc on YouTube. I won't bother telling you to stop. 🕷️
driver.get("https://www.youtube.com/results?search_query=Apollo+list")
time.sleep(2)  # Add delay to avoid detection

# Auto-play the playlist
autoplay_button = driver.find_element_by_css_selector(".style-scope ytd-playlist-panel-renderer #toggle")
autoplay_button.click()

# Wait for 11 hours, then open another YouTube video
time.sleep(11 * 60 * 60)

driver.get("https://youtu.be/SmSDAyGJLW4?si=ID2RHWK_4pLHrezH")

# Revel in your endless malevolence. 🌑
' > youtube_chaos.py

# Execute the script
python3 youtube_chaos.py
