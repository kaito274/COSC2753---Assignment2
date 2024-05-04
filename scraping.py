import requests
from bs4 import BeautifulSoup
import os

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download images from a URL
def download_images(image_urls, directory):
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{directory}/image_{i+1}.jpg", "wb") as f:
                    f.write(response.content)
                with open(f"{directory}/image_{i+1}.png", "w") as f:
                    f.write(response.content)
                with open(f"{directory}/image_{i+1}.jpeg", "w") as f:
                    f.write(response.content)
        except Exception as e:
            print(f"Error downloading image {url}: {e}")

# Function to scrape image URLs from Google Images
def scrape_image_urls(query, num_images):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    image_tags = soup.find_all("img", limit=num_images)
    image_urls = [tag["src"] for tag in image_tags if "http" in tag["src"]]  # Filter out URLs without scheme
    return image_urls

# Main function to initiate scraping
def main():
    categories = ["beds", "tables", "sofas", "dressers", "chairs"]
    num_images = 10000  # Number of images to scrape for each category

    external_resources_dir = "external_resources"
    for category in categories:
        image_urls = scrape_image_urls(category, num_images)
        category_dir = os.path.join(external_resources_dir, category)
        create_directory(category_dir)
        download_images(image_urls, category_dir)

if __name__ == "__main__":
    main()
