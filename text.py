from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

driver = webdriver.Firefox()
driver.minimize_window()
f = open("Data\\baseurl.txt", "r")
url = f.read()
print('\nURL Read\n')
i=1
tresult = 0
#file open
f = open("Data\\filename.txt", "r")
filename = f.read()
f = open('Data\\'+filename+'.csv','w',encoding='utf-8')
headers = "Name, Address, Contact"
f.write(headers)
print('\nFile created and header printed\n')

print('\nBrowser Started\n')
#loop starts

while True:
    s=0
    
    driver.get(url)
    
    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    print('Printing of Page '+str(i)+' Data Started \n')
    #main concept
    officials = soup.findAll("div",{"class":"VkpGBb"})
    for every in officials:
         container = every.find("div",{"class":"BSaJxc"})
         if container != None :
                 
                 containerq = (every.find("div",{"class":"dbg0pd"}))
                 containerw = (every.span.div.find_next_sibling())
                 containerr = ((every.span.div.find_next_sibling()).find_next_sibling())
                   
                 if(containerr is None or containerr == "" or containerr ==" "):
                     container3 = 'Null'
                 elif(containerq is None or containerq == "" or containerq ==" "):
                     Containerq = 'Null'
                 elif(containerw is None or containerw == "" or containerw ==" "):
                     Containerw = 'Null'
                 else:
                     container3 = containerr.text
                     container2 = containerw.text
                     container1 = containerq.text
                 f.write("\n"+container1.replace(",","|") + "," + container2.replace(",","|") + "," + container3)
                 print('line printed')
                 tresult = tresult + 1
                 s = s+1
                 
    print('\n Page Successful')
    #redirect
    if (len(driver.find_elements_by_id('pnnext'))>0):
        link = driver.find_element_by_link_text('Next')
        link.click()
        url = driver.current_url
        print("\n Page " +str(i)+" Successful with "+str(s)+" results \n")
        print("-============================================================-\n\n")
        i=i+1
    else:
        print('\n No more Data Left')
        break
    
print('Program Executed Successfully \n Total number Of Pages Scanned :'+str(i)+'\n Total number Of Data Found: '+str(tresult))
f.close()
time.sleep(8)
driver.quit()
