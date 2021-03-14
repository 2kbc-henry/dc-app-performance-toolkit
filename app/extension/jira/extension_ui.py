import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['project_key']:
        project_key = datasets['project_key']

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_issue")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{project_key}?selectedItem=linkboard:linkboard-page")
            page.wait_until_visible((By.ID, "lb-root"))  # Wait for summary field visible
            page.wait_until_visible((By.CSS_SELECTOR, "#lb-root .ijnXzl"))  # Wait for summary field visible
        sub_measure()
    measure()
