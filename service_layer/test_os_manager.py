import pytest
import os
from shutil import rmtree
from service_layer.os_manager import OsManager

class TestOsManager:
    DIRNAME = 'dir_0'
    DEEP = 3

    def setup(self):
        print('setup')
        self.generateDir(self.DEEP)
        self.generateFiles(self.DEEP)

    def teardown(self):
        print('teardown')
        rmtree(self.DIRNAME)

    @pytest.mark.run(order=1)
    def testReadDir(self):
        om = OsManager()
        filelist = om.readDir(self.DIRNAME)

        print('    > Test for reading from test directory {0} from {1}'.format(*[len( filelist), self.DEEP * 2]))
        assert(len( filelist) == self.DEEP * 2)

    @pytest.mark.run(order=2)
    def testRemoveFile(self):
        om = OsManager()
        filelist = om.readDir(self.DIRNAME)

        for i in range(len(filelist)):
            if i%2 == 0:
                om.removeFile(filelist[i].path)

        filelist = om.readDir(self.DIRNAME)

        print('    > Test for removing half of files {0} from {1}'.format(*[len( filelist), self.DEEP]))
        assert(len( filelist) == self.DEEP)

    def generateDir(self, deep):
        dirPath = ''
        for i in range(deep):
            if i != 0:
                dirPath += '/'

            dirPath += 'dir_' + str(i)

        os.makedirs(dirPath)

    def generateFiles(self, deep):
        filePath = ''

        for i in range(deep):
            iStr = str(i)
            if i != 0:
                filePath += '/'

            filePath += 'dir_' + iStr

            fileName = 'file_small_' + iStr + '.txt'
            with open(os.path.join(filePath, fileName), 'w') as temp_file:
                temp_file.write('Some text  ' + iStr)

            fileName = 'file_big_' + iStr + '.txt'
            with open(os.path.join(filePath, fileName), 'w') as temp_file:
                longStr = 'Some text  ' + iStr + '\n'
                for j in range(1000):
                    longStr += 'Some text  ' + str(j) + '\n'

                temp_file.write(longStr)