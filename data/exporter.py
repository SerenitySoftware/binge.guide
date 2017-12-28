#!/usr/bin/env python3

import csv
import jinja2
from shutil import copyfile


with open('shows.csv') as shows_data:
    shows = csv.reader(shows_data)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = env.get_template('template.md')

    for show in shows:
        slug = show[0]
        title = show[1]
        pilot = show[4]

        if slug == "Slug":
            continue

        output = template.render(slug=slug, title=title, pilot=pilot)
        with open("../content/{0}.md".format(slug), "w") as content:
            content.write(output)

        copyfile("./template.png", "../theme/binge/static/images/shows/{0}.png".format(slug))
