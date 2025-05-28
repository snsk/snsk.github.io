import os
import sys
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Collect all html files in root directory
HTML_DIRS = [ROOT_DIR]

# Acceptable schemes for remote links
REMOTE_SCHEMES = ("http://", "https://", "mailto:")

def find_html_files():
    for dir_path in HTML_DIRS:
        for fname in os.listdir(dir_path):
            if fname.endswith('.html'):
                yield os.path.join(dir_path, fname)

def check_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    for tag in soup.find_all(['a', 'img', 'script', 'link']):
        attr = 'href' if tag.name in ['a', 'link'] else 'src'
        link = tag.get(attr)
        if not link or link.startswith(REMOTE_SCHEMES) or link.startswith('#'):
            continue
        target_path = os.path.join(os.path.dirname(file_path), link)
        if not os.path.exists(target_path):
            print(f"Missing asset referenced in {file_path}: {link}")
            return False
    return True

def main():
    all_ok = True
    for html_file in find_html_files():
        if not check_links(html_file):
            all_ok = False
    if not all_ok:
        sys.exit(1)

if __name__ == '__main__':
    main()
