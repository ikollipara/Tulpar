"""
tulpar/html_dsl/head.py
Ian Kollipara
2022.05.03

Head Html Tag
"""

# Imports


from typing import Iterable


class Head:

    """ Header HTML Tag
    
    This represents the <head> tag.
    """
    
    def __init__(self) -> None:
        self.children: Iterable = []
    

    def __getitem__(self, values: Iterable):
        self.children = values
    
    def __str__(self) -> str:
        return f"<head>{''.join(str(child) for child in self.children)}</head>"