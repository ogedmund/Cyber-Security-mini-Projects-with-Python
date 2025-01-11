import requests
from bs4 import BeautifulSoup

URL = "https://www.projecthoneypot.org/list_of_ips.php" 
html_content = requests.get(URL)
soup = BeautifulSoup(html_content, 'html.parser')

ip_addresses = [] #store the data being read
for row in soup.select('table.manmx tr')[1:]: #read the data but skip first line ([1:0])
    ip_cell = row.select_one('td a.bnone') 
    if ip_cell:
        ip_addresses.append(ip_cell.text.strip())

for ip in ip_addresses: 
    print(ip)

with open('iplist.txt', 'w') as file:  #Assuming there was an iplist.txt file to save the result to
    for ip in ip_addresses: 
        print(ip)
        file.write(ip + '\n')"""
