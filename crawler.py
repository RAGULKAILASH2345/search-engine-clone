from database import get_db_connection
from bs4 import BeautifulSoup
import requests

def crawl_page(url):
    try:
        headers = {'User-Agent':"MySearchEngineBot/1.0(A simple search engine project,student-bott@example.com)"}
        response = requests.get(url,headers=headers,timeout=(3,5))
        response.raise_for_status()
        soup = BeautifulSoup(response.text,'html.parser')
        for tag in soup(['script','style']):
            tag.decompose()
        title = soup.title.string if soup.title else "No Title"
        div = soup.find('div',id='bodyContent')
        if div:
            content = div.get_text(strip=True)
        else:
            content = soup.get_text(strip=True)
        print(f"Title: {title}")
        print(f"Content Length: {len(content)} characters")
        return response.text
    except requests.Timeout:
        print("Request Time out.")
        return None
    except requests.exceptions.HTTPError as et:
        print(f"HTTP Error: {et.response.status_code}")
        print(f"Error Message: {et.response.text}")
        return None
    except requests.RequestException as e:
        print(f"Error : {e}")
        return None