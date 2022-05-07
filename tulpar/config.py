"""
tulpar/config.py
Ian Kollipara
2022.04.19

Tulpar Config Class Definition
"""

# Imports
from functools import singledispatchmethod
from typing import Any, List, TypedDict, Literal, Tuple
class SQLiteParams(TypedDict):
    """SQLiteParams denotes the parameters
    needed for an SQLite PonyORM DB Connection.
    """

    filename: str
    create_db: bool


class PostgresParams(TypedDict):
    """PostgresParams denotes the parameters
    needed for an Postgres PonyORM DB Connection.
    """

    user: str
    password: str
    host: str
    database: str


class MySQLParams(TypedDict):
    """MySQLParams denotes the parameters
    needed for an MySQL PonyORM DB Connection.
    """

    user: str
    passwd: str
    host: str
    database: str


class OracleParams(TypedDict):
    """OracleParams denotes the parameters
    needed for an Oracle PonyORM DB Connection.
    """

    user: str
    password: str
    dsn: str


class CockroachParams(TypedDict):
    """CockroachParams denotes the parameters
    needed for an Cockroach PonyORM DB Connection.
    """

    user: str
    passwd: str
    host: str
    database: str
    sslmode: Literal["disable"]


DB_PARAMS = (
    Tuple[Literal["sqlite"], SQLiteParams]
    | Tuple[Literal["postgres"], PostgresParams]
    | Tuple[Literal["mysql"], MySQLParams]
    | Tuple[Literal["oracle"], OracleParams]
    | Tuple[Literal["cockroach"], CockroachParams]
)

class TulparConfig:

    """ TulparConfig
    
    This class implements the builder pattern to set its attributes.
    This is done via a context manager. These settings are used in
    bootstrapping the Tulpar Application.
    """

    def __init__(self) -> None:
        self.app_name = ""
        self.db_params: DB_PARAMS = ("sqlite", SQLiteParams(filename=":memory:", create_db=False))
        self.middleware = []
    
    def set_app_name(self, app_name: str):
        """ Set the App Name.
        
        Given an app name, set the name.
        """
        
        self.app_name = app_name
        return self
    
    def set_db_params(self, db_params: DB_PARAMS):
        """ Set the Database Settings
        
        Set the Database Params.
        """
        
        self.db_params = db_params
        return self
    
    @singledispatchmethod
    def add_middleware(self, middleware: Any):
        self.middleware.append(middleware)
        return self
    
    @add_middleware.register
    def _(self, middleware: List[Any]):
        self.middleware += middleware
        return self
