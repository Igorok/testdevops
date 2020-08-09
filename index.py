import sys
import time
from datetime import date
from dateutil.relativedelta import relativedelta
from service_layer.os_manager import OsManager
from domen_layer.os_use_case import OsUseCase

def index():
    osManager = OsManager()
    osUseCase = OsUseCase(osManager)

    arguments = sys.argv[1:]
    if (
        len(arguments) != 2 or
        not arguments[1] or
        not arguments[1].isdigit
    ):
        print('Please select correct directory and size')
        return

    folder = arguments[0]
    size = int(arguments[1])

    six_months = date.today() - relativedelta(months=+6)
    six_month_timestamp = time.mktime(six_months.timetuple())

    osUseCase.clearDir(folder, six_month_timestamp, size)

index()