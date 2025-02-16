from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configure headless Chrome in WSL
options = Options()
options.headless = True
options.binary_location = "/usr/bin/chromium-browser"
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

# Read links from links.txt
with open("links.txt", "r") as file:
    original_links = [line.strip() for line in file]

games_links = []

# Visit each link and extract /games/ links
x=1
for url in original_links:
    print(f"Scanning {x}/{len(original_links)} : {url}")
    driver.get(url)
    time.sleep(5)  # Allow the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    for a_tag in soup.find_all('a', href=True):
        if '/games/' in a_tag['href']:  # Look specifically for /games/ links
            games_links.append(a_tag['href'])
            print(f"Changed URL to: {a_tag['href']}")
            x += 1
# Display and save the links
if games_links:
    print("Links with /games/ found:")
    for link in games_links:
        print(link)

    with open("links3.txt", "w") as output:  # Save to links3.txt
        for link in games_links:
            output.write(link + "\n")
else:
    print("No links with /games/ found.")

driver.quit()

