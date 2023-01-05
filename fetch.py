import argparse
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import datetime
import os

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add a flag for printing metadata
parser.add_argument("--metadata", action="store_true", help="print metadata about the page")

# Add a positional argument for the URL(s)
parser.add_argument("url", nargs="+", help="URL(s) to fetch")

# Parse the command line arguments
args = parser.parse_args()

# Get the list of URLs
urls = args.url

# Fetch and save each URL
for url in urls:
    try:
        # Fetch the web page
        response = urllib.request.urlopen(url)
        html = response.read()

        # Parse the URL
        url_parsed = urllib.parse.urlparse(url)

        # Parse the HTML
        soup = BeautifulSoup(html, "html.parser")

        # Extract the metadata
        num_links = len(soup.find_all("a"))
        num_images = len(soup.find_all("img"))
        last_fetch = datetime.datetime.utcnow().isoformat()

        # Print the metadata if the --metadata flag was passed
        if args.metadata:
            print(f"\nsite: {url}")
            print(f"num_links: {num_links}")
            print(f"num_images: {num_images}")
            print(f"last_fetch: {last_fetch}")

        # Create a directory to store the assets
        assets_path = 'assets/'
        os.makedirs(assets_path, exist_ok=True)
        asset_dir = os.path.join(assets_path, os.path.basename(url_parsed.netloc))
        os.makedirs(asset_dir, exist_ok=True)

        # Replace the URLs of the assets with local file paths
        for img in soup.find_all("img"):
            img_src = img.attrs.get("src")
            if img_src:
                # Download the asset
                asset_url = urllib.parse.urljoin(url, img_src)
                asset_response = urllib.request.urlopen(asset_url)
                asset_data = asset_response.read()

                # Save the asset to a file
                asset_filename = os.path.join(asset_dir, img_src.split("/")[-1]).replace("?", ".")
                try:
                    with open(asset_filename, "wb") as f:
                        f.write(asset_data)
                    # Replace the URL with the local file path
                    img.attrs["src"] = asset_filename
                except Exception as e:
                    print(f"- error saving image [skipping]: {img_src}")

        # Save the modified HTML to a file
        file_name = (url_parsed.netloc + url_parsed.path).rstrip("/")
        file_name = file_name.replace("/", "-")
        file_name += '.html'
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(str(soup))
            print(f"✓ successfully saved file: {file_name}")

    except Exception as e:
        print(f"error while downloading url {url} -- skipping")
        print(e)
