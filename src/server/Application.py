from flask import Flask

from server.AppConfig import AppConfig
from server.controllers.HomeController import HomeController


class Application:
    def __init__(self, server: Flask, config: AppConfig):
        self.__server = server
        self.__config = config
        self.__init_controllers()

    def __init_controllers(self):
        self.__server.add_url_rule('/', view_func=HomeController.as_view(''))

    def run(self):
        self.__server.run(
            port=self.__config.port,
            debug=self.__config.debug
        )
