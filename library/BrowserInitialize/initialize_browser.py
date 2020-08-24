from selenium import webdriver
from robot.errors import RemoteError


class InitializeBrowser():
    def __init__(self):
        project_location=r"C:\Users\Arun\Budget_Project"
        self._options = webdriver.ChromeOptions()
        self._options.add_argument("--start-maximized")
        self._options.add_argument("--disable-plugins")
        self._options.add_argument("--disable-extensions")
        self._chromedriver = r"C:\Users\Arun\Budget_Project\driver\chromedriver.exe"

    def initialize_driver(self,browser_type):
        try:
            if browser_type is "Chrome":
                self.driver = webdriver.Chrome(executable_path= self._chromedriver, chrome_options= self._options)
        except Exception as err:
            raise RemoteError ("Issue in initializung browser",fatal=False, continuable=False)


