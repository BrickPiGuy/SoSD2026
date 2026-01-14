#!/usr/bin/env python3
"""
Script to check all external links in HTML files for 404 and other errors.
"""

import os
import re
import requests
from urllib.parse import urlparse
from collections import defaultdict
import sys

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

def extract_links_from_html(html_content):
    """Extract all href links from HTML content."""
    # Match href="..." and href='...'
    pattern = r'href=(["\'])([^"\']+)\1'
    matches = re.findall(pattern, html_content)
    return [url for _, url in matches]

def is_external_link(url):
    """Check if a link is external (starts with http/https)."""
    return url.startswith('http://') or url.startswith('https://')

def check_link(url, timeout=5):
    """Check if a URL is accessible."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True, verify=False)
        return {
            'url': url,
            'status': response.status_code,
            'ok': response.status_code < 400,
            'error': None
        }
    except requests.Timeout:
        return {'url': url, 'status': None, 'ok': False, 'error': 'Timeout'}
    except requests.RequestException as e:
        return {'url': url, 'status': None, 'ok': False, 'error': str(e)}

def main():
    # Get all HTML files in current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    all_links = defaultdict(list)
    broken_links = []
    
    print("Extracting links from HTML files...")
    print(f"Found {len(html_files)} HTML files\n")
    
    # Extract all links
    for html_file in sorted(html_files):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = extract_links_from_html(content)
            external_links = [l for l in links if is_external_link(l)]
            all_links[html_file] = external_links
            print(f"{html_file}: {len(external_links)} external links")
    
    # Get unique links across all files
    unique_links = set()
    for links in all_links.values():
        unique_links.update(links)
    
    print(f"\nTotal unique external links: {len(unique_links)}\n")
    print("Testing links...\n")
    
    # Test each link
    results = {}
    for i, url in enumerate(sorted(unique_links), 1):
        print(f"[{i}/{len(unique_links)}] Testing: {url}", end=' ... ')
        result = check_link(url)
        results[url] = result
        
        if result['ok']:
            print(f"✓ ({result['status']})")
        else:
            print(f"✗ ({result['status'] or result['error']})")
            broken_links.append(result)
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    working = sum(1 for r in results.values() if r['ok'])
    broken = sum(1 for r in results.values() if not r['ok'])
    
    print(f"✓ Working links: {working}")
    print(f"✗ Broken/problematic links: {broken}\n")
    
    if broken_links:
        print("BROKEN LINKS DETAILS:")
        print("-" * 80)
        for result in sorted(broken_links, key=lambda x: x['url']):
            print(f"\nURL: {result['url']}")
            print(f"Status: {result['status'] or result['error']}")
            # Find which files have this link
            files_with_link = [f for f, links in all_links.items() if result['url'] in links]
            print(f"Found in: {', '.join(files_with_link)}")
    
    # Status code breakdown
    print("\n" + "="*80)
    print("STATUS CODE BREAKDOWN:")
    print("="*80)
    status_breakdown = defaultdict(list)
    for url, result in results.items():
        status = result['status'] or result['error']
        status_breakdown[status].append(url)
    
    for status in sorted(status_breakdown.keys(), key=str):
        count = len(status_breakdown[status])
        print(f"{status}: {count} links")

if __name__ == '__main__':
    main()
