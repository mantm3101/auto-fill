import platform
import random
import time
import rtime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import LOOP_TIME
import comment
import customer

PATH = ""
if platform.system() == 'Windows':
    PATH = './chromedriver_win32/chromedriver.exe'
else:
    PATH = './chromedriver_linux64/chromedriver'

SLEEP_SECONDS = 10
DRIVER = webdriver.Chrome(PATH)
WAIT = WebDriverWait(DRIVER, SLEEP_SECONDS)


def main():
    for x in range(LOOP_TIME):
        print("----------Loop time {}------".format(x+1))
        DRIVER.get("https://fb.highlandscoffee.com.vn/")
        step1()
        step2()
        step3()
        step4()
        step5()
        step6()
        step7()
        step8()
        step9()
        step10()
        step11()


def step1():
    # 1/ Enter code
    try:
        print("-----------step1-----------")
        code_input = DRIVER.find_element_by_id('code')
        code_input.send_keys('2263257')
        code_input.send_keys(Keys.RETURN)
    except:
        print("step1 error, retry step1")
        step1()


def step2():
    # 2/ Next
    try:
        print("-----------step2-----------")
        time.sleep(SLEEP_SECONDS)
        fmSurveyBtn = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#fm_survey button")))
        fmSurveyBtn.send_keys(Keys.ENTER)
    except:
        print("step2 error, retry step2")
        step2()


def step3():
    # 3/ Fill customer form
    try:
        print("-----------step3-----------")
        time.sleep(SLEEP_SECONDS)
        txtName = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".form-control.text")))
        txtName.clear()
        customer_name = customer.random_customer()
        print("--Customer name: {}--".format(customer_name))
        txtName.send_keys(customer_name)
        txtDatetime = DRIVER.find_element_by_css_selector(
            ".form-control.date_time")

        r_datetime = rtime.random_time()
        print("----Date: {}------".format(r_datetime))
        txtDatetime.clear()
        txtDatetime.send_keys(r_datetime)
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step3 error, retry step3")
        step3()


def step4():
    # 4/ Choose food
    try:
        print("-----------step4-----------")
        available_food = (0, 1, 2, 3, 7, 8, 9, 10, 11, 12, 14)
        selected_food_idx = random.choice(available_food)
        time.sleep(SLEEP_SECONDS)
        food = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#fm_survey .__item")))
        foods = DRIVER.find_elements_by_css_selector('#fm_survey .__item')
        foods[selected_food_idx].click()
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step4 error, retry step4")
        step4()


def step5():
    # 5/ Rate 7*
    try:
        print("-----------step5-----------")
        time.sleep(SLEEP_SECONDS)
        rate = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#question_data .card")))
        rate.click()
        time.sleep(1)
        points = rate.find_elements_by_css_selector(".__item")[6].click()
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step5 error, retry step5")
        step5()


def step6():
    # 6/ Rate
    try:
        print("-----------step6-----------")
        time.sleep(SLEEP_SECONDS)
        rate = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#question_data .card")))
        rates = DRIVER.find_elements_by_css_selector("#question_data .card")
        for r in rates:
            r.click()
            time.sleep(1)
            point = r.find_elements_by_css_selector(".__item")[6].click()
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step6 error, retry step6")
        step6()


def step7():
    # 7/ Rate
    try:
        print("-----------step7-----------")
        time.sleep(SLEEP_SECONDS)
        rate = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#question_data .card")))
        rates = DRIVER.find_elements_by_css_selector("#question_data .card")
        for r in rates:
            r.click()
            time.sleep(1)
            point = r.find_elements_by_css_selector(".__item")[6].click()
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step7 error, retry step7")
        step7()


def step8():
    # 8/ Rate
    try:
        print("-----------step8-----------")
        time.sleep(SLEEP_SECONDS)
        rate = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#question_data .card")))
        rates = DRIVER.find_elements_by_css_selector("#question_data .card")
        for r in rates:
            r.click()
            time.sleep(1)
            point = r.find_elements_by_css_selector(".__item")[6].click()
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step8 error, retry step8")
        step8()


def step9():
    # 9/
    try:
        print("-----------step9-----------")
        time.sleep(SLEEP_SECONDS)
        question_card = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".__question")))
        question_card.find_elements_by_css_selector(".__item")[10].click()
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step9 error, retry step9")
        step9()


def step10():
    # 10 /
    try:
        print("-----------step10-----------")
        time.sleep(SLEEP_SECONDS)
        answer_box = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".form-control.text")))
        answer_box.clear()
        answer_box.send_keys(comment.random_comment())
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step10 error, retry step10")
        step10()


def step11():
    # 11 /
    try:
        print("-----------step11-----------")
        time.sleep(SLEEP_SECONDS)
        answer_box = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".form-control.text")))
        DRIVER.find_element_by_css_selector("#fm_survey button").click()
    except:
        print("step11 error, retry step11")
        step11()


main()
