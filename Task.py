from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="chromedriver.exe")
url='https://www.demoblaze.com/'
driver.get(url)
login=driver.find_element(By.ID,"login2").click()
sleep(2)
Username=driver.find_element(By.ID,"loginusername")
Username.send_keys("naomi suli")
Password=driver.find_element(By.ID,"loginpassword")
sleep(1)
Password.send_keys("A123456789")

loginbutton=driver.find_element(By.XPATH,"//button[text()='Log in']").click()
sleep(4)
Nexus6=driver.find_element(By.XPATH,"//a[text()='Nexus 6']").click()
sleep(3)
Addtocart=driver.find_element(By.XPATH,"//a[text()='Add to cart']").click()
sleep(1)
driver.switch_to.alert.accept()
Cart=driver.find_element(By.ID,"cartur").click()

sleep(3)
rows=driver.find_elements(By.XPATH,"//tr")
if len(rows)>2:
    print("The number of items in the card greater than 1")
else:
    print("The number of items in the card is 1")
print(rows[1].find_elements(By.XPATH,"//td")[2].get_attribute('innerHTML'))
if rows[1].find_elements(By.XPATH,"//td")[2].get_attribute('innerHTML')=="650":
    print("The price of the selected phone == 650")
else:
    print("The price of the selected phone != 650")
if rows[1].find_elements(By.XPATH,"//td")[1].get_attribute('innerHTML')=="Nexus 6":
    print("The title of the selected phone == “Nexus 6”")
else:
    print("The title of the selected phone != “Nexus 6”")
sleep(5)
driver.close()
