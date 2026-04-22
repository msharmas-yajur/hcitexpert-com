#!/usr/bin/env python3
"""Convert WordPress.com XML export to Jekyll posts and pages."""

import xml.etree.ElementTree as ET
import os
import re
import sys
from datetime import datetime

NS = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
}

AUTHOR_MAP = {
    'thehcitexpertsblog': 'Team HCITExperts',
    'hcitexpert': 'Manish Sharma',
    'anushaashwin': 'Anusha Ashwin',
    'santoshshevade': 'Santosh Shevade',
    'digitalhealthexperts': 'DigitalHealth Experts',
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text


def escape_yaml(text):
    if not text:
        return '""'
    text = str(text).replace('\\', '\\\\').replace('"', '\\"')
    if any(c in text for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', "'"]):
        return f'"{text}"'
    return text


def get_text(element, tag, ns=NS):
    el = element.find(tag, ns)
    if el is not None and el.text:
        return el.text.strip()
    return ''


def parse_date(pub_date):
    formats = [
        '%a, %d %b %Y %H:%M:%S %z',
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
    ]
    for fmt in formats:
        try:
            return datetime.strptime(pub_date.strip(), fmt)
        except ValueError:
            continue
    return None


def get_categories_tags(item):
    categories = []
    tags = []
    for cat in item.findall('category'):
        domain = cat.get('domain', '')
        nicename = cat.get('nicename', '')
        text = cat.text or ''
        if domain == 'category':
            categories.append(text.strip())
        elif domain == 'post_tag':
            tags.append(text.strip())
    return categories, tags


def write_post(item, output_dir):
    title = get_text(item, 'title') or 'Untitled'
    pub_date = get_text(item, 'pubDate') or get_text(item, 'wp:post_date')
    content = get_text(item, 'content:encoded')
    excerpt = get_text(item, 'excerpt:encoded')
    author_login = get_text(item, 'dc:creator')
    author = AUTHOR_MAP.get(author_login, author_login)
    wp_slug = get_text(item, 'wp:post_name')
    link = get_text(item, 'link')

    dt = parse_date(pub_date) if pub_date else None
    if dt:
        date_str = dt.strftime('%Y-%m-%d')
        date_full = dt.strftime('%Y-%m-%d %H:%M:%S %z')
    else:
        date_str = '1970-01-01'
        date_full = '1970-01-01 00:00:00 +0000'

    slug = wp_slug if wp_slug else slugify(title)
    filename = f"{date_str}-{slug[:80]}.md"
    filepath = os.path.join(output_dir, filename)

    categories, tags = get_categories_tags(item)

    cats_yaml = ''
    if categories:
        cats_list = '\n'.join(f'  - {escape_yaml(c)}' for c in categories)
        cats_yaml = f'categories:\n{cats_list}'

    tags_yaml = ''
    if tags:
        tags_list = '\n'.join(f'  - {escape_yaml(t)}' for t in tags)
        tags_yaml = f'tags:\n{tags_list}'

    front_matter_parts = [
        f'title: {escape_yaml(title)}',
        f'date: {date_full}',
        f'author: {escape_yaml(author)}',
    ]
    if excerpt:
        front_matter_parts.append(f'excerpt: {escape_yaml(excerpt[:200])}')
    if link:
        front_matter_parts.append(f'original_url: {link}')
    if cats_yaml:
        front_matter_parts.append(cats_yaml)
    if tags_yaml:
        front_matter_parts.append(tags_yaml)

    front_matter = '\n'.join(front_matter_parts)

    post_content = f"---\n{front_matter}\n---\n\n{content}\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(post_content)

    return filename


def write_page(item, output_dir):
    title = get_text(item, 'title') or 'Untitled'
    content = get_text(item, 'content:encoded')
    wp_slug = get_text(item, 'wp:post_name')
    link = get_text(item, 'link')
    pub_date = get_text(item, 'pubDate') or get_text(item, 'wp:post_date')

    dt = parse_date(pub_date) if pub_date else None
    date_full = dt.strftime('%Y-%m-%d %H:%M:%S %z') if dt else '2015-01-01 00:00:00 +0000'

    slug = wp_slug if wp_slug else slugify(title)
    filename = f"{slug[:80]}.md"
    filepath = os.path.join(output_dir, filename)

    front_matter_parts = [
        f'title: {escape_yaml(title)}',
        f'date: {date_full}',
        f'permalink: /{slug}/',
    ]
    if link:
        front_matter_parts.append(f'original_url: {link}')

    front_matter = '\n'.join(front_matter_parts)
    page_content = f"---\n{front_matter}\n---\n\n{content}\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_content)

    return filename


def main():
    xml_file = sys.argv[1] if len(sys.argv) > 1 else 'wordpress.xml'
    posts_dir = sys.argv[2] if len(sys.argv) > 2 else '_posts'
    pages_dir = sys.argv[3] if len(sys.argv) > 3 else '_pages'

    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(pages_dir, exist_ok=True)

    print(f"Parsing {xml_file}...")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    channel = root.find('channel')
    items = channel.findall('item')

    posts_written = 0
    pages_written = 0
    skipped = 0

    for item in items:
        post_type = get_text(item, 'wp:post_type')
        status = get_text(item, 'wp:status')

        if status != 'publish':
            skipped += 1
            continue

        if post_type == 'post':
            filename = write_post(item, posts_dir)
            posts_written += 1
            print(f"  [post] {filename}")
        elif post_type == 'page':
            filename = write_page(item, pages_dir)
            pages_written += 1
            print(f"  [page] {filename}")
        else:
            skipped += 1

    print(f"\nDone!")
    print(f"  Posts written: {posts_written}")
    print(f"  Pages written: {pages_written}")
    print(f"  Skipped (drafts/other): {skipped}")


if __name__ == '__main__':
    main()
