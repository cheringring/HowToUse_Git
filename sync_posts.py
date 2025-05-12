# sync_posts.py
import os
import requests
import json
from datetime import datetime

# Velog GraphQL API endpoint
VELOG_USERNAME = os.getenv('VELOG_USERNAME', 'cheringring')
API_URL = 'https://v2.velog.io/graphql'

def get_posts():
    print(f"Fetching posts for user: {VELOG_USERNAME}")
    
    # GraphQL 쿼리 수정 - body 내용 추가
    query = """
    query Posts($username: String) {
      posts(username: $username) {
        id
        title
        url_slug
        created_at
        body
        series {
          name
        }
        tags
        short_description
      }
    }
    """
    
    try:
        response = requests.post(
            API_URL,
            json={
                'query': query,
                'variables': {'username': VELOG_USERNAME}
            }
        )
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'posts' in data['data']:
                # github 시리즈 포스트 필터링
                github_posts = [
                    post for post in data['data']['posts']
                    if post.get('series') and post['series'].get('name', '').lower() == 'github'
                ]
                
                for post in github_posts:
                    print(f"Found post: {post['title']}")
                
                return github_posts
            else:
                print("No posts data in response")
                return []
        else:
            print(f"API request failed with status: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"Error fetching posts: {e}")
        print(f"Full error: {str(e)}")
        return []

def save_post(post):
    # url_slug를 사용하여 파일명 생성
    filename = f"posts/{post['url_slug']}.md"
    print(f"Saving post: {post['title']} to {filename}")
    
    # 메타데이터와 본문 내용을 포함한 마크다운 파일 생성
    content = f"""---
title: {post['title']}
date: {post['created_at']}
series: github
tags: {', '.join(post.get('tags', []))}
link: https://velog.io/@{VELOG_USERNAME}/{post['url_slug']}
---

{post.get('body', '')}

---
원본 포스트: https://velog.io/@{VELOG_USERNAME}/{post['url_slug']}
"""
    
    os.makedirs('posts', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved post: {filename}")

def main():
    print("Starting sync process...")
    posts = get_posts()
    print(f"Found {len(posts)} posts in github series")
    for post in posts:
        save_post(post)
    print("Sync complete!")

if __name__ == '__main__':
    main()