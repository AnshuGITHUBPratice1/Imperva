# Anshuman Imperva Git Search

### Prerequisite
- install python3
- Install python packages (pip install -r requirements.txt)
- Need to have Chrome browser installed

### Note
- The script is designed to run with windows and chrome browser, for any other system and browser it won't work.
- You may find some code related to Unix (centos) machine but it is not tested so not sure whether it will work or not

- It should work for any versions of chrome. Below code indicates that
```
  chromedriver_autoinstaller.install()
  self.driver = webdriver.Chrome(options=chrome_options)
```
- If you want to run with specific chrome browser, download corresponding selenium driver from "https://chromedriver.chromium.org/downloads"
- Place it under drivers folder and in config.py update "CHROMEDRIVER_WIN" path and uncomment below codes in products/base_class.py. Comment the above autoinstller code.
```
  executable_path = config.CHROMEDRIVER_WIN
  self.driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
 ```
### Setup and Installation
1. Clone the repository
```
   git clone https://github.com/AnshuGITHUBPratice1/Imperva.git
```
2. To run the script
```
    python git_search.py --browser_type chrome
    or
    python git_search.py (default browser is set as chrome)
```
