from config.config_loader import load_config
from config.mongodb_config import MongoDBConfig
from repo.eland_mongo_repo import ElandDataMongoRepo


def main():
    mongo_repo = ElandDataMongoRepo(MongoDBConfig.build(load_config("./conf/application.yml", "mongodb")))

    pass


if __name__ == '__main__':
    main()
