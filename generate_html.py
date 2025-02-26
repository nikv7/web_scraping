import os

# Define the structure of the website
pages = {
    "index.html": ["page1.html", "page2.html", "page3.html"],
    "page1.html": ["page1a.html", "page1b.html"],
    "page1a.html": ["page1a1.html", "page1a2.html"],
    "page1a1.html": ["page1a1a.html"],
    "page2.html": ["page2a.html", "page2b.html"],
    "page3.html": ["page3a.html"],
}

# Function to create an HTML file
def create_html_file(filename, links):
    with open(filename, "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n<head>\n")
        f.write(f"    <title>{filename.replace('.html', '').capitalize()}</title>\n")
        f.write("</head>\n<body>\n")
        f.write(f"    <h1>{filename.replace('.html', '').capitalize()}</h1>\n")
        if links:
            f.write("    <ul>\n")
            for link in links:
                f.write(f"        <li><a href='{link}'>{link.replace('.html', '').capitalize()}</a></li>\n")
            f.write("    </ul>\n")
        f.write("</body>\n</html>\n")

# Ensure the directory exists
os.makedirs("web_crawler_site", exist_ok=True)

# Generate each HTML file
for page, links in pages.items():
    create_html_file(os.path.join("web_crawler_site", page), links)

print("HTML files generated successfully in 'web_crawler_site' folder.")
