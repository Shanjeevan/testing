from behave import *
# to import Webdriver
from selenium import webdriver
# Opening Google Chrome Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

use_step_matcher("re")

driver = webdriver.Chrome(r"C:\Users\MSI\Documents\AutomationTest\Browsers\chromedriver.exe")
@given("Open the Chrome and launch the application")
def step_impl(context):
    # Maximize our browser
    driver.maximize_window()
    # Navigate to "https://www.google.com/"
    driver.get("http://demo.guru99.com/v1/index.php")
    print("Chrome Opened")

@when("Enter the Username and Password")
def step_impl(context):
    # enter username in the field
    driver.find_element_by_name("uid").send_keys("mngr251062")
    # enter password in the field
    driver.find_element_by_name("password").send_keys("negutat")
    print("Usename and password entered")

@step("Click Search Button")
def step_impl(context):
    # Click enter
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/input[1]").send_keys(Keys.ENTER)
    print("Searching")

@then("Go to home page")
def step_impl(context):
    print("Go to home page")

@given("After Login the application")
def step_impl(context):
    print("After Login the application")

@when("Select New Customer")
def step_impl(context):
    # # select New Customer
    driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").send_keys(Keys.ENTER)
    print("Selecting New Customer")

@then("Can See Add customer form")
def step_impl(context):
    print("Can See Add customer form")

@given("showing add customer page")
def step_impl(context):
    print("showing add customer page")

@when("filling the form")
def step_impl(context):
    # enter Customer Name in the field
    driver.find_element_by_name("name").send_keys("Shan")
    # Select Gender
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]").click()
    # Select Date Of Birth
    driver.find_element_by_name("dob").send_keys("01/01/2020")
    # enter Address in the field
    driver.find_element_by_name("addr").send_keys("Srilanka colombo")
    # enter City in the field
    driver.find_element_by_name("city").send_keys("Colombo")
    # enter State in the field
    driver.find_element_by_name("state").send_keys("Colombo")
    # enter PIN in the field
    driver.find_element_by_name("pinno").send_keys("123456")
    # enter Telephone number in the field
    driver.find_element_by_name("telephoneno").send_keys("0773416673")
    # enter Email number in the field
    driver.find_element_by_name("emailid").send_keys("Shanjee1997@gmail.com")
    print("showing add customer page")

@step("Click submit button")
def step_impl(context):
    # Click Submit Button
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[13]/td[2]/input[1]").send_keys(Keys.ENTER)
    print("showing add customer page")

@then("click the submit the button")
def step_impl(context):
    print("showing add customer page")