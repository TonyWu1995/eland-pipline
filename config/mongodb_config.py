class MongoDBConfig:

    def __init__(self, host, port, database, username, password, collection_name):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__username = username
        self.__password = password
        self.__collection_name = collection_name

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

    @property
    def collection_name(self):
        return self.__collection_name

    @staticmethod
    def build(config: dict):
        return MongoDBConfig(config['host'],
                             config['port'],
                             config['database'],
                             config['username'],
                             config['password'],
                             config['collection-name'])
