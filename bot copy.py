from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://www.typing.com/student/typing-test/1-page")


try:
    text_list = []
    
    #driver.find_element_by_class_name("js-continue-button").click()
    time.sleep(5)

    driver.find_element_by_class_name("js-sound-settings").click()
    overlay = driver.find_element_by_class_name("modal-wrapper")
    time.sleep(1)
    switches = overlay.find_elements_by_class_name("has-switch")
    for switch in switches:
        switch.click()
    time.sleep(1)
    overlay.find_element_by_tag_name("button").click()
    
    mainContent = driver.find_element_by_class_name("screenBasic-lines")
    letters = mainContent.find_elements_by_class_name("letter")
    for letter in letters:
        i = letter.get_attribute("innerText")
        text_list.append(i)

    print(text_list)

    """
    text_to_type = ""
    for i in range(0, len(text_list)):
        text_to_type = text_to_type + text_list[i]
    print(text_to_type)
    """
    inputText = driver.find_element_by_class_name("js-input-box")


    for each in text_list:
        if each == "\xa0":
            inputText.send_keys(Keys.SPACE)
            print(" ")
        else:
            inputText.send_keys(each)
            print(each)

    test = input(": ")
    if test == "1":
        driver.quit()
    else:
        raise NameError

finally:
    driver.quit()
