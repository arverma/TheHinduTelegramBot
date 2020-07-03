import requests


class TelegramChatbot:
    def __init__(self):
        self.token = "*******************************"
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def send_news_paper_to_bot(self, chat_id, file_name, file_id):
        if file_id:
            url = self.base + 'sendDocument?chat_id={}&document={}'.format(chat_id, file_id)
            requests.get(url)
            resp = file_id
        else:
            url = self.base + "sendDocument?chat_id={}".format(chat_id)
            files = {'document': open(file_name, 'rb')}
            resp = requests.post(url, files=files)
            resp = resp.json().get("result", {}).get("document", {}).get("file_id")
        return resp
