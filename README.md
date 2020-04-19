# Manticore

A simple, minimal static site generator in Python.

## Getting Started

- Create a virtual environment - `virtualenv venv`
- Run `pip install -r requirements.txt`
- Add posts in markdown format in the content folder.
  - In `content/resume` for resume.
  - In `content/default` for blog posts.
- Check commands with `python build.py --help`

```
Usage: build.py [OPTIONS]

Options:
  -d, --default TEXT  Generate the default blog template
  -r, --resume TEXT   Generate a resume template
  --help              Show this message and exit.
```

- E.g. To generate a blog,
Type `python build.py --default default`

  - An `output` folder will be created with the markdown files in `content/default`
  - The directory structure in the `output` folder

   ```
   \output
    \posts
     home.html
   ```

The process is similar but a little easier for generating a resume since it only creates one page.

### Prerequisites

- Python 3.6 or higher.

## Deployment

Deployment solutions are currently being worked on. Deployment with Netlify CLI could be available in upcoming releases.

## Built With

* [Markdown2](https://github.com/trentm/python-markdown2) - A fast and complete Python implementation of Markdown.
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - A modern and designer-friendly templating language for Python.
* [Click](https://click.palletsprojects.com/en/7.x/) - A Python package for creating beautiful command line interfaces.
* [Skeleton CSS](https://github.com/dhg/Skeleton) - A Dead Simple, Responsive Boilerplate for Mobile-Friendly Development 
* [Normalize CSS](https://necolas.github.io/normalize.css/) - Normalize.css makes browsers render all elements more consistently and in line with modern standards

## Contributing

Pull requests are welcome.

## Versioning

Currently on 1.0.0

## Authors

* **Tanmay Naik** - *Initial work* - [Blazephoenix](https://github.com/Blazephoenix)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgement

- Normalize CSS - [Necolas](https://github.com/necolas)
- Skeleton CSS - [Dave Gamache](https://github.com/dhg)
- Jinja2 and Click - [Pallets Projects](https://github.com/pallets)
- Markdown2 - [Trent Mick](https://github.com/trentm)

### Upcoming feature releases (probably):
- [ ] Custom category/tags.
- [ ] Other static site templates (portfolio, landing page)
