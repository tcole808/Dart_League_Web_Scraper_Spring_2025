from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True  # Run in headless mode (no browser window)
options.binary_location = "/usr/bin/chromium-browser"  # Path to Chromium in WSL

# Use the built-in Chromedriver from WSL installation
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

with open('links5.txt', 'r') as file:
    url = file.readline().strip()

driver.get(url)
driver.implicitly_wait(10)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

links = []
for a_tag in soup.find_all('a', href=True):
    if 'recap.dartconnect.com' in a_tag['href']:
        links.append(a_tag['href'])

if links:
    print("Links found:")
    for link in set(links):
        print(link)
else:
    print("No links found.")

with open("links.txt", "w") as file:
    for link in set(links):
        file.write(link + "\n")

driver.quit()
