from selenium import webdriver
from selenium.webdriver.common.by import By
import time
urlPath=input()
driver = webdriver.Chrome() 
driver.get(urlPath)

def fillingTheForm():
    listItems=driver.find_elements(By.CLASS_NAME,"Qr7Oae")
    #in listItems we will have all the questions list
    for item in listItems:
        # time.sleep(1) 
        heading=item.find_element(By.CLASS_NAME,"M7eMe").text
        textArea=item.find_elements(By.CLASS_NAME,"whsOnd")
        #in heading we have the heading of a quesion
        if(len(textArea)>=1 and textArea[0].get_attribute('data-initial-value')==''):
            textArea[0].send_keys("hello ",heading)
        #in this if we have textArea and it is empty we will fill it with hello heading 
        radioButtons=item.find_elements(By.CLASS_NAME,"oyXaNc")
        if(len(radioButtons)):
            for radioButton in radioButtons:
                options=radioButton.find_elements(By.CLASS_NAME,"Od2TWd")
                val=[]
                for option in options:
                    val.append(option.get_attribute('aria-checked'))
                if('true' not in val):
                    options[0].click()
                #if no option is selected in the multi choice we will keep the first option
    buttonList=driver.find_elements(By.CLASS_NAME,'NPEfkd')
    for button in buttonList:
        if(button.text=="Next"):
            button.click()
            fillingTheForm()    # if page has next button we will call the fun on next page
            return 
        if(button.text=="Submit"):
            button.click()      # if submit we will submit the form
            return

fillingTheForm()

driver.quit()
