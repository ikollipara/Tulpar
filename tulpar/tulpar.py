"""
tulpar/tulpar.py
Ian Kollipara
2022.04.19

Tulpar Main File
"""

# Imports
from os import getcwd
from typing import List
from pony.orm import Database
from falcon import App, MEDIA_HTML


from .config import TulparConfig


class Tulpar:

    """ Tulpar Application
    
    Tulpar is the main class of a Tulpar Application. It
    contains all the initialization code, as well as any
    customization of the application.

    This is what should be called when running the app in
    gunicorn.
    """

    db = Database()
    __app = App(MEDIA_HTML)
    __app_dir = getcwd()
    
    def __init__(self, config: TulparConfig) -> None:
        self.config = config
    
    def __call__(self, env, start_response):
        return self.__app(env, start_response)
    
