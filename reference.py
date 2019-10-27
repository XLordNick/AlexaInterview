#serves as the database for buzzowrds
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

pos_buzzword = {"Agile":(), "DevOps":(), "Responsive Deisgn":(), "Unit Testing":(), 
    "Artificial Intelligence":(), "Big Data":(), "Cloud":(), "Algorithm":(), "API":(),
    "Application":(), "Adaptive Design":(), "Bootstrap":(), "Backend":(), "Bug":(),
    "Cache":(), "CSS":(), "Data Structure":(), "Debugging":(), "Deployment":(),
    "Documentation":(), "Domain Name":(), "Framework":(), "Frontend":(), "Full-Stack":(),
    "Git":(), "GitHub":(), "HTML":(), "HTTP":(), "Information Architecture":(), "Java":(),
    "JavaScript":(), "jQuery":(), "Libraries":(), "Mobile-First":(), "MVP":(), "MySQL":(), 
    "Operating System":(), "PHP":(), "Plugin":(), "Python":(), "Resolution":(), 
    "Responsive Design":(), "Ruby":(), "Ruby and Rails":(), "Sitemap":(), "Software Stack":(), 
    "SSL":(), "UI Design":(), "UX Design":(), "Version Control":(), "Web App":(), "Wireframe":(),}

neg_buzzword = ["um", "OMG", "sure", "cool", "kinda", "we"]

url = "http://www.bannedwordlist.com/lists/swearWords.txt"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

for word in str(page_soup).split("\n"):
    word = word.replace("\r", "")
    neg_buzzword.append(word)