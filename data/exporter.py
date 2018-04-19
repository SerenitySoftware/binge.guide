#!/usr/bin/env python3

import csv
import jinja2
from shutil import copyfile
import glob

drafts = glob.glob('../drafts/*.md')
reviews = glob.glob('../content/shows/*.md')

with open('shows.csv') as shows_data:
    shows = csv.reader(shows_data)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = env.get_template('template.md')

    for show in shows:
        slug = show[1]
        title = show[2]
        webaddress = show[3]
        producer = show[4]
        creator = show[5]
        pilot = show[6]
        finale = show[7]
        seasons = show[8]
        episodes = show[9]
        hours = show[10]
        IMDBrating = show[11]
        IMDBratingcount = show[12]
        Amazonrating = show[13]
        iTunesrating = show[14]
        Metacriticaverage = show[15]
        Listofproviders = show[16]
        NetflixURL = show[17]
        HuluURL = show[18]
        AmazonURL = show[19]
        iTunesURL = show[20]
        VuduURL = show[21]
        HBOURL = show[22]
        GoogleplayURL = show[23]

        if slug == "Slug":
            continue

        output = template.render(slug=slug, title=title, pilot=pilot,
                                 webaddresss=webaddress, producer=producer,
                                 creator=creator, finale=finale,
                                 seasons=seasons, episodes=episodes,
                                 hours=hours, IMDBrating=IMDBrating,
                                 IMDBratingcount=IMDBratingcount,
                                 Amazonrating=Amazonrating,
                                 iTunesrating=iTunesrating,
                                 Metacriticaverage=Metacriticaverage,
                                 Listofproviders=Listofproviders,
                                 NetflixURL=NetflixURL, HuluURL=HuluURL,
                                 AmazonURL=AmazonURL, iTunesURL=iTunesURL,
                                 VuduURL=VuduURL, HBOURL=HBOURL,
                                 GoogleplayURL=GoogleplayURL)

        try:
            with open("../drafts/{0}.md".format(slug), "x") as content:
                content.write(output)
                for review in reviews:
                    if (slug) in review:
                        with open(review, 'r') as writeup:
                            writeuplines = []
                            for line in writeup:
                                if "Synopsis" in line:
                                    writeuplines.append('\n' + '\n' + line)
                                    for line in writeup:
                                        writeuplines.append(line)
                            writecon = ("".join(writeuplines))
                            content.write('\n' + writecon)
                    else:
                        continue
        except Exception:
            for draft in drafts:
                if (slug) in draft:
                    with open(draft, 'r+') as existing:
                        draftcon = existing.read()
                        for review in reviews:
                            if slug in review:
                                with open(review, 'r') as writeup:
                                    writeuplines = []
                                    for line in writeup:
                                        if "Synopsis" in line:
                                            writeuplines.append(
                                                '\n' + '\n' + line)
                                            for line in writeup:
                                                writeuplines.append(line)
                                    writecon = ("".join(writeuplines))
                                    if writecon in draftcon:
                                        continue
                                    else:
                                        existing.write(writecon)

                            else:
                                continue
                else:
                    continue

        copyfile("./template.png",
                 "../theme/binge/static/images/shows/{0}.png".format(slug))
