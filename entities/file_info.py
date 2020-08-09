class FileInfo():
    '''Entity of file information'''

    def __init__(self, path: str, birthtime: float, size: float):
        self.path = path
        self.birthtime = birthtime
        self.size = size
