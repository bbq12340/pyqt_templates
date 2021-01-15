from PySide6.QtCore import QThread, QObject, Signal

class Worker(QObject):
    finished = Signal()
    progress = Signal(float)

    def run(self):
        """Long-running task."""
        for i in range(100):
            time.sleep(1)
            self.progress.emit(i + 1)
        self.finished.emit()
