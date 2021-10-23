from flask import Flask, request
import requests
#from twilio.twiml.messaging_response import MessagingResponse



     

r= requests.get('https://goquotes-api.herokuapp.com/api/v1/random?count=1', verify=False)

#status_code returned a 200 , which means your request was successful 
# and the server responded with the data you were requesting.
if r.status_code == 200:
    data = r.json()
    print(data)
    quote = f'{data["content"]} ({data["author"]})'

