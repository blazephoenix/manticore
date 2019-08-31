from jinja2 import Environment, PackageLoader
from render import POSTS

env = Environment(loader=PackageLoader('render', 'templates'))
home_temp = env.get_template('home.html')
post_temp = env.get_template('post.html')

posts_mdata = [POSTS[post].metadata for post in POSTS]
home_html = home_template.render(posts=posts_mdata)

