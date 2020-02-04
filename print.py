from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.tiktok.com/trending/?lang=en"

uClient = Request(url, headers={'User-Agent': 'Chrome/79.0.3945.130', 'cookie': 'tt_webid_v2=6788578608383362565; _ga=GA1.2.531912397.1580589130; _gid=GA1.2.1526704251.1580764151; ak_bmsc=46D2485C5199B7BFF7510D8DDCC6025B48F7F01D34500000F68B385EADB4E449~plm/JfWQ2GCzFPhkcNK7+cuCexRw4j9XGbfEcOE9ZpAAuHBqj507Ky+OeeNJWcCtW9oD3ACEXqgnB/IvjjvzA+Jo5HyzbNBYZEVmxIANlkk10Xov5IQspyU3uZtd5QN3KYUO2nEWr45l8JVFe/acZ7Q3r2sa6EB2qNgS2CRYZXpPmATf64rfXkm6L21z99o9/P+7zTH+RbyIhZQEW2xHY0W1FWRgX69csoibDsKnfxSa7+us8jZLjSZyMyomkSsRjs; SLARDAR_WEB_ID=3a75d4fa-a546-4bbc-8f21-709db11d3374; bm_sv=7C944E4014A5B9488C263D620E7821CB~LhQm7n91rnne0SS2J9kLnCCm1vHWsZUeE10yHSsk9L714zqvxR5kDxTHzXziQgVr5cHZ1A65uW09Jo0YDbBclwVP0GTBWcmP/Q1XH8KQ/pYpx+d2glIghU4ZjEHUennMVpZjwGUbWoglOOLY12Zb9i63rZ96hXSoQ55D/BtHstI='})
html = urlopen(uClient).read()

page_soup = soup(html, features="html.parser")
#print(page_soup.prettify())

match = page_soup.find_all('div',{'class':'jsx-1464109409 image-card'})
#match = page_soup.find("div",{'class':'jsx-1410658769 video-feed-item'})
print(match)

# name of the video classes class="jsx-1410658769 video-feed-item"