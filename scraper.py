from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def find_jobs(jobName, city, state):
    url = "https://www.indeed.com/jobs?q=" + jobName + "&l=" + city + "%2C+" + state
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"})

    #now need to grab each product that I want
    for container in containers:
        name = container.a.text.strip()
        url = "https://indeed.com/" + container.a['href']
        compare_description(url)
        # now should loop through the links and compare against your skillset


def compare_description(url):
    uclient = uReq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "jobsearch-jobDescriptionText"})

    for container in containers:
        value = page_soup.findAll("b")
        value2 = page_soup.findAll("div")

find_jobs("Software+Development", "Atlanta", "GA")
