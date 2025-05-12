# sync_posts.py
import feedparser
import os
import requests
from datetime import datetime

# Velog RSS 피드 URL
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
RSS_URL = f'https://velog.io/@{VELOG_USERNAME}/rss'

def get_posts():
    print(f"Fetching posts from: {RSS_URL}")
    feed = feedparser.parse(RSS_URL)
    
    # 전체 피드 정보 출력
    print(f"Total posts found: {len(feed.entries)}")
    
    for entry in feed.entries:
        print(f"\nPost title: {entry.title}")
        print(f"Tags: {entry.get('tags', [])}")
        print(f"Categories: {entry.get('categories', [])}")
        print(f"Link: {entry.link}")
        
    # github 시리즈 포스트 필터링
    github_posts = []
    for post in feed.entries:
        # 모든 가능한 메타데이터 확인
        if hasattr(post, 'tags'):
            print(f"Tags for {post.title}: {post.tags}")
        if hasattr(post, 'categories'):
            print(f"Categories for {post.title}: {post.categories}")
        
        # 시리즈 정보가 있는지 확인
        if 'github' in post.link.lower():
            github_posts.append(post)
    
    print(f"\nFound {len(github_posts)} posts in github series")
    return github_posts

def save_post(post):
    filename = f"posts/{clean_filename(post.title)}.md"
    print(f"Saving post: {post.title} to {filename}")
    
    content = f"""---
title: {post.title}
date: {post.published}
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