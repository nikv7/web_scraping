# 🕷️ DFS Web Crawler Using Python

This project implements a simple **Depth-First Search (DFS)** based **web crawler** using Python. It explores a website recursively from a given starting URL up to a specified depth, mimicking the behavior of an **AI search algorithm**.

---

## 🧠 AI Search Algorithm Background

This web crawler applies the concept of **uninformed search** from **Artificial Intelligence**. Specifically, it implements a **Depth-First Search (DFS)** approach, which explores as far as possible along each branch before backtracking.

In this context:
- **Nodes** = Web pages (URLs)  
- **Edges** = Hyperlinks between web pages  
- **Goal** = Crawl as many reachable links as possible from a starting page  
- **Strategy** = DFS traversal using a stack

### Why DFS?

- DFS uses a **stack** to track pages, diving deep into a single path before exploring alternative links.
- Useful for crawling deeply nested structures, e.g., blogs or article series.

---

## 📌 Features

- AI-inspired DFS traversal of web pages.
- Fetches all reachable links from the given URL up to a given depth.
- Avoids revisiting pages using a visited list.
- Prints all crawled URLs and their depth.

---

## 📁 Project Files

- `web crawling(AI).py` – Contains the DFS web crawling logic.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/nikv7/web_crawling_using_py.git
cd web_crawling_using_py
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Crawler

```bash
python main.py
```

You can modify the `start_url` and `max_depth` inside the script.

---

## 🔍 How It Works

1. **Initialize** a stack with the starting URL and depth 0.
2. **Pop** the top URL from the stack.
3. If the URL is **unvisited** and depth is within the allowed limit:
   - Fetch HTML content.
   - Extract all links.
   - Push each new link to the stack with depth +1.
4. **Repeat** until the stack is empty.

---

## 🧪 Example Output

```
RA2311004010387
Crawling: https://nikv7.github.io/web_scraping/ (Depth: 0)
Crawling: https://nikv7.github.io/web_scraping/page1.html (Depth: 1)
Crawling: https://nikv7.github.io/web_scraping/page2.html (Depth: 2)
...

Visited URLs:
https://nikv7.github.io/web_scraping/
https://nikv7.github.io/web_scraping/page1.html
...
```

---

## 🧰 Requirements

- Python 3.x  
- `requests`  
- `beautifulsoup4`  
- `urllib`  

---

## 🎯 Applications

- Demonstrates DFS-style AI search on web data.
- Educational tool for AI and search theory.
- Basis for developing advanced crawlers and web agents.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

AI concepts based on standard university curriculum in Artificial Intelligence and Search Algorithms.
