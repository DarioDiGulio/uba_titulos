from flask import Blueprint
from flask.views import View


class HomeController(View):
    def __init__(self):
        pass

    def dispatch_request(self):
        return 'Hola mundo'
