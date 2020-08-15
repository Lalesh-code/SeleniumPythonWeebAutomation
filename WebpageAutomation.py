from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\Lalesh_Python\Drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407%22")
driver.find_element_by_id("RESULT_TextField-1").send_keys("Aatmaja")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Garud")
driver.find_element_by_id("RESULT_TextField-3").send_keys("9967554433")
driver.find_element_by_id("RESULT_TextField-4").send_keys("India")
driver.find_element_by_id("RESULT_TextField-5").send_keys("Pune")
driver.find_element_by_id("RESULT_TextField-6").send_keys("LG@gmail.com")

# status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
# print(status)
# status=driver.find_element_by_id("RESULT_RadioButton-7_0").click()
# print(status)

status=driver.find_element_by_xpath("//label[contains(text(),'Male')]").is_selected()
print(status)

driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
driver.implicitly_wait(5)
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

status=driver.find_element_by_xpath("//label[contains(text(),'Sunday')]").is_selected()
print(status)
driver.find_element_by_xpath("//label[contains(text(),'Sunday')]").click()
driver.implicitly_wait(5)
status=driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)

status=driver.find_element_by_xpath("//label[contains(text(),'Saturday')]").is_selected()
print(status)
driver.find_element_by_xpath("//label[contains(text(),'Saturday')]").click()
driver.implicitly_wait(5)
status=driver.find_element_by_id("RESULT_CheckBox-8_6").is_selected()
print(status)

driver.implicitly_wait(10)
drp=Select(driver.find_element_by_id("RESULT_RadioButton-9"))
drp.select_by_visible_text('Morning')
drp.select_by_index(2)
drp.select_by_value("Radio-2")

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("E://SeleniumDemo/myfile.txt")
driver.implicitly_wait(10)

#testing_link = driver.find_element_by_link_text('Software Testing Tutorials')
driver.find_element_by_xpath("//a[contains(text(),'Software Testing Tutorials')]").click()
#testing_link.click()

#driver.find_element_by_id("FSsubmit").click()

driver.close()