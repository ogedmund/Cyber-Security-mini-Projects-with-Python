import requests from bs4 #The requests module allows communicating with web servers using the HTTP protocol
import BeautifulSoup #BeautifulSoup library is used to parse HMTL and XML docs
URL = "https://letsdefend.io"  
page = requests.get(URL) # HTTP GET request is sent to the specified URL using the "requests.get()" method
soup = BeautifulSoup(page.content, "html.parser") #instance of the BeautifulSoup class
results = soup.find("meta", {"name":"description"}) 

print(results)
