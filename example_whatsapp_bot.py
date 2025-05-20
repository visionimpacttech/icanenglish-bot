
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from .user_profile import UserProfile
from .bot_engine import get_response


app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    msg = request.form.get('Body')
    user = UserProfile(name="Ravi", age=22, region="Hubli", level="Starter")
    reply = get_response(msg, user)
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

    
