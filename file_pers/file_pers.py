import core.globals
import core.persistence
import sys
import time


sys.path.append(sys.path[0] + './/persistence//file_pers//lib')
# import your Library, here are no libraries needed

persistence_description =    'Persistence Object for persisting to a ordinary text file'
persistence_version =        '0.01'
persistence_author =         'Christian Kueken, Germany'
persistence_library =        'none'

persistence_parameters = {'interval':       'Interval time. How often (in seconds) will a value be persisted.',
                         'persistOnChange': 'Shall the value be persited on every change?',
                         'file':            'Path to the filename where the data will be stored'}


class File_pers(core.persistence.Persistence):

    def __init__(self, name, friendly_name, interval=None, persistOnChange=True, file=None):

        super().__init__(name, friendly_name, interval, persistOnChange)
        self.file = file
        self.status = 'stopped'                             # Set status to stopped. Indicate the start() method that init is complete.


    def user_persist(self, dp_obj):

        try:
            f = open(self.file,'a', encoding='utf8')
            f.write(core.globals.pool['conf']['timestamp'] + '|' + dp_obj.name + '|' + str(dp_obj.value) + '|' + str(dp_obj.unit) + '|' + str(dp_obj.raw) + '\n')
            f.close()

        except OSError as err:
            errno, strerror = err.args
            core.globals.bus.emit('log_error', 'Error while accessing file < ' + self.file + '> Error: ' + strerror , threads=True)


    def getData(self, startTimestamp=None, endTimestamp=None, timeDelta=None, datapointname=None):
        # Manage to et historical data back

        # return three lists timestanmp, value, raw or numpy timeseries
        pass



