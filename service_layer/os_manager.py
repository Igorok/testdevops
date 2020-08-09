import os
from pathlib import Path
from entities.file_info import FileInfo
from service_layer.file_manager import FileManager

class OsManager (FileManager):
    def readDir(self, folderPath: str) -> [FileInfo]:
        folderInfo = []
        for root, dirs, files in os.walk(folderPath):
            for f in files:
                path = Path('{0}/{1}'.format(root, f))
                info = path.stat()
                folderInfo.append(FileInfo(path, info.st_birthtime, info.st_size))

        return folderInfo

    def removeFile(self, filePath: str):
        os.remove(filePath)