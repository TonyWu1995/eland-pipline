class SegmentConfig:

    def __init__(self, criteria_key, criteria_value, algo, day):
        self.__criteria_key = criteria_key
        self.__criteria_value = criteria_value
        self.__algo = algo
        self.__day = day

    @property
    def criteria_key(self):
        return self.__criteria_key

    @property
    def criteria_value(self):
        return self.__criteria_value

    @property
    def algo(self):
        return self.__algo

    @property
    def day(self):
        return self.__day

    @staticmethod
    def build(config: dict):
        return SegmentConfig(config['criteria_key'], config['criteria_value'], config['algo'], config['day'])

    @staticmethod
    def build_list(config_list: list):
        return [SegmentConfig.build(config) for config in config_list]
