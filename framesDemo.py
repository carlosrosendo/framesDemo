from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch to frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce" ).clear()
driver.find_element(By.ID, "tinymce" ).send_keys("I am able to automate frames")

#switch back
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
