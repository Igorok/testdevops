from service_layer.file_manager import FileManager
from entities.file_info import FileInfo

class OsUseCase:
    def __init__(self, fileManager: FileManager):
        self.fileManager = fileManager

    def clearDir(self, path: str, fileTime: float, size: int) -> [FileInfo]:
        fileList = self.fileManager.readDir(path)
        forRemove = list(filter(lambda info: (info.birthtime < fileTime and info.size > size), fileList))

        for f in forRemove:
            self.fileManager.removeFile(f.path)

        return forRemove