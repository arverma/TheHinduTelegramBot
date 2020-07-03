from datetime import datetime
from os import path
from glob import glob
from bot import TelegramChatbot
import csv

JOB_RUN_ID_FORMAT = '%-d %b'


def find_file_with_ext(dr, ext):
    return glob(path.join(dr, "*.{}".format(ext)))


def get_today_date():
    now = datetime.now()
    return now.strftime(JOB_RUN_ID_FORMAT)


def get_latest_thehindu_epaper_link(content):
    table = content.find('ul', attrs={'class': 'list-group list-group-flush'})
    links = []
    date = get_today_date()
    for row in table.findAll('li'):
        if row.a:
            links.append((row.text, row.a['href']))
            print(date, row.text, row.a['href'])
    resp = [link[1] for link in links if date in link[0]]
    print(resp)
    return resp


def get_file_id(urls):
    fileids = []
    for url in urls:
        fileids.append(url.split("/")[5])
    return fileids


def get_destination(url):
    file_name = []
    for i in range(len(url)):
        date = get_today_date()
        file_name.append("TheHindu_{}_{}.pdf".format(date, i).replace(" ", "_"))
    return file_name


def send_to_telegram(url):
    bot = TelegramChatbot()
    chat_ids = get_chat_ids()
    file_name = get_destination(url)
    for file in file_name:
        file_id = None
        for i_d in chat_ids:
            file_id = bot.send_news_paper_to_bot(i_d, file, file_id)


def get_chat_ids():
    with open('chat_id.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print("sent to: ", data)
    return data[0]
