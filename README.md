# snsk.github.io

This repository hosts the static files for the website.

## Running the link check test

The project includes a simple script to verify that local links in the HTML
files point to existing resources. Install `beautifulsoup4` and run the script:

```bash
pip install beautifulsoup4
python tests/test_links.py
```

The script will exit with a non-zero status if any referenced file is missing.
