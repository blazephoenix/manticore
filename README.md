# Manticore

Manticore is a static site generator using Python.

It uses Markdown2 and the jinja2 templating engine to render static pages as output.
A lot of work remains to be done but the basic functionality is all there.

### To-do:
- [ ] Custom category and tags.
- [x] CLI application.
-  [x] Other static site templates (resume, portfolio, landing page, etc.).

### Steps to get started: 

- Install `requirements.txt`
- Add posts in markdown format in the content folder.
- Check commands with `python build.py --help`

```
Usage: build.py [OPTIONS]

Options:
  -d, --default TEXT  Generate the default blog template
  -r, --resume TEXT   Generate a resume template
  --help              Show this message and exit.
```