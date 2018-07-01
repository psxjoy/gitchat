from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC141778d2eed2ba022112c91157426103"
# Your Auth Token from twilio.com/console
auth_token  = "55738589b6ac6246896de0977500e63e"

client = Client(account_sid, auth_token)
def send_sms(sms_text):
    message = client.messages.create(
        to="你的手机号码",
        from_="twilio给你的号码",
        body=sms_text)
    print(message.sid)