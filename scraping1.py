import os
import requests
from bs4 import BeautifulSoup

# Create the directory for saving images if it doesn't already exist
os.makedirs('external_resources', exist_ok=True)

# List of page URLs to scrape
urls_sofas = [
    'https://www.ikea.com/us/en/cat/sofas-fu003/',
    'https://www.shutterstock.com/search/isolated-sofa'
]

urls_beds = [
    'https://www.ikea.com/us/en/cat/beds-bm003/',
]

urls_tables = [
    'https://www.ikea.com/us/en/cat/tables-desks-fu004/',
]

urls_dressers = [
    'https://www.ikea.com/us/en/cat/chest-of-drawers-10402/',
]

urls_chairs = [
    'https://www.ikea.com/us/en/cat/chairs-fu002/',
]


# Function to download images
def download_images(url, category):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')  # Assuming images are tagged with <img>
    limit = 10000  # Limit the number of images to download
    downloaded = 0
    for i, img in enumerate(images):
        if downloaded == limit:
            break
        # Construct image URL
        img_url = img['src']
        if not img_url.startswith(('http', 'https')):
            img_url = f"{url}{img_url}"  # Handling relative URLs
        
        # Download and save the image
        try:
            img_data = requests.get(img_url).content
            with open(f'external_resources/{category}_{i}.jpg', 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded {category}_{i}.jpg from {img_url}")
        except Exception as e:
            print(f"Could not download image from {img_url}. Error: {e}")

# Loop through urls and categories
categories = ['beds', 'tables', 'sofas', 'dressers', 'chairs']
for category in categories:
    if category == 'sofas':
        for url in urls_sofas:
            download_images(url, category)
    elif category == 'beds':
        for url in urls_beds:
            download_images(url, category)
    elif category == 'tables':
        for url in urls_tables:
            download_images(url, category)
    elif category == 'dressers':
        for url in urls_dressers:
            download_images(url, category)
    elif category == 'chairs':
        for url in urls_chairs:
            download_images(url, category)


print("Image download complete.")
