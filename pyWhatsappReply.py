from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/Azeem Bukhari/OneDrive/Documents/Projex/Python/Apps/chromedriver/chromedriver.exe")
driver.get('https://web.whatsapp.com/')
t_exit = 0;
        
def send_custom_message():
    print ("Please enter the receipient name")
    r_name = input()
    
    if (input):
        print ("Enter Message \n")
        r_msg = input()
        
        if (r_msg):
            count = 0
            count = input("Enter Message Count")
            if (count):
                count = int (count)
            else : 
                print ("Error : Invalid Count")
            user = driver.find_element_by_class_name('_2S1VP')
            user.send_keys(r_name)
            user.send_keys(Keys.RETURN)
            while (count):
                msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                msg_box.send_keys(r_msg)
                button = driver.find_element_by_class_name('_35EW6')
                button.click()
                count = count - 1
            print ("Message Sent Successfully")
        else :
            print ("Error : Empty Message")
    else :
        print ("Receipent Name Error!!")
        
        
while (t_exit == 0):  
    print ("1. Send Custom Message")
    print ("0. Exit")
    t_input = input ()
    if (t_input):
        t_input = int (t_input)
    if (t_input == 1):
        send_custom_message()
    elif (t_input == 0):
        print ("Exiting.... Thankyou!!!")
        t_exit = 1;
    else :
        print ("Invalid Input.. Please retry")
        
