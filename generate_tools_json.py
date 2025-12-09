#!/usr/bin/env python3
"""
Generate tools.json from HTML files and their corresponding .docs.md files.
This script extracts metadata about tools including titles, descriptions, and dates.
"""

import json
import re
import subprocess
from pathlib import Path
from datetime import datetime


def extract_title_from_html(html_path):
    """Extract the title from an HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Look for <title> tag
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1)
            # Clean up common suffixes
            title = re.sub(r'\s*[|\-]\s*.+$', '', title)
            return title.strip()
    return None


def extract_description_from_docs(docs_path):
    """Extract the first paragraph/description from a .docs.md file."""
    if not docs_path.exists():
        return None
    
    # Minimum length for a substantial paragraph (to skip short fragments)
    MIN_DESCRIPTION_LENGTH = 20
    
    with open(docs_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Remove any HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        # Remove markdown headers
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        # Skip lines that are just headers or empty
        for line in lines:
            if not line.startswith('#') and len(line) > MIN_DESCRIPTION_LENGTH:
                # Take first substantial paragraph
                return line
    return None


def get_git_dates(file_path):
    """Get created and updated dates from git history."""
    try:
        # Get the first commit date (created)
        result = subprocess.run(
            ['git', 'log', '--follow', '--format=%aI', '--reverse', '--', file_path],
            capture_output=True,
            text=True,
            check=True,
            timeout=10  # Prevent hanging on long-running git operations
        )
        dates = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
        
        if dates:
            created = dates[0]
            updated = dates[-1] if len(dates) > 1 else created
            return created, updated
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, Exception):
        pass
    
    return None, None


def generate_tools_json():
    """Generate tools.json from all HTML tool files."""
    tools = []
    
    # Find all HTML files except potential index.html
    html_files = sorted(Path('.').glob('*.html'))
    
    for html_path in html_files:
        # Skip index.html if it exists
        if html_path.name == 'index.html':
            continue
        
        slug = html_path.stem
        docs_path = Path(f'{slug}.docs.md')
        
        # Extract metadata
        title = extract_title_from_html(html_path)
        description = extract_description_from_docs(docs_path)
        created, updated = get_git_dates(str(html_path))
        
        tool_data = {
            'slug': slug,
            'title': title or slug.replace('-', ' ').title(),
            'url': f'{slug}.html'
        }
        
        if description:
            tool_data['description'] = description
        
        if created:
            tool_data['created'] = created
        
        if updated:
            tool_data['updated'] = updated
        
        tools.append(tool_data)
    
    # Sort by updated date (newest first), then by title
    # Use a very old date as default for tools without dates to sort them to the end
    tools.sort(key=lambda x: (x.get('updated', '1970-01-01'), x.get('title', '')), reverse=True)
    
    # Write to tools.json
    with open('tools.json', 'w', encoding='utf-8') as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    
    print(f'Generated tools.json with {len(tools)} tools')
    return len(tools)


if __name__ == '__main__':
    generate_tools_json()
