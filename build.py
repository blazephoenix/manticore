import parse
import logging
import click
from render import Render

logging.basicConfig(level = logging.INFO)

@click.command()
@click.option('--default', '-d', help='Generate the default blog template')
@click.option('--resume','-r', help='Generate a resume template')

def build(default, resume):
    Renderer = Render()
    if default:
        try:
            posts = parse.Post_parser()
            Renderer.Render_posts(posts)
            logging.info(" Build successful. Check your output folder.")
        except:
            logging.exception(" Build failed :(")           
    elif resume:
        try:
            details = parse.Resume_parser()
            Renderer.Render_resume(details)
            logging.info(" Build successful. Check your output folder.")
        except:
            logging.exception(" Build failed :(")

if __name__ == "__main__":
    build()