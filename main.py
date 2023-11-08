import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from datetime import datetime
import re
import tkinter as tk
from tkinter import filedialog

# Create a directory to store the downloaded images
downloaded_images_dir = 'downloaded_images'
if not os.path.exists(downloaded_images_dir):
    os.makedirs(downloaded_images_dir)

current_download_folder = os.path.abspath(downloaded_images_dir)


def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)


def download_images():
    base_url = base_url_entry.get()
    target_url = target_url_entry.get()

    # Start a Selenium WebDriver session
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r"chromedriver-win32\chromedriver.exe", options=chrome_options)
    driver.get(target_url)

    # Allow some time for dynamic content to load
    time.sleep(5)

    # Find all image elements using Selenium
    img_elements = driver.find_elements(By.TAG_NAME, 'img')

    # Download images to the current download folder
    download_folder = current_download_folder
    for index, img_element in enumerate(img_elements):
        img_src = img_element.get_attribute('src')
        img_url = urljoin(base_url, img_src)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        img_extension = img_url.split('.')[-1]
        img_name = f"{timestamp}_{index}.{img_extension}"
        img_name = sanitize_filename(img_name)
        img_path = os.path.join(download_folder, img_name)

        img_response = requests.get(img_url)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_response.content)

    # Close the WebDriver session
    driver.quit()
    result_label.config(text="All images downloaded successfully.")


def change_download_folder():
    global current_download_folder
    new_download_folder = filedialog.askdirectory()
    if new_download_folder:
        current_download_folder = new_download_folder


def access_download_folder():
    os.system(f'explorer {current_download_folder}')


# Create a Tkinter window
window = tk.Tk()
window.title("Image Downloader")

# Create input fields for base_url and target_url
base_url_label = tk.Label(window, text="Base URL:")
base_url_label.pack()
base_url_entry = tk.Entry(window)
base_url_entry.pack()

target_url_label = tk.Label(window, text="Target URL:")
target_url_label.pack()
target_url_entry = tk.Entry(window)
target_url_entry.pack()

# Create buttons to start the download, change the folder, and access the folder
start_button = tk.Button(window, text="Start Download", command=download_images)
start_button.pack()

change_folder_button = tk.Button(window, text="Change Download Folder", command=change_download_folder)
change_folder_button.pack()

access_folder_button = tk.Button(window, text="Access Download Folder", command=access_download_folder)
access_folder_button.pack()

# Create a label to display the download result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the GUI application
window.mainloop()
