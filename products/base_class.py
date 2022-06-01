###############################################################
# Copyright Anshuman_Das. All Rights Reserved.
#
###############################################################
"""
    Script Name : base_class.py
    Description: Initialize the browser and close the session
    Author : Anshuman Das
"""
__author__ = "anshuman.das"
__version__ = "1.0v"

import sys

from selenium import webdriver
import chromedriver_autoinstaller
import logging

import config
from lib.util import Common_Util as com_util

LOG = logging.getLogger(__name__)

class Base_Class(object):

    def __init__(self):
        self.driver = None
        self.system = com_util.get_system_os()

    def initialize(self, url, browser_type):
        """
        Initalize the browser session and browse the url
        :param url: url of site
        :param browser_type: chrome of firefox
        :return:
        """
        try:
            self.launch_browser(browser_type)
            self.get_Url(url)
        except Exception as exp:
            LOG.info(f"Exception occurred: {exp}")
            sys.exit(0)

    def launch_browser(self, browser_type):
        """
        Initialize the browser seesion
        :param browser_type: chrome or firefox
        :return:
        """
        executable_path = None
        if browser_type.lower() == "chrome":
            LOG.info("Chrome browser is selected")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--no-sandbox')
            if self.system.lower() == "centos":
                chrome_options.add_argument('--headless')
                executable_path = config.CHROMEDRIVER_UNIX
            elif self.system.lower() == "windows":
                LOG.info("Initializing the chrome driver")
                chromedriver_autoinstaller.install()
                self.driver = webdriver.Chrome(options=chrome_options)
                # executable_path = config.CHROMEDRIVER_WIN
            # self.driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)

    def get_Url(self, url):
        """
        Browse the given url
        :param url: url of site to be browsed
        :return:
        """
        LOG.info(f'Browsing the url {url}')
        self.driver.get(url)
        if self.system.lower() == "windows":
            LOG.info(f"Maximizing the window")
            self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def close_browser(self):
        """
        Will close all browser session
        :return:
        """
        LOG.info("Closing all browser session")
        self.driver.quit()