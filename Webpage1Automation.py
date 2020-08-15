from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\Lalesh_Python\Drivers\chromedriver.exe")
driver.maximize_window()

# Pop-up - Ok and Cancel

# driver.get("http://testautomationpractice.blogspot.com/")
# driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
# time.sleep(3)
# #driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()

# Windows frames - iframes - switch t other frames in same window.

# driver.get("https://www.selenium.dev/selenium/docs/api/java/")
# driver.switch_to_frame("packageListFrame")
# link = driver.find_element_by_link_text('org.openqa.selenium')
# link.click()
# time.sleep(3)

# driver.switch_to_default_content()

# driver.switch_to_frame("packageFrame")
# testing1_link = driver.find_element_by_link_text('WebDriver')
# testing1_link.click()
# time.sleep(3)

# driver.switch_to_default_content()

# time.sleep(3)
# driver.switch_to_frame("classFrame")
# driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()

# Window Handling

# driver.get("https://demoqa.com/")
#
# driver.find_element_by_xpath("//img[@class='banner-image']").click()
# print(driver.current_window_handle) #CDwindow-3C21EC9428BA259D52D54FA2021D2F92
# handles=driver.window_handles
#
# for handle in handles:
#     driver.switch_to_window(handle)
#     print(driver.title)
#     if driver.title=="ToolsQA":
#         driver.close()

# Scrolling:

# driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
#
# driver.execute_script("window.scrollBy(1,1000)", "") # pixel
# flag=driver.find_element_by_xpath("//table[1]//tbody[1]//tr[86]//td[1]//img[1]")
# driver.execute_script("arguments[0].scrollIntoView();",flag) # find web page element
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") # end of the page


# Mouse Hover
# driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# driver.find_element_by_id("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
#
# admin=driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
# usermgmt=driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
# users=driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")
# driver.implicitly_wait(5)
#
# actions=ActionChains(driver)
# actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
#
# driver.close()

#Double click

# driver.get("http://testautomationpractice.blogspot.com/")
# element=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")
# actions=ActionChains(driver)
# actions.double_click(element).perform()

#Right click

# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# button=driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
# actions=ActionChains(driver)
# actions.context_click(button).perform()

#Drag & Drop
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# source=driver.find_element_by_xpath("//div[@id='box6']")
# target=driver.find_element_by_xpath("//div[@id='box106']")
# actions=ActionChains(driver)
# actions.drag_and_drop(source,target).perform()

#Upload file
# driver.get("http://testautomationpractice.blogspot.com/")
# driver.switch_to_frame(0)
# driver.find_element_by_id("RESULT_FileUpload-10").send_keys("E://SeleniumDemo/SikuliDemo.png")

#Download File/ Chnage the download file location - ChromeOptions
# driver.get("http://demo.automationtesting.in/FileDownload.html")
# driver.find_element_by_id("textbox").send_keys("Test Demo")
# driver.find_element_by_id("createTxt").click()
# driver.find_element_by_id("link-to-download").click()

# driver.find_element_by_id("pdfbox").send_keys("Test Demo 2")
# driver.find_element_by_id("createPdf").click()
# driver.find_element_by_id("pdf-link-to-download").click()

# Backward - Forward functions:

# driver.get("https://selenium-python.readthedocs.io/")
# print(driver.title)

# driver.get("http://testautomationpractice.blogspot.com/")
# time.sleep(5)
# print(driver.title)

# driver.back()

# time.sleep(5)
# print(driver.title)

# driver.forward()
# time.sleep(5)
# print(driver.title)

# Cookies Demo

# driver.get("https://www.amazon.in/")

# cookies=driver.get_cookies()
# print(len(cookies))
# print(cookies)

# Capture screenshots

# driver.get("https://selenium-python.readthedocs.io/")
# driver.save_screenshot("E:\SeleniumDemo\screenshot\homepage.png")
# driver.get_screenshot_as_file("E:\SeleniumDemo\screenshot\homepage5.jpg")

# Logging Mechanism: actions log file

# import logging

# logging.basicConfig(filename="E://SeleniumDemo//screenshot//test.log",
#                               level=logging.DEBUG)

# logging.debug("This is message debug")
# logging.info("This is message info")
# logging.warning("This is message warning")
# logging.error("This is message error")
# logging.critical("This is message critical")



