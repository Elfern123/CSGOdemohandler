import patoolib
import requests
import os
import gzip
import shutil
from webbot import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

config = open("config.txt", "r")
configLines = config.read().splitlines()
downloadsFolder = configLines[0]
outDirectory = configLines[1]
noesisInUse = configLines[2]
noesisUser = configLines[3]
noesisPW = configLines[4]


config.close
webOn = False


while(True):
    query = input("Input direct link to an HLTV demo/Faceit demo/ESEA match page or e to exit program: ")

    if query=="e":
        web.quit()
        break

    matchName = input("Name of the match: ")
    os.mkdir(outDirectory+matchName)
    
    if "esea" in query:

        try:
            web = Browser()
            webOn = True;
            web.go_to(query)
            web.click("Katso Demo")        
            web.driver.minimize_window()
            eseaNumber = query.split("/")
            eseaNumber = eseaNumber[-1]
            print(downloadsFolder+"esea_match_"+eseaNumber+".zip")
           
            while not os.path.exists(downloadsFolder+"esea_match_"+eseaNumber+".zip"):
                sleep(1)
            patoolib.extract_archive(downloadsFolder+"esea_match_"+eseaNumber+".zip",outdir=outDirectory+matchName)
            #web.close_current_tab()
        except:
            print("Failed to fetch demo or extract demo. Is the link valid ESEA match link? Also make sure unrar.exe is in the same folder as this program.")
        
              
    elif "hltv" in query:
        try:
            
            
            hltvFile = requests.get(query)
            open(downloadsFolder + "\\demo.rar", "wb").write(hltvFile.content)
            patoolib.extract_archive(downloadsFolder+"demo.rar", outdir=outDirectory+matchName)
        except:
            print("Something went wrong. Perhaps there is already a match with the same name?")

    elif "faceit" in query:
        try:
            faceitFile = requests.get(query)
            open(downloadsFolder + "\\demo.gz","wb").write(faceitFile.content)
            with gzip.open(downloadsFolder + "\\demo.gz", 'r') as f_in, open(outDirectory+matchName+"\\"+matchName+".dem", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            
           

        except Exception as e:
            print(e)

    else:
        print("Only HLTV or ESEA demos supported currently!")

                             
    if(noesisInUse):
        toNoesis = input("Upload to Noesis y/n :")

        if toNoesis=="y":
            if not webOn:
                web = Browser() 
            
            web.go_to('noesis.gg/app/')
            web.type(noesisUser , into='Username')
            web.type(noesisPW , into='Password')
            web.click('Sign in')
            web.go_to('noesis.gg/app/#/console/upload/')
            sleep(2)
            filename = os.listdir(outDirectory+matchName)[0]
            web.driver.find_element_by_xpath("//input[@name = 'demo-upload-file']").send_keys(outDirectory + matchName + "\\" + filename)
            web.click("UPLOAD")
            web.driver.minimize_window()
            while not web.exists("Analysis complete!"):
                sleep(1)
                
            web.close_current_tab()
            
        
        
        


