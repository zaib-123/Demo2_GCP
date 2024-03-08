from flask import Flask 
import os

app = Flask(__name__)

@app.route("/")

def wish():
    message = "{name} is a leading service provider"
    return message.format(name=os.getenv("NAME", "Networklogic"))
if __name__ == "__main__":
   app. run (host='0.0.0.0', port=80)