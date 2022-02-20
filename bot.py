import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://play.typeracer.com/")


try:
    text_list = []
    
    time.sleep(10)
    print("over")
    driver.implicitly_wait(10)

    #practice_button_click = driver.find_element_by_class_name("bkgnd-green")
    #practice_button_click.click()

    driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL + Keys.ALT + "I")

    table = driver.find_element_by_class_name("gameView")
    spans = table.find_elements_by_tag_name("span")
    for span in spans:
        text = span.get_attribute("innerText")
        if "(you)" in text or ":0" in text:
            continue
        else:
            text_list.append(text)

    print(text_list)
    time.sleep(14)

    #text_to_type = str(text_list[0])+str(text_list[1])+str(text_list[2])
    text_to_type = ""
    for i in range(0, len(text_list)):
        text_to_type = text_to_type + text_list[i]

    print(text_to_type)
    textbox = table.find_element_by_class_name("txtInput")
    for letter in text_to_type:
        time.sleep(0.01)
        textbox.send_keys(letter)

    test = input(": ")
    if test == "1":
        driver.quit()
    else:
        raise NameError
finally:
    driver.quit()

input("Press any key to quit: ")
driver.quit()
