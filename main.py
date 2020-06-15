from bs4 import BeautifulSoup
import requests
import os

from download_file import download_file_from_google_drive
from utils import get_latest_thehindu_epaper_link, get_file_id, get_destination, get_today_date, find_file_with_ext

if __name__ == "__main__":
    page = requests.get("https://www.newspaperpdf.online/download-the-hindu-adfree.php")
    soup = BeautifulSoup(page.content, 'html.parser')

    download_link = get_latest_thehindu_epaper_link(soup)
    print(download_link)
    file_ids = get_file_id(download_link)
    destinations = get_destination(download_link)
    print(file_ids, destinations)
    for file_id, destination in zip(file_ids, destinations):
        download_file_from_google_drive(file_id, destination)
        yesterday_date = str(int(get_today_date()) - 1)
        pdf_files = find_file_with_ext(".", "pdf")
        print(pdf_files)
        for file in pdf_files:
            if yesterday_date in file:
                os.remove(file)
