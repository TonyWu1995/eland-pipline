class MongoDBConfig:

    def __init__(self, host, port, database, username, password):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__username = username
        self.__password = password

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def database(self):
        return self.__database

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @staticmethod
    def build(config: dict):
        return MongoDBConfig(config['host'], config['port'], config['database'], config['username'], config['password'])
