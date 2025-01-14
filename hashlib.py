import requests
import hashlib 

response = Requests.get("https://letsdefend.io/robots.txt") #assigning the get URL response to response

if response.status_code == 200:
  file_content = respomse.text.encode()
  sha256_hash = hashlib.sha256()
  sha256_hash.update(file_content)
  sha256_value = sha256_hash.hexdigest()
  print(sha256_value)
