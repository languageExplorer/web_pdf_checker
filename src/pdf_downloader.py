import requests
from bs4 import BeautifulSoup
import os


def download_pdf(path):
    # URL from which PDFs are to be downloaded
    url = "" # ⚠️ Place to write the URL

    # Headers to mimic a browser request
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
    }

    # Request URL and get response object
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')

    # Ensure the directory to save files exists
    os.makedirs(path, exist_ok=True)

    # i = 0

    # From all links check for PDF links and download the file
    for link in links:
        href = link.get('href', [])
        if '.pdf' in href:
            # i += 1
            print(f"Downloading the PDF file")

            # Handle relative URLs
            if not href.startswith('http'):
                href = requests.compat.urljoin(url, href)

            # Get response object for link
            pdf_response = requests.get(href, headers=headers)
            pdf_response.raise_for_status()

            # Write content in PDF file
            pdf_path = os.path.join(path, f"last_file.pdf")
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)

            print(f"The file is downloaded")
            break

    print("All PDF files downloaded")
