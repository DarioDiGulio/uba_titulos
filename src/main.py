import os

from flask import Flask
from dotenv import load_dotenv

from server.AppConfig import AppConfig
from server.Application import Application

load_dotenv()

server = Flask(__name__)
PORT = int(os.environ['PORT'])
DEBUG = bool(os.environ['PORT'])
config = AppConfig(PORT, DEBUG)
app = Application(server, config)

if __name__ == '__main__':
    app.run()
