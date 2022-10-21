from flask import Flask

from src.api.Server.AppConfig import AppConfig


class Application:
    def __init__(self, server: Flask, config: AppConfig):
        self.__server = server
        self.__config = config

    def run(self):
        self.__server.run(
            port=self.__config.port,
            debug=self.__config.debug
        )
