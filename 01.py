import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://old.namanarora.xyz"

# Send request to the website
response = requests.get(url)

# Check whether the request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    print("WEB SCRAPING RESULT")
    print("-------------------")

    # Extract webpage title
    print("Page Title:", soup.title.get_text(strip=True))

    # Extract headings
    print("\nHeadings:")
    for heading in soup.find_all(["h1", "h2", "h3"]):
        print("-", heading.get_text(strip=True))

    # Extract hyperlinks
    print("\nLinks:")
    for link in soup.find_all("a", href=True):
        print(link.get_text(strip=True), "->", link["href"])

else:
    print("Unable to access the webpage.")
