###############################################################
# Copyright Anshuman_Das. All Rights Reserved.
#
###############################################################
"""
    Script Name : base_page_objects.py
    Description: Get the elements of given browser
    Author : Anshuman Das
"""

__author__ = "anshuman.das"
__version__ = "1.0v"

import logging
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.util import Common_Util

LOG = logging.getLogger(__name__)

class BasePageObjects(Common_Util):

    def __init__(self, driver, page_object_file, web_page):
        super().__init__()
        self.driver = driver
        self.web_page = web_page
        self.page_object_file = page_object_file

    def get_element(self, driver, locator_type, locator_val):
        """
        Return the single element for given object details
        :param locator_type: Type of the locator (id, name, css, tag, xpath, link, text, partialLinkTest)
        :param locator_val: Value of the given locator type
        :return: Page element on successful identification or None
        """
        element = None
        try:
            element = driver.find_element(by=getattr(By, locator_type.upper()), value=locator_val)
        except Exception as exp:
            LOG.exception(f"{self.web_page}: Element could not be located, Exception Occoured {exp}", exc_info=True)
            sys.exit()

        return element

    def get_elements(self, driver, locator_type, locator_val):
        """
        Return the list of elements for given object details
        :param locator_type: Type of the locator (id, name, css, tag, xpath, link, text, partialLinkTest)
        :param locator_val: Value of the given locator type
        :return: Page element on successful identification or None
        """
        elements = None
        try:
            elements = driver.find_elements(by=getattr(By, locator_type.upper()), value=locator_val)
        except Exception as exp:
            LOG.exception(f"{self.web_page}: Element could not be located, Exception Occoured {exp}", exc_info=True)
            sys.exit()

        return elements

    def find_page_element(self, element_name, parent_ele=None):
        """
        It will help in identifying the the element in given page or of a parent element
        :param element_name: Element name (Should be present on corresponding page object yaml file
        :param parent_ele: Page object (It is required sometimes some object is the part of another object
                                        In those cases, it is required, e.g. WebTable Row containing the columns values)
        :return: single Element
        """
        element = None
        try:
            element_details = self.read_yaml_file(self.page_object_file, self.web_page)[element_name]
            if not element_details:
                LOG.error(f"{self.web_page}: Could not get the element details")
                sys.exit()
            else:
                if not parent_ele:
                    element = self.get_element(self.driver, element_details['locator_type'], element_details['locator_val'])
                else:
                    element = self.get_element(parent_ele, element_details['locator_type'], element_details['locator_val'])
                LOG.debug(f'{self.web_page}: Found the element:{element_name}')
        except Exception as err:
            LOG.exception(f"{self.web_page}: Could not find the given element, exception occoured:\n {err}",
                          exc_info=True)
            sys.exit()
        return element

    def find_page_elements(self, element_name, parent_ele=None):
        """
        It will help in identifying the list of elements in given page or of a parent element
        :param element_name: Element name (Should be present on corresponding page object yaml file
        :param parent_ele: Page object (It is required sometimes some object is the part of another object
                                        In those cases, it is required, e.g. WebTable Row containing the columns values)
        :return: List of Elements
        """
        elements = None
        try:
            element_details = self.read_yaml_file(self.page_object_file, self.web_page)[element_name]
            if not element_details:
                LOG.error(f"{self.web_page}: Could not get the element details")
                sys.exit()
            else:
                if not parent_ele:
                    elements = self.get_elements(self.driver, element_details['locator_type'], element_details['locator_val'])
                else:
                    elements = self.get_elements(parent_ele, element_details['locator_type'], element_details['locator_val'])
                LOG.debug(f'{self.web_page}: Found the element:{element_name}')
        except Exception as err:
            LOG.exception(
                f"{self.web_page}: Could not find the given element {element_name}, exception occoured:\n {err}",
                exc_info=True)
            sys.exit()
        return elements

    def wait_for_element(self, element_name):
        """

        :param element:
        :return:
        """
        element_details = self.read_yaml_file(self.page_object_file, self.web_page)[element_name]
        locator_type = element_details['locator_type'].upper()
        locator_val = element_details['locator_val']
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((getattr(By, locator_type), locator_val)))