"""
tulpar/html_dsl/html.py
Ian Kollipara
2022.05.01

Html Class Definition
"""

# Imports


from typing import Iterable


class Html:

    """ Html Element Class
    
    Tulpar uses an HTML DSL for its endpoints. This
    the implementation for the whole page.
    """

    def __init__(self) -> None:
        self.children: Iterable = []
        self.lang = "en"
    
    def set_lang(self, lang: str) -> "Html":
        self.lang = lang
        return self
    
    def __getitem__(self, values: Iterable):
        self.children = values

    def __str__(self) -> str:
        return f"<html>{'\n'.join(str(child) for child in self.children)}</html>"