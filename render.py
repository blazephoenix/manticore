import os
from jinja2 import Environment, PackageLoader
from parse import POSTS

env = Environment(loader=PackageLoader('render', 'templates'))
home_temp = env.get_template('home.html')
post_temp = env.get_template('post.html')

posts_mdata = [POSTS[post].metadata for post in POSTS]
# tags = [post['tags'] for post in posts_mdata]
home_html = home_temp.render(posts=posts_mdata)

with open('output/home.html', 'w') as file:
    file.write(home_html)

#FOR INDIVIDUAL POSTS///////////////////////////////////////
for post in POSTS:
    post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date'],
    }

    post_html = post_temp.render(post=post_data)

    post_file_path = 'output/posts/{slug}.html'.format(slug=post_metadata['slug'])

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html)

