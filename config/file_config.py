class FileConfig:

    def __init__(self, save_segment_folder_path):
        self.__save_segment_folder_path = save_segment_folder_path

    @property
    def save_segment_folder_path(self):
        return self.__save_segment_folder_path

    @staticmethod
    def build(config: dict):
        save_segment_folder_path = str(config['save-segment-folder-path'])
        if not save_segment_folder_path.endswith("/"):
            save_segment_folder_path = save_segment_folder_path + "/"
        return FileConfig(save_segment_folder_path)

