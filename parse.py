import os
from datetime import datetime
from markdown2 import markdown

def Parser():

    POSTS = {}

    for md_post in os.listdir('content'):
        md_post_path = os.path.join('content', md_post)
        
        with open(md_post_path, 'r') as f:
            POSTS[md_post] = markdown(f.read(), extras=['metadata'])

    POSTS = {
        post: POSTS[post] for post in sorted(POSTS, 
        key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%d %b %Y'), 
        reverse=True)
    }

    return POSTS