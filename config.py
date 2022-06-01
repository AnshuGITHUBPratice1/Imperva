import os

BASE_DIR = os.path.abspath(os.getcwd())
SUPPORTED_SYSTEMS = ['windows', 'centos']
GIT_PAGE_OBJECTS = os.path.join(BASE_DIR, "resources", "page_objects.yaml")
LINUX_PASSWORD = ""

CHROMEDRIVER_WIN = os.path.join(BASE_DIR, "drivers", "chromedriver_win.exe")
CHROMEDRIVER_UNIX = os.path.join(BASE_DIR, "drivers", "chromedriver_unix")
GIT_URL = "https://github.com/"

