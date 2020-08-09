import time
from entities.file_info import FileInfo
from service_layer.file_manager import FileManager

class OsManagerMock (FileManager):
    def readDir(self, folderPath: str) -> [FileInfo]:
        folderInfo = []
        weekAgo = time.time() - 7 * 24 * 60 * 60
        for i in range(15):
            fileName = folderPath + '/' + str(i)

            if i%3 == 0:
                folderInfo.append(FileInfo(fileName, weekAgo, 10000))
            elif i%2 == 0:
                folderInfo.append(FileInfo(fileName, weekAgo, 10))
            else:
                folderInfo.append(FileInfo(fileName, time.time(), 10))

        return folderInfo

    def removeFile(self, filePath: str):
        pass