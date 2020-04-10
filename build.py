import render, parse
import logging

logging.basicConfig(level = logging.INFO)

if __name__ == "__main__":
    try:
        render.Render(parse.Parser())
        logging.info(" Build successful. Check your output folder.")
    except:
        logging.exception(" Build failed :(")