import pytest
import time
from service_layer.os_manager_mock import OsManagerMock
from domen_layer.os_use_case import OsUseCase

class TestOsUseCase:
    DIRNAME='/Users/user/Documents'

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def testReadDir(self):
        fileManager = OsManagerMock()
        osUseCase = OsUseCase(fileManager)

        fileList = fileManager.readDir(self.DIRNAME)

        dayAgo = time.time() - 24 * 60 * 60
        removed = osUseCase.clearDir(self.DIRNAME, dayAgo, 1000)

        print('    > Test for logic of removing, all - {0} removed - {1}'.format(*[len( fileList), len(removed)]))

        assert(len(fileList) == 15)
        assert(len(removed) == 5)