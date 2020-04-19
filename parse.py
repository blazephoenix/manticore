import os
from datetime import datetime
from markdown2 import markdown

'''
Parser will parse arguments according to selected option.
'''

def Post_parser():

    POSTS = {}

    for md_post in os.listdir('content/default'):
        md_post_path = os.path.join('content', 'default', md_post)        
        with open(md_post_path, 'r') as f:
            POSTS[md_post] = markdown(f.read(), extras=['metadata'])

    POSTS = {
        post: POSTS[post] for post in sorted(POSTS, 
        key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%d %b %Y'), 
        reverse=True)
    }

    return POSTS

def Resume_parser():

    DETAILS = {}

    md_file_path = 'content/resume/resume.md'

    with open(md_file_path, 'r') as f:
        DETAILS = markdown(f.read(), extras=['metadata'])
    
    return DETAILS