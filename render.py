import os
from pathlib import Path
from jinja2 import Environment, PackageLoader
from parse import Resume_parser, Post_parser

class Render:

    """
    
    Renders the HTML page according to the arguments provided by build.py.

    """

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=PackageLoader('render', 'templates'))

    def Render_posts(self, posts):
            POSTS = posts

            home_temp = self.env.get_template('default/home.html')
            post_temp = self.env.get_template('default/post.html')

            posts_mdata = [POSTS[post].metadata for post in POSTS]
            home_html = home_temp.render(posts=posts_mdata)

            if Path(os.path.join(self.ROOT_DIR, 'output', 'home.html')).is_file():
                with open('output/home.html', 'w') as file:
                    file.write(self.env.get_template('home.html').render(posts=posts_mdata))
            else:
                os.makedirs(os.path.join(self.ROOT_DIR, 'output'))

                with open('output/home.html', 'w') as file:
                    file.write(home_html)


            for post in POSTS:
                post_metadata = POSTS[post].metadata

                post_data = {
                    'blog': post_metadata['blog'],
                    'content': POSTS[post],
                    'title': post_metadata['title'],
                    'date': post_metadata['date'],
                }

                post_html = post_temp.render(post=post_data)

                post_file_path = 'output/posts/{slug}.html'.format(slug=post_metadata['slug'])

                if Path(os.path.join(self.ROOT_DIR, post_file_path)).is_file():
                    with open(post_file_path, 'w') as file:
                        file.write(self.env.get_template('post.html').render(post=post_data))
                else:
                    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
                    
                    with open(post_file_path, 'w') as file:
                        file.write(post_html)
    
    def Render_resume(self, details):    
            DETAILS = details

            resume_temp = self.env.get_template('resume/home.html')

            resume_data = {
                'name': details.metadata['name'],
                'designation': details.metadata['designation'],
                'address': details.metadata['address'],
                'phone': details.metadata['phone'],
                'email':details.metadata['email'],
                'content': details
            }

            resume_html = resume_temp.render(details=resume_data)

            if Path(os.path.join(self.ROOT_DIR, 'output', 'resume.html')).is_file():
                with open('output/resume.html', 'w') as file:
                    file.write(self.env.get_template('resume/home.html').render(details=resume_data))
            else:
                os.makedirs(os.path.join(self.ROOT_DIR, 'output'))

                with open('output/resume.html', 'w') as file:
                    file.write(resume_html)