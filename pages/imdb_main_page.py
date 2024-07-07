import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.common.keys
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class imdb_search_page:
    Select_Collapse = '//span[text()="Expand all"]'
    scroll_to_Bdate = '//div[text()="Birth date"]'
    DB_startdate = '//input[@name="birth-year-month-start-input"]'
    DB_todate = '//input[@name="birth-year-month-end-input"]'
    scroll_to_Birthday = "//div[text()='Birthday']"
    BD_Input = '//input[@name="birthday-input"]'
    scroll_to_Awards_recognition = "//div[text()='Awards & recognition']"
    Award_select = "//span[text()='Best Director-Nominated']"
    scroll_to_Page_topics = "//div[text()='Page topics']"
    page_topic = "//span[text()='Place of birth']"
    scroll_to_Trivia = "//span[text()='Trivia']"
    topic = '//select[@class="ipc-select__input"]'
    dropdown_option = 'text-input__5'
    scroll_toGender_identity = "//div[text()='Gender identity']"
    credit = '//input[@class="sc-cb8b4fe5-0 hbbOwa react-autosuggest__input"]'
    scroll_to_Credits = "//div[text()='Credits']"
    Adult_name = "include-adult-names"
    result = "//span[text()='See results']"
    scroll_to_form = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[1]/ul/li[1]/span"
    name_input = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_form(self):
        scroll_to = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_form)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
        self.driver.implicitly_wait(10)

    def click_collapse(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.Select_Collapse))).click()

    def set_Name(self, name):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.name_input))).send_keys(name)

    def navigate_to_Birth_date(self):
        scroll_to1 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_Bdate)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to1)
        self.driver.implicitly_wait(10)

    def set_date(self, start_date, to_date):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.DB_startdate))).send_keys(start_date)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.DB_startdate))).send_keys(to_date)

    def navigate_to_Birthday(self):
        scroll_to2 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_Birthday)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to2)
        self.driver.implicitly_wait(10)

    def set_BD(self, date):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.BD_Input))).send_keys(date)

    def navigate_to_Awards(self):
        scroll_to3 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_Awards_recognition)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to3)
        self.driver.implicitly_wait(10)

    def select_Award(self):
        Award_select = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.Award_select)))
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(Award_select)
        actions.click(Award_select)
        actions.perform()

    def navigate_to_Page_topics(self):
        scroll_to4 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_Page_topics)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to4)
        self.driver.implicitly_wait(10)

    def select_page_topic(self):
        page_topic = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.page_topic)))
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(page_topic)
        actions.click(page_topic)
        actions.perform()

    def navigate_to_Trivia(self):
        scroll_to5 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_Trivia)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to5)
        self.driver.implicitly_wait(10)

    def select_topic(self):
        topic = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.topic)))
        dropdown = Select(topic)
        dropdown.select_by_index(2)

    def set_dropdown_option(self, option):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_option))).send_keys("India")


    def navigate_to_Gender_identity(self):
        scroll_to6 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_toGender_identity)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to6)
        self.driver.implicitly_wait(10)

    def select_credit(self,credit):
        actions = ActionChains(self.driver)  # initialize ActionChain object
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.credit))).send_keys(credit)
        actions.pause(2)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.pause(1)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def navigate_to_Credits(self):
        scroll_to7 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.scroll_to_Credits)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to7)
        self.driver.implicitly_wait(10)


    def select_Adult_name(self):
        actions = ActionChains(self.driver)
        Adult_name = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, self.Adult_name)))
        actions.move_to_element(Adult_name)
        actions.click(Adult_name)
        actions.perform()

    def See_results(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.result))).click()