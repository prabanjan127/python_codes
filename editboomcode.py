import art, time, os, platform
from colorama import init, Fore
from termcolor import colored
import pandas as pd
import subprocess
import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


FILE_LOC = r"C:\Users\DELL\Desktop\data.xlsx"
SRNO = 'SRNO'
NAME = 'Name'
PHONENUMBER = 'Phone Number'
MESSAGE = 'Message'
IMAGE = 'Image'
REPLACENAME = '{{name}}'
URL = 'https://web.whatsapp.com/'
WAITER_ELEMENT = "landing-title _3-XoE"
PHONE_NUMER_INPUT = "//*[@id='side']/div[1]/div/label/div/div[2]"
PERSON_DIV = "//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[1]/div/div/img"
MESSAGE_INPUT = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]"
IMAGE_INPUT = "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"
SEND_BUTTON = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button"
driver = webdriver.Chrome(executable_path='E:\\chromedriver_win32 (1)\chromedriver.exe')
waiter = WebDriverWait(driver, 10)
data = []
Date = datetime.datetime(int(2022), int(1), 1)
def printData(message,type):
    if type == 'INFO':
        print('[' + colored(datetime.datetime.now().strftime('%H:%M:%S'), 'cyan') + '][' + colored('INFO', 'green') +  '] ' +  message)
    elif type == 'WARNING':
        print('[' + colored(datetime.datetime.now().strftime('%H:%M:%S'), 'cyan') + '][' + colored('WARNING', 'yellow') +  '] ' + message)
    elif type == 'ERROR':
        print('[' + colored(datetime.datetime.now().strftime('%H:%M:%S'), 'cyan') + '][' + colored('ERROR', 'red') +  '] ' + message)

def read_data_from_excel():
    try:
        df = pd.DataFrame()
        df = pd.read_excel(FILE_LOC)
        printData("Retrieving data from excel", 'INFO')
    except:
        printData("Excel 'data.xlsx' not found", 'ERROR')
        printData("Found {0} messages to be send".format(len(df.index)), 'INFO')
    for i in df.index:
        if '+' not in str(df[PHONENUMBER][i]):
            number = '+91' + str(df[PHONENUMBER][i])
        else:
            number = str(df[PHONENUMBER][i])
        output = {
            'SrNo': df[SRNO][i],
            'Name': df[NAME][i],
            'PhoneNumber': number,
            'Message': df[MESSAGE][i],
            'Image':df[IMAGE][i],
        }
        data.append(output)

def send_whatsapp_message():
    global driver
    driver.get(URL)
    printData("Loading site...", 'INFO')
    waiter.until(EC.title_is("WhatsApp"))
    printData("Site loaded successfully...", 'INFO')
    printData("Waiting for user to log in using WhatsApp Web", 'INFO')
    waitCounter = 0
    while 1:
        try:
            waiter.until(EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))
            waitCounter+=1
            if waitCounter%1000 == 0:
                printData("Waiting for user to log in...", 'WARNING')
        except:
            printData("Logged in to WhatsApp", 'INFO')
            break

def send_whatsapp_image():
    global driver
    driver.get(URL)
    printData("loading site...",'INFO')
    waiter.until(EC.title_is("whatsapp"))
    printData("site loaded successfully..",'INFO')
    waitCounter =0
    while 1:
        try:
            waiter.until(EC.presence_of_element_located((By.XPATH, "//div[@title='Attach']")))
            waitCounter+=1
            if waitCounter%1000 ==0:
                printData("wating for the user to log in...",'WARNING')
        except:
                printData("logged in to whatsapp",'INF0')
                break
                 
    for entry in data:
        driver.find_element_by_xpath(PHONE_NUMER_INPUT).send_keys(str(entry['PhoneNumber']))
        time.sleep(5)
        driver.find_element_by_xpath(PHONE_NUMER_INPUT).send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(MESSAGE_INPUT).send_keys(str(entry['Message']))
        time.sleep(5)
        driver.find_element_by_xpath(IMAGE_INPUT).send_keys(str['Image'])
        time.sleep(5)
        driver.find_element_by_xpath(IMAGE_INPUT).send_keys(os.getcwd().ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(SEND_BUTTON).click()
        time.sleep(5)
        printData("Successfully send message to {0}, name: {1}".format(str(entry['PhoneNumber']), str(entry['Name'])), 'INFO')

if __name__ == '__main__':
    # Initialize colorama
    init()

    # Clear the screen
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    # Display ASCII art
    print(art.text2art("Boom Messenger"))
    print(Fore.CYAN + "\nCreated By:" + Fore.RESET + " Arunkumar[All About Python]\n")
    print(Fore.YELLOW + "GitHub: " + Fore.RESET + "   Arunkumar")



    # Read data from 'data.xlsx' file
    read_data_from_excel()

    # Send whatsapp message 
    send_whatsapp_message()

    # send whatsapp image
    IMAGE_INPUT.send_keys (FILE_LOC)
    
    
    # Close chromedriver
    driver.close()
    
