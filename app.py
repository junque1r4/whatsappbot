from flask import Flask, request
import requests
from modules.scrapping import meme
import secrets
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'citar' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Não consegui recuperar uma citação neste momento, desculpe.'
        msg.body(quote)
        responded = True

    if 'gato' in incoming_msg or 'gata' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded = True

    if 'meme' in incoming_msg or 'mene' in incoming_msg:
        quote = 'Hmm... Que tal esse?'
        resp.message().body(quote)
        msg.media(meme(secrets.randbelow(6500)))
        responded = True

    if 'arthur' in incoming_msg:
        quote = 'Hmm... Que tal esse?'
        resp.message().body(quote)
        responded = True

    if not responded:
        msg.body('Só conheço frases, memes e gatos famosos, desculpe!')
    return str(resp)

if __name__ == '__main__':
   app.run(debug=True)