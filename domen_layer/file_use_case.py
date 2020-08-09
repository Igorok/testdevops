from service_layer.file_manager import FileManager
from entities.file_info import FileInfo

class FileUseCase:
    def __init__(self, fileManager: FileManager):
        '''Set manager for files on init'''
        pass

    def clearDir(self, dirname: str, fileTime: float, size: int) -> [FileInfo]:
        '''Clear directory'''
        pass