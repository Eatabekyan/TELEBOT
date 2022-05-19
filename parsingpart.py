import logging
import requests

from bs4 import BeautifulSoup
Infostart = 0
Infoend = 20

def newsfunc(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="post-list")
    summary = results.find_all("div", class_ ="post-summary")
    info=""
    for i in summary:
        info += i.text + "\n\n\n\n\n"
    
    return info

def FIOfunc(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="bodyContent")
    soup = results.find(id="mw-content-text")
    
    element  = soup.find("table", class_="wikitable card")
    job_elements = element.find_all("tr")
    job_elements_1 = results.find_all("p")
  
    info=""
    for job_element in job_elements:
        info += "::"+job_element.text
    i = Infostart
    for jelement in job_elements_1:
        if i == Infoend:
            break
        info += jelement.text+"\n"
        i += 1
    
    return info
