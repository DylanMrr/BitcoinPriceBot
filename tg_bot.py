import requests
import datetime


class Bot:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset = None, timeout = 30):
        method = 'getUpdates'
        params = {'timeout':timeout, 'offset':offset}
        return requests.get(self.api_url + method, params).json()['result']

    def send_message(self, chat_id, text):
        params = {'chat_id':chat_id, 'text':text}
        method = 'sendMessage'
        return requests.post(self.api_url + method, params)

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result)>0:
            last_upd = get_result[-1]
        else:
            last_upd = get_result[len(get_result)]
        return last_upd
