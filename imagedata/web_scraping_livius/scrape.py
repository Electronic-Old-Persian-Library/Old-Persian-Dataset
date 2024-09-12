import os
import requests
from lxml import html


def fetch_page_content(url):
    """Fetches the content of a page and returns the parsed HTML tree."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return html.fromstring(response.content)
    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        return None


def extract_links(tree):
    """Extracts and returns links from the specified XPath query."""
    return tree.xpath('//*[@id="content"]/table[2]/tbody/tr/td[1][not(@colspan="6")]//a')


def extract_image_sources(tree):
    """Extracts and returns image sources from the page."""
    return tree.xpath('//*[@id="content"]//img/@src')


def save_image(img_url, folder="images"):
    """Downloads and saves an image from a given URL to the specified folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    try:
        img_data = requests.get(img_url).content
        img_name = os.path.join(folder, img_url.split('/')[-1])
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)
        print(f"Saved image: {img_name}")
    except requests.RequestException as error:
        print(f"Error saving image {img_url}: {error}")


def main():
    url = "https://www.livius.org/sources/content/achaemenid-royal-inscriptions/"
    tree = fetch_page_content(url)

    if tree is None:
        return

    links = extract_links(tree)

    for link in links:
        link_text = link.text_content().strip()
        href = link.get('href')
        if not href.startswith('http'):
            href = "https://www.livius.org/"+href
        print(f"{link_text}: {href}")

        page_tree = fetch_page_content(href)
        if page_tree:
            img_sources = extract_image_sources(page_tree)
            for img_src in img_sources:
                img_src = "https://www.livius.org"+ img_src
                save_image(img_url=img_src , folder=f'images/{link_text}')


if __name__ == "__main__":
    main()
