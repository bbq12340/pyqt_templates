from PySide2.QtCore import QThread, QObject, Signal
import time


class Worker(QObject):
    finished = Signal()
    progress = Signal(float)

    def __init__(self, query_list, delay):
        super().__init__()
        self.query_list = query_list
        self.delay = float(delay)

    def run(self):
        for query in self.query_list:
            """
                do something fancy
                like scraping somthing by query
            """
            self.progress.emit(
                ((self.query_list.index(query)+1)/len(self.query_list)*100))
            time.sleep(self.delay)
        self.finished.emit()
