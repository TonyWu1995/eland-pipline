import csv
import logging
from datetime import datetime

from config.file_config import FileConfig

log = logging.getLogger(__name__)

class ExportSegmentService:

    def __init__(self, file_config: FileConfig):
        self.__folder_path = file_config.save_segment_folder_path

    def save(self, file_name, ctid_list):
        log.info("save() file_name={} ctid_list={}".format(file_name, ctid_list))
        time_str = datetime.now().strftime("%Y%m%d")
        self.__save_csv(self.__folder_path + file_name.format(time_str, len(ctid_list)), [[ctid] for ctid in ctid_list])

    def __save_csv(self, file_path, data_list):
        try:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in data_list:
                    writer.writerow(row)
        except Exception as e:
            raise Exception(e)
