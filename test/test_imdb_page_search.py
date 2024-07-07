from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import sys
import os
import time

# Add the parent directory to the path if amazon_login_page.py is in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from page.imdb_main_page import imdb_search_page
# from pages.Admin.HRM_admin_page import AdminPage

@pytest.fixture
def browser():
    chromedriver_path = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    time.sleep(6)
    driver.quit()
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options)
    # driver.maximize_window()

def pytest_configure(config):
    config.option.htmlpath = '/path/to/report.html'

def test_imdb_search(browser):
    imdb_page = imdb_search_page(browser)
    browser.get("https://www.imdb.com/search/name/")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()
    imdb_page.navigate_to_form()
    imdb_page.click_collapse()
    imdb_page.set_Name("vignesh")
    print("Name is entered into text box")
    imdb_page.navigate_to_Birth_date()
    imdb_page.set_date("2020-02","2024-02")
    print("Birth date is entered into text box")
    imdb_page.navigate_to_Birthday()
    imdb_page.set_BD("12-02")
    print("navigate_to_Birthday is entered into text box")
    imdb_page.navigate_to_Awards()
    imdb_page.select_Award()
    print("Selected Award Nomination")
    imdb_page.navigate_to_Page_topics()
    imdb_page.select_page_topic()
    print("Selected page Nomination")
    imdb_page.navigate_to_Trivia()
    imdb_page.select_topic()
    imdb_page.set_dropdown_option("India")
    print("setted India in options text box")
    imdb_page.navigate_to_Gender_identity()
    imdb_page.select_credit("Holiday")
    print("setted Holiday in credit text box")
    imdb_page.navigate_to_Credits()
    imdb_page.select_Adult_name()
    print("selected option in under Adult name")
    imdb_page.See_results()
    print("Search performed successfully.""Test passed")
