import feedparser
import os
import requests
from datetime import datetime

# Velog RSS 피드 URL 수정
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
RSS_URL = f'https://velog.io/@{VELOG_USERNAME}/rss'  # 전체 RSS 피드를 가져온 후 필터링

def get_posts():
    print(f"Fetching posts from: {RSS_URL}")
    feed = feedparser.parse(RSS_URL)
    # github 시리즈의 포스트만 필터링
    github_posts = [post for post in feed.entries if 'github' in post.get('tags', [''])[0].lower()]
    print(f"Found {len(github_posts)} posts in github series")
    return github_posts

def save_post(post):
    filename = f"posts/{clean_filename(post.title)}.md"
    print(f"Saving post: {post.title} to {filename}")
    
    content = f"""---
title: {post.title}
date: {post.published}
series: github
link: {post.link}
---

{post.description}
"""
    
    os.makedirs('posts', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved post: {filename}")

def clean_filename(title):
    return title.replace('/', '-').replace('\\', '-')

def main():
    print("Starting sync process...")
    posts = get_posts()
    for post in posts:
        save_post(post)
    print("Sync complete!")

if __name__ == '__main__':
    main()