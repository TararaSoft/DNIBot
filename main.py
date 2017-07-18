import private
import random
import time
import telepot

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent


def control_digit_dni(num):
    letter = num % 23

    return {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X',
            11: 'B', 12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L',
            20: 'C', 21: 'K', 22: 'E'}[letter]


def control_digit_nie(num):
    letter = num % 3

    return {
        0: 'X', 1: 'Y', 2: 'Z'
    }[letter]


def generate_dni():
    num = random.randint(9999999, 100000000)
    return str(num) + control_digit_dni(num)


def generate_nie():
    num = random.randint(999999, 10000000)
    return str(num) + control_digit_nie(num)


def on_chat_message(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/randomdni':
        bot.sendMessage(chat_id, generate_dni())
    elif command == '/randomnie':
        bot.sendMessage(chat_id, generate_nie())
    # elif command == '/verify':


def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)

        articles = []

        if query_string == 'dni':
            for i in xrange(3):
                res = generate_dni()
                articles.append(InlineQueryResultArticle(
                    id=res,
                    title=res,
                    input_message_content=InputTextMessageContent(
                        message_text=res
                    )
                ))
        elif query_string == 'nie':
            for i in xrange(3):
                res = generate_nie()
                articles.append(InlineQueryResultArticle(
                    id=res,
                    title=res,
                    input_message_content=InputTextMessageContent(
                        message_text=res
                    )
                ))
        elif len(query_string) == 7 and query_string.isdigit():
            res = query_string + control_digit_nie(int(query_string))
            articles.append(InlineQueryResultArticle(
                id=res,
                title=res,
                input_message_content=InputTextMessageContent(
                    message_text=res
                )
            ))
        elif len(query_string) == 8 and query_string.isdigit():
            res = query_string + control_digit_dni(int(query_string))
            articles.append(InlineQueryResultArticle(
                id=res,
                title=res,
                input_message_content=InputTextMessageContent(
                    message_text=res
                )
            ))

        return articles

    answerer.answer(msg, compute)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)


bot = telepot.Bot(private.token)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message,
                  'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result
                  }).run_as_thread()

print 'I am listening ...'

while 1:
    time.sleep(10)
