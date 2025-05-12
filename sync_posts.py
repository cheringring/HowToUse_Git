# sync_posts.py
import feedparser
import os
import requests
from datetime import datetime

# Velog 특정 시리즈 RSS 피드 URL
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
SERIES_NAME = 'github'
RSS_URL = f'https://velog.io/@{VELOG_USERNAME}/series/{SERIES_NAME}?format=rss'

def get_posts():
    print(f"Fetching posts from: {RSS_URL}")  # 디버그 출력
    feed = feedparser.parse(RSS_URL)
    print(f"Found {len(feed.entries)} posts")  # 디버그 출력
    return feed.entries

def save_post(post):
    filename = f"posts/{clean_filename(post.title)}.md"
    print(f"Saving post: {post.title} to {filename}")  # 디버그 출력
    
    content = f"""---
title: {post.title}
date: {post.published}
series: GitHub
link: {post.link}
---

{post.description}
"""
    
    os.makedirs('posts', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved post: {filename}")  # 디버그 출력

def clean_filename(title):
    return title.replace('/', '-').replace('\\', '-')

def main():
    print("Starting sync process...")  # 디버그 출력
    posts = get_posts()
    for post in posts:
        save_post(post)
    print("Sync complete!")  # 디버그 출력

if __name__ == '__main__':
    main()
