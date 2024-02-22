from flask import Flask 
import os
import sys

app = Flask(__name__)

@app.route("/")
def wish():
    message = "{name} is a leading service provider"
    return message.format(name=os.getenv("NAME", "Networklogic"))

if __name__ == "__main__":
    host = '0.0.0.0' if len(sys.argv) < 2 else sys.argv[1]
    port = 8080 if len(sys.argv) < 3 else int(sys.argv[2])
    app.run(host=host, port=port)
