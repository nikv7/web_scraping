import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def fetch_webpage(url):
    """Fetches the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
def extract_links(html, base_url):
    """Extracts all links from a webpage."""
    soup = BeautifulSoup(html, "html.parser")
    links = list()
    for anchor in soup.find_all("a", href=True):
        link = urljoin(base_url, anchor["href"])
        links.append(link)
    return links
def web_crawler_dfs(starting_url, max_depth):
    """Crawls the web using DFS."""
    visited = list()
    stack = [(start_url, 0)]  # (url, depth)
    while stack:
        current_url, depth = stack.pop()

        if current_url not in visited and depth <= max_depth:
            print(f"Crawling: {current_url} (Depth: {depth})")
            visited.append(current_url)

            html = fetch_webpage(current_url)
            if html:
                links = extract_links(html, current_url)
                for link in links:
                    stack.append((link, depth + 1))
    return visited
# Example usage
if __name__ == "__main__":
    start_url = "https://nikv7.github.io/web_scraping/"  # Starting URL
    max_depth = 4  # Maximum depth to crawl
    print("RA2311004010387")
    crawled_urls = web_crawler_dfs(start_url, max_depth)

    print("\nVisited URLs:")
    for url in crawled_urls:
        print(url)
