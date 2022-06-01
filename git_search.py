###############################################################
# Copyright 2022 AnshumanDas. All Rights Reserved.
#
###############################################################
"""
    Script Name : git_search.py
    Description : Navigates to Git Home page and search the page on given search criteria. Display the details
                  first 5 results.
    Author : Anshuman Das
"""
__author__ = "anshuman.das"
__version__ = "1.0v"

import json
import os.path
from argparse import ArgumentParser
from datetime import datetime

from products.base_class import Base_Class
from page_objects.home_page import HomePage
from lib.util import *

LOG = logging.getLogger(__name__)


class GitSearch(Base_Class):

    def __init__(self, url, browser_type):
        super().__init__()
        self.url = url
        self.browser_type = browser_type

    def get_git_search_result(self, search_text):
        """
        Navigate the git home page and search the given text.
        :param search_text: text to be searched
        :return: search_result list containing details in json format
        """

        def get_info(elements):
            """
            Check the element is found or not, if found then return the text
            :param elements: page elements
            :return:
            """
            if len(elements) == 0:
                return "N/A"
            elif len(elements) == 1:
                return elements[0].text
            elif len(elements) > 1:
                result = []
                for ele in elements:
                    result.append(ele.text)
                return result

        self.initialize(self.url, self.browser_type)

        git_home = HomePage(self.driver)
        git_result = git_home.get_search_result(search_text)
        no_of_repos = int(git_result.get_results_count().text.split(" ")[0].replace(",", ""))
        if no_of_repos == 0:
            LOG.info(f"No result found based on your search criteria, refine your search criteria")
            LOG.info("Exiting the process")
            sys.exit(1)
        LOG.info(f"No. of results are found: {no_of_repos}")
        repo_list = git_result.get_repo_list()

        if no_of_repos > 5:
            max_search_result = 5
        else:
            max_search_result = no_of_repos

        search_result = []
        LOG.info(f"Get the details of first {max_search_result} searched repositories.")
        for i in range(0, max_search_result):
            repo_details = {}
            LOG.info(f"Getting details of {i} searched repository.")
            repo_details["No"] = i
            repo_details["repo_title"] = git_result.get_repo_title(repo_list[i]).text
            repo_details['repo_desc'] = get_info(git_result.get_repo_desc(repo_list[i]))
            repo_details['repo_tags'] = get_info(git_result.get_repo_tags(repo_list[i]))
            repo_details['repo_stars'] = get_info(git_result.get_repo_stars(repo_list[i]))
            repo_details['repo_lang'] = get_info(git_result.get_repo_lang(repo_list[i]))
            repo_details['repo_license'] = get_info(git_result.get_repo_license(repo_list[i]))
            repo_details['repo_last_updated_time'] = get_info(git_result.get_repo_updated_time(repo_list[i]))
            LOG.debug(repo_details)
            search_result.append(repo_details)

        self.close_browser()
        return search_result


def parse_args():
    """
    Define the command line arguments
    :return: command line arguments
    """
    parser = ArgumentParser()

    parser.add_argument("--browser_type", action='store', dest='browser_type', required=False,
                        choices=["chrome"], default="chrome", type=str.lower, help="Decide the browser initialize process",
                        metavar="browser_type")

    args = vars(parser.parse_args())

    return args

def main(args):
    """
    Operation function
    :param args: command line arguments
    :return:
    """
    try:
        LOG.info("Starting git search process")
        browser_type = args.get("browser_type")
        git_search = GitSearch(config.GIT_URL, browser_type)
        search_result = git_search.get_git_search_result("Security")

        timestamp = datetime.now().strftime("%d%H%M%S")
        com_util = Common_Util()
        com_util.create_directory("results")
        result_file = os.path.join("results", f"git_search_resutl_{timestamp}.json")
        with open(result_file, "w") as file:
            json.dump(search_result, file, indent=4)
        LOG.info(f"The result file: {result_file}")
        LOG.info("Completed git search process")
    except Exception as err:
        LOG.exception(f"Exception occurred while git search process: {err}")
        LOG.info("Exiting the process")
        sys.exit(1)


if __name__ == '__main__':
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        handlers=[
            logging.FileHandler(f"./logs/git_search_process.log"),
            logging.StreamHandler(sys.stdout)
        ])
    main(args)

