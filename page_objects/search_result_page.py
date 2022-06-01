###############################################################
# Copyright Anshuman_Das. All Rights Reserved.
#
###############################################################
"""
    Script Name : search_result_page.py
    Description: Page objects for GIT Search Result page
    Author : Anshuman Das
"""

__author__ = "anshuman.das"
__version__ = "1.0v"

import logging

from page_objects.base_page_objects import BasePageObjects
import config

LOG = logging.getLogger(__name__)

class SearchResultPage(BasePageObjects):

    def __init__(self, driver):
        super().__init__(driver, config.GIT_PAGE_OBJECTS, "SearchResultPage")

    def get_results_count(self):
        return self.find_page_element("no_of_results")

    def get_repo_list(self):
        return self.find_page_elements("repo_list")

    def get_repo_title(self, parent_ele):
        return self.find_page_element("repo_title", parent_ele)

    def get_repo_desc(self, parent_ele):
        return self.find_page_elements("repo_desc", parent_ele)

    def get_repo_tags(self, parent_ele):
        return self.find_page_elements("repo_tags", parent_ele)

    def get_repo_stars(self, parent_ele):
        return self.find_page_elements("repo_stars", parent_ele)

    def get_repo_lang(self, parent_ele):
        return self.find_page_elements("repo_lang", parent_ele)

    def get_repo_license(self, parent_ele):
        return self.find_page_elements("repo_license", parent_ele)

    def get_repo_updated_time(self, parent_ele):
        return self.find_page_elements("repo_updated_time", parent_ele)
