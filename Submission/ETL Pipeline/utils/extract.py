from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_page(page_num):
    if page_num == 1:
        url = "https://fashion-studio.dicoding.dev/"
    else:
        url = f"https://fashion-studio.dicoding.dev/page{page_num}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("div", class_="product-details")

        data = []
        timestamp = datetime.now().isoformat()

        for product in products:
            try:
                title_tag = product.find("h3", class_="product-title")
                title = title_tag.text.strip() if title_tag else None
                if title == "Unknown Product" or title is None:
                    continue

                price_tag = product.find("span", class_="price")
                price = price_tag.text.strip() if price_tag else None

                rating_tag = product.find("p", string=lambda x: x and "Rating:" in x)
                rating_raw = rating_tag.text.strip() if rating_tag else None
                if rating_raw is None or "Invalid Rating" in rating_raw:
                    continue

                colors_tag = product.find("p", string=lambda x: x and "Colors" in x)
                colors_raw = colors_tag.text.strip() if colors_tag else None

                size_tag = product.find("p", string=lambda x: x and "Size:" in x)
                size_raw = size_tag.text.strip() if size_tag else None

                gender_tag = product.find("p", string=lambda x: x and "Gender:" in x)
                gender_raw = gender_tag.text.strip() if gender_tag else None

                data.append(
                    {
                        "Title": title,
                        "Price": price,
                        "Rating": rating_raw,
                        "Colors": colors_raw,
                        "Size": size_raw,
                        "Gender": gender_raw,
                        "Timestamp": timestamp,
                    }
                )
            except Exception as e:
                print(f"⚠️ Error parsing product on page {page_num}: {e}")
        return data

    except Exception as e:
        print(f"❌ Error fetching page {page_num}: {e}")
        return []


def extract_all():
    all_data = []
    for page in range(1, 51):
        print(f"🔍 Scraping page {page}...")
        page_data = scrape_page(page)
        all_data.extend(page_data)

    df = pd.DataFrame(all_data)
    return df
