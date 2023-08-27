from selenium import webdriver
from time import sleep
driver=webdriver.Chrome (r'E:\\chromedriver_win32 (1)\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name=input("Enter name of user or group:")
filepath=input ("Enter your Filepath:")
input("Enter anything after scanning QR code")
user = driver.find_element('//span[@title = "{}"]'.format(name))
user.click()
attachment_box=driver.find_element('//div[@title="Attach"]')
attachment_box.click()
image_box=driver.find_element('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys (filepath)
send_button=driver.find_element("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")      
send_button.click()
sleep (3)
