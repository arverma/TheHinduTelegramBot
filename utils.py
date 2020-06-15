from datetime import datetime
from os import path
from glob import glob

JOB_RUN_ID_FORMAT = '%d'


def find_file_with_ext(dr, ext):
    return glob(path.join(dr, "*.{}".format(ext)))


def get_today_date():
    now = datetime.now()
    return now.strftime(JOB_RUN_ID_FORMAT)


def get_latest_thehindu_epaper_link(content):
    # print(content)
    table = content.find('ul', attrs={'class': 'list-group list-group-flush'})
    # print("\n\n\n")
    # print(table)
    links = []
    # print("\n\n\n")
    date = get_today_date()
    for row in table.findAll('li'):
        if row.a:
            # print(row.text)
            # print(row.a['href'])
            links.append((row.text, row.a['href']))
    return [link[1] for link in links if date in link[0]]


def get_file_id(urls):
    fileids = []
    for url in urls:
        fileids.append(url.split("/")[5])
    return fileids


def get_destination(url):
    file_name = []
    for i in range(len(url)):
        date = get_today_date()
        file_name.append("TheHindu_{}_{}.pdf".format(date, i))
    return file_name
