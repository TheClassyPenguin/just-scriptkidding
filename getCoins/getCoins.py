from selenium import webdriver
import subprocess
from selenium.webdriver.common.keys import Keys
if __name__ == "__main__":

    driver = webdriver.PhantomJS()
    driver.get("https://www.chrono.gg/")

    elem = driver.find_element_by_class_name("container_coin")
    elem.click()

    loginBox = driver.find_element_by_id("signin-email")
    loginBox.send_keys("EMAIL HERE")

    passwordBox = driver.find_element_by_id("signin-password")
    passwordBox.send_keys("PASSWORD HERE")
    passwordBox.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.save_screenshot('screen1.png')
    elem = driver.find_element_by_class_name("container_coin")
    elem.click()
    time.sleep(0.5)
    driver.save_screenshot('screen2,png')
    driver.quit()
