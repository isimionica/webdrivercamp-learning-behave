from behave import *
from selenium import webdriver
from behave_basics.components.gift_page import *

@step('launch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

@step('Navigate to {url}')
def step_impl(context, url):
    context.browser.get("https://www.target.com/")

@step('Search for {search_item}')
def step_impl(context, search_item):
    context.driver.find_element_by_xpath("//input[@name='searchTerm']")

@step('Verify searched page contains {search_item} ')
def step_impl(context, search_item):
    context.drive.find.header_xpath = "//h1"

@step("Select {option} in {section} section")
def step_impl(context, option, section):
    context.gift_page = GiftPage(context.browser)
    context.gift_page.select_option(option, section)

@step('Collect all items on the first page into {context_var}')
def step_impl(context, context_var):
    items = context.gift_page.collect_item_features()
    if level is not None:
        setattr(context.feature, var, items)
    # assigns the result to the context variable
    else:
        setattr(context, var, items)
