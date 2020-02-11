import patoolib
import requests
import os
from webbot import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


config = open("config.txt", "r")
configLines = config.read().splitlines()
downloadsFolder = configLines[0]
outDirectory = configLines[1]
noesisInUse = configLines[2]
noesisUser = configLines[3]
noesisPW = configLines[4]

config.close
from time import sleep

while(True):
    valinta = input("Input direct link to demo or e to exit program: ")

    if valinta=="1":
        web.quit()
        break

    nimi = input("Name of the match: ")
    lahde = input("esea or hltv e/h: ")
    os.mkdir(outDirectory+nimi)
    
    if lahde == "e":
        web = Browser()        
        web.go_to(valinta)
        web.click("Katso Demo")        
        web.driver.minimize_window()
        eseaNumero = valinta.split("/")
        eseaNumero = eseaNumero[-1]
        print(downloadsFolder+"esea_match_"+eseaNumero+".zip")
       
        while not os.path.exists(downloadsFolder+"esea_match_"+eseaNumero+".zip"):
            sleep(1)
        patoolib.extract_archive(downloadsFolder+"esea_match_"+eseaNumero+".zip",outdir=outDirectory+nimi)
        web.close_current_tab()
        
              
    elif lahde == "h":
        try:
            
            
            hltvFile = requests.get(valinta)
            open(downloadsFolder + "\\demo.rar", "wb").write(hltvFile.content)
            patoolib.extract_archive(downloadsFolder+"demo.rar", outdir=outDirectory+nimi)
        except:
            print("Something went wrong. Perhaps there is already a match with the same name?")

    else:
        print("You didn't choose e or h!")

        
            #print("Something went wrong. Perhaps there is already a match with the same name?")
            
            
            
            
    if(noesisInUse):
        noesikseen = input("Upload to Noesis y/n :")

        if noesikseen=="y":
            
            
            web.go_to('noesis.gg/app/')
            web.type(noesisUser , into='Username')
            web.type(noesisPW , into='Password')
            web.click('Sign in')
            web.go_to('noesis.gg/app/#/console/upload/')
            
            sleep(2)
            filuname = os.listdir(outDirectory+nimi)[0]
            web.driver.find_element_by_xpath("//input[@name = 'demo-upload-file']").send_keys(outDirectory + nimi + "\\" + filuname)
            web.click("UPLOAD")
            web.driver.minimize_window()
            while not web.exists("Analysis complete!"):
                sleep(1)
                
            web.close_current_tab()
            
        
        
        

    #C:\\Users\\Jere\\Documents\\  C:\\Users\\Jere\\Downloads\\demo.rar
