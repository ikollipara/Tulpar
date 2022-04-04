'''
tests/test_config.py
Ian Kollipara
2022.04.04

Testing tulpar.config
'''
# Imports
from tulpar import config


def test_sqlite_params():

    test = config.SQLiteParams(filename="test.db", create_db=True)
    successful = { "filename": "test.db", "create_db": True }
    failure = {}

    assert test.items() == successful.items()
    assert not test.items() == failure.items()

def test_posgres_params():

    test = config.PostgresParams(user="Ian", password="Test", host="test", database="test")
    successful = {"user": "Ian", "password": "Test", "host": "test", "database": "test"}
    failure = {}

    assert test.items() == successful.items()
    assert not test.items() == failure.items()

def test_mysql_params():

    test = config.MySQLParams(user="Ian", passwd="Test", host="test", database="test")
    successful = {"user": "Ian", "passwd": "Test", "host": "test", "database": "test"}
    failure = {}

    assert test.items() == successful.items()
    assert not test.items() == failure.items()

def test_oracle_params():
    test = config.OracleParams(user="Ian", password="Test", dsn="test")
    successful = {"user": "Ian", "password": "Test", "dsn": "test"}
    failure = {}

    assert test.items() == successful.items()
    assert not test.items() == failure.items()

def test_cockroach_params():

    test = config.CockroachParams(user="Ian", passwd="Test", host="test", database="test", sslmode="disable")
    successful = {"user": "Ian", "passwd": "Test", "host": "test", "database": "test", "sslmode": "disable"}
    failure = {}

    assert test.items() == successful.items()
    assert not test.items() == failure.items()

def test_tulpar_config():

    config_test = config.TulparConfig("Test", ("sqlite", config.SQLiteParams(filename="test.db", create_db=True)), middleware=[])
    
    assert config_test.app_name == "Test"
    assert isinstance(config_test.db_params[1], dict)
    assert config_test.db_params[0] == "sqlite"
