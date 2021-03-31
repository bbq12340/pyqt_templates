from PySide2.QtCore import QThread, QObject, Signal
import time
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from scraper import start_driver, search_coupang


class Worker(QObject):
    finished = Signal()
    progress = Signal(float)

    def __init__(self, query_list, delay):
        super().__init__()
        self.query_list = query_list
        self.delay = float(delay)

    def run(self):
        browser = start_driver()
        wait = WebDriverWait(browser, 10)
        result = []
        for query in self.query_list:
            data = search_coupang(browser, wait, query)
            result.append(data)
            self.progress.emit(
                ((self.query_list.index(query)+1)/len(self.query_list)*100))
            time.sleep(self.delay)
        browser.quit()
        df = pd.DataFrame(result)
        df.to_csv(f"result/{self.query_list[0]}.csv",
                  encoding="utf-8-sig", index=False)
        self.finished.emit()
