# sync_posts.py
import feedparser
import os
import requests
from datetime import datetime
import re

# Velog 특정 시리즈 RSS 피드 URL
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
SERIES_NAME = 'github'
RSS_URL = f'https://velog.io/@{VELOG_USERNAME}/series/{SERIES_NAME}?format=rss'

def clean_filename(title):
    # 파일명으로 사용할 수 없는 문자 처리
    # Windows와 Unix 모두에서 안전하게 사용할 수 있는 파일명 생성
    return title.replace('/', '-').replace('\\', '-')

def get_posts():
    feed = feedparser.parse(RSS_URL)
    return feed.entries

def save_post(post):
    # 원래 제목 그대로 사용 (파일명으로 사용할 수 없는 문자만 처리)
    filename = f"posts/{clean_filename(post.title)}.md"
    
    # 포스트 내용 구성
    content = f"""---
title: {post.title}
date: {post.published}
series: GitHub
link: {post.link}
---

{post.description}
"""
    
    # posts 디렉토리 생성
    os.makedirs('posts', exist_ok=True)
    
    # 파일 저장
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"저장됨: {post.title}")

def main():
    posts = get_posts()
    for post in posts:
        save_post(post)

if __name__ == '__main__':
    main()