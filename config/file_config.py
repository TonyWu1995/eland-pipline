from typing import (
    Any,
    Dict
)


class FileConfig:

    def __init__(self, save_segment_folder_path: str) -> None:
        self.__save_segment_folder_path = save_segment_folder_path

    @property
    def save_segment_folder_path(self) -> str:
        return self.__save_segment_folder_path

    @staticmethod
    def build(config: Dict[str, Any])-> Any:
        save_segment_folder_path = str(config['save-segment-folder-path'])
        if not save_segment_folder_path.endswith("/"):
            save_segment_folder_path = save_segment_folder_path + "/"
        return FileConfig(save_segment_folder_path)
