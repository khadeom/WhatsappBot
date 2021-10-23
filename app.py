from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

#print("started")

app = Flask(__name__)

#/bot is end pointthat supports requests POST. 
# Every time a message from a user is received by Twilio this endpoint will be called. 
# The function body bot()will analyze the message sent by the user and provide the appropriate response.
@app.route('/bot', methods=['POST']) 
def bot():
    incoming_msg = request.values.get('Body', '').lower()

    '''
    The answer that Twilio expects from the webhook needs to be given in TwiML 
    or Twilio Markup Language , which is an XML-based language.
    MessagingResponse helps us do that
    '''
     
    resp = MessagingResponse()
    msg = resp.message()
    print(incoming_msg)
    responded = False
    if 'quote' in incoming_msg:
        # return quote image 
        r = requests.get('https://api.quotable.io/random')
        #r= requests.get('https://type.fit/api/quotes')

        #status_code returned a 200 , which means your request was successful 
        # and the server responded with the data you were requesting.
        if r.status_code == 200:
        #if True:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
            #quote = 'sorry message was not sent this time'
        else:
            quote = 'sorry message was not sent this time'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg or 'cats' in incoming_msg:
        # retorne uma foto de gato
        msg.media('https://cataas.com/cat')
        responded = True
    if "random" in incoming_msg:
        msg.media('https://picsum.photos/200/300')
        responded = True
    if not responded:
        msg.body('I only know famous quote and cats, sorry!.')
    return str(resp)

if __name__ == '__main__':
   app.run()