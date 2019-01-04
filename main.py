import  time
from tg_bot import Bot
import bitcoin_price

bot = Bot('744390326:AAH3Af_5ypxRRB_hhAUollRw44gijKowtAs')

def main():
    new_offset = None
    while (True):
        last_upd = bot.get_last_update()

        upd_id = last_upd['update_id']
        chat_id = last_upd['message']['chat']['id']

        bot.send_message(chat_id, bitcoin_price.get_price())
        new_offset = upd_id +1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
