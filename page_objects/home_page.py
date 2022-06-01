###############################################################
# Copyright Anshuman_Das. All Rights Reserved.
#
###############################################################
"""
    Script Name : home_page.py
    Description: Page objects for GIT Home page
    Author : Anshuman Das
"""

__author__ = "anshuman.das"
__version__ = "1.0v"

import logging

from page_objects.base_page_objects import BasePageObjects
from page_objects.search_result_page import SearchResultPage
import config

LOG = logging.getLogger(__name__)

class HomePage(BasePageObjects):

    def __init__(self, driver):
        super().__init__(driver, config.GIT_PAGE_OBJECTS, "GITHomePage")

    def get_search_box(self):
        self.wait_for_element("search_box")
        return self.find_page_element("search_box")

    def get_search_result(self, search_text):
        search_box = self.get_search_box()
        LOG.info(f"Searching the text:{search_text}")
        search_box.send_keys(search_text)
        search_box.submit()
        search_result = SearchResultPage(self.driver)
        LOG.info(f"Looking for search result")
        return search_result
