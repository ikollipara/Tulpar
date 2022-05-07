"""
tulpar/model.py
Ian Kollipara
2022.04.10

Model Decorator Definition
"""

# Imports
from typing import Optional, Type

from .tulpar import Tulpar


class Model:
    """Create a PonyORM model

    This decorator serves to denote PonyORM models. It automatically
    connects them to your application, and is type-safe. If you would 
    like a custom table name, set the table_name parameter to a string
    value.
    """

    def __init__(self, table_name: Optional[str] = None) -> None:
        self._table_name = table_name

    def __call__(self, model_cls: Type):

        if self._table_name:
            model = type(model_cls.__name__, (Tulpar.db.Entity,), model_cls.__dict__ | {"_table_": self._table_name})
        else:
            model = type(model_cls.__name__, (Tulpar.db.Entity,), model_cls.__dict__)

        return model
