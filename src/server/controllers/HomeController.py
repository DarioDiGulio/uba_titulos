from flask import render_template
from flask.views import View


class HomeController(View):
    def __init__(self):
        pass

    def dispatch_request(self):
        return render_template('index.html')
