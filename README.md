# Image Scraper

This Python script allows you to scrape and download images from a website using Selenium and requests.

## Features

- Download images from a specified URL.
- Customize the base URL for image sources.
- Specify the download location for images.
- Access the downloaded images folder.

## Requirements

- Python 3.x
- Selenium (install using `pip install selenium`)
- Chrome WebDriver (included in the script)
- Requests (install using `pip install requests`)
- Tkinter (for the GUI, included with most Python installations)

## Usage

1. Clone or download the project to your local machine.

2. Install the required Python packages by running:

   ```shell
   pip install selenium requests
Make sure you have Google Chrome installed on your machine. The script uses the Chrome WebDriver, which is included in the project.

Run the script: 
python main.py

In the GUI, you can enter the base URL, target URL, and specify the download location for the images.

Click "Start Download" to begin the image download process.

Click "Change Download Folder" to select a new download folder.

Click "Access Download Folder" to open the current download folder in your system's file explorer.
