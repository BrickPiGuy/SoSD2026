#!/usr/bin/env python3
"""
Test potential replacement URLs for broken links
"""

import requests

test_urls = {
    "OWASP ZAP": [
        "https://www.zaproxy.org/",
        "https://owasp.org/www-project-zap/",
    ],
    "InfoQ Trends": [
        "https://www.infoq.com/articles/",
        "https://www.infoq.com/",
    ],
    "Rust Why": [
        "https://www.rust-lang.org/",
        "https://www.rust-lang.org/what/",
    ],
    "Hacker News": [
        "https://news.ycombinator.com/",
    ]
}

for category, urls in test_urls.items():
    print(f"\n{category}:")
    for url in urls:
        try:
            response = requests.head(url, timeout=5, allow_redirects=True, verify=False)
            print(f"  {url}: {response.status_code}")
        except Exception as e:
            print(f"  {url}: ERROR - {e}")
