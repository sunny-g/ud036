''' lesson 2 - sms texting app
build a texting from computer app

don't try to understand all the code in an example UNTIL YOU GET IT TO RUN

similarities between rest.TwilioRestClient() and turtle.Turtle()
    both call __init__() and instantiate an obj of the respective class
    both define things that the objs of that class can do, like a blueprint
        TRC contains info on how to communicate w/ Twilio and send an sms
        Turtle contains info on how to make a thing draw other things


'''
# imports class TwilioRestClient from rest folder within twilio folder
from twilio.rest import TwilioRestClient

account_sid = 'AC878c5d1b40d909bbdc4358f9ad9838bc'
# retrieves auth_token from saved file
auth_file = open('/Users/sunnyg/Dropbox/programs/learning/python/ud036/lesson2/twilio_auth.py')
auth_token = auth_file.readlines()[0].split()[0]
auth_file.close()

def sendSMS(message, destinationNumber):
    client = TwilioRestClient(account_sid, auth_token)

    message = client.sms.messages.create(
        body=message,
        to=destinationNumber,
        from_="+15127824051")

    print message.sid

sendSMS("fuck you gumby", "")
