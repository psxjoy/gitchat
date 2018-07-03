from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC141778d2eed2ba022112c91157426103"
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)
def send_sms(to_number,from_number,sms_text):
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=sms_text)
    print(message.sid)