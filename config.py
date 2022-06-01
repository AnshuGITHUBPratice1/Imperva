import os

BASE_DIR = os.path.abspath(os.getcwd())
SUPPORTED_SYSTEMS = ['windows', 'centos']
LINUX_PASSWORD = ""

# Where all the page objects are defined
GIT_PAGE_OBJECTS = os.path.join(BASE_DIR, "resources", "page_objects.yaml")

# Chromedriver for windows
CHROMEDRIVER_WIN = os.path.join(BASE_DIR, "drivers", "chromedriver_win.exe")
# Chromedriver for unix
CHROMEDRIVER_UNIX = os.path.join(BASE_DIR, "drivers", "chromedriver_unix")

# Test Data
GIT_URL = "https://github.com/"
SEARCH_PATTERN = "Security"
