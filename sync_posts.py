# sync_posts.py
import feedparser
import os
import requests
import json
from datetime import datetime

# Velog API URL
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
API_URL = f'https://v2.velog.io/api/posts/@{VELOG_USERNAME}'

def get_posts():
    print(f"Fetching posts from API: {API_URL}")
    
    try:
        # API 호출
        response = requests.get(API_URL)
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text[:200]}...")  # 응답 내용 확인
        
        if response.status_code == 200:
            posts_data = response.json()
            # github 시리즈 포스트 필터링
            github_posts = [
                post for post in posts_data
                if 'series' in post and post['series'] and 'github' in post['series'].lower()
            ]
            
            for post in github_posts:
                print(f"Found post: {post['title']}")
            
            return github_posts
        else:
            print(f"API request failed with status: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"Error fetching posts: {e}")
        return []

def save_post(post):
    filename = f"posts/{clean_filename(post['title'])}.md"
    print(f"Saving post: {post['title']} to {filename}")
    
    content = f"""---
title: {post['title']}
date: {post.get('created_at', '')}
series: github
link: https://velog.io/@{VELOG_USERNAME}/{post.get('url_slug', '')}
---

{post.get('short_description', '')}
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
    print(f"Found {len(posts)} posts in github series")
    for post in posts:
        save_post(post)
    print("Sync complete!")

if __name__ == '__main__':
    main()