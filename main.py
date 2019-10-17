import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import bs4 as BeautifulSoup
import time
from getpass import getpass
#bs4&selenium import
#https://www.instagram.com/accounts/login/?source=auth_switcher 

#target Link for Login

#Click <div class="JRHhD">1</div>
#--> it also contains the amount of ppl who want to subscribe
#/html/body/span/section/main/div/div/div/div/div[1]/div[1]/div


#First Login

#username input xpath //*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input
#password input xpath //*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input
#Login Button not needed , just send Enter key after password was inserted

#Navigate to -> https://www.instagram.com/accounts/activity/
#danach auf <div class="JRHhD">1</div> klicken
# --> First Test : Get Subscriber REQUEST amount and display the amount in the terminal



#/html/body/span/section/main/div/div/div[1]/div/div[1]/div[3]/div/div[1]/button

def login(u,p,driver):
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    var = checkVisibility(driver,'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    var.click()
    var.send_keys(u)
    var=checkVisibility(driver,'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    var.click()
    var.send_keys(p)
    var.send_keys(Keys.RETURN)

    #Depends on Inet Connection
    time.sleep(5)
    if str(driver.current_url) == "https://www.instagram.com/":
        return True
    else:
        print(driver.current_url)
        return False


def checkVisibility(driver,path):
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
    except:
        print("Failed finding Xpath!")
        sys.exit()
    return element


def main():
    #TODO Main Function
    
    username = input("Username: ")
    #could use getpass for psw (not showing the psw in the terminal)
    password = getpass("Passwort: ")
    
    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)



    #Authentication Error
    if not login(username,password,driver) :
        print("AUTH ERROR!")
        sys.exit()

    navigate(driver)

    


def navigate(driver):
    driver.get("https://www.instagram.com/accounts/activity/")
    button =checkVisibility(driver,"/html/body/span/section/main/div/div/div/div/div[1]/div[1]/div")
    button.click()

    amount_of_likes = driver.find_elements_by_xpath('/html/body/span/section/main/div/div/div[1]/div/*/div[3]/div/div[1]/button')


    counter=1
    for i in amount_of_likes:
        i.click() 

    driver.refresh()
    refresh()

    


def refresh():
    #Refresh Insta Notif Site every n minutes
    time.sleep(1800)
    navigate()



if __name__ == '__main__':
    main()

#TODO Error Handling
   # --> Network Errors
   # --> Login Fails
   # --> TimeOuts etc..