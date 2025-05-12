# sync_posts.py
import feedparser
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Velog 시리즈 URL
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
SERIES_URL = f'https://velog.io/@{VELOG_USERNAME}/series/github'

def get_posts():
    print(f"Fetching posts from series: {SERIES_URL}")
    
    try:
        # 시리즈 페이지 가져오기
        response = requests.get(SERIES_URL)
        print(f"Response status: {response.status_code}")
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 시리즈의 포스트 링크 찾기
        posts = []
        for article in soup.find_all('article'):
            title = article.find('h2').text if article.find('h2') else ''
            link = article.find('a')['href'] if article.find('a') else ''
            date = article.find('div', {'class': 'date'}).text if article.find('div', {'class': 'date'}) else ''
            
            if title and link:
                posts.append({
                    'title': title,
                    'link': f'https://velog.io{link}',
                    'date': date
                })
                print(f"Found post: {title}")
        
        return posts
        
    except Exception as e:
        print(f"Error fetching series: {e}")
        return []

def save_post(post):
    filename = f"posts/{clean_filename(post['title'])}.md"
    print(f"Saving post: {post['title']} to {filename}")
    
    content = f"""---
title: {post['title']}
date: {post['date']}
link: {post['link']}
series: github
---

[Original Post]({post['link']})
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
    print(f"Found {len(posts)} posts in series")
    for post in posts:
        save_post(post)
    print("Sync complete!")

if __name__ == '__main__':
    main()