#!/usr/bin/env python3
"""
Get list of NeuroML contributors

File: get-contributors.py

Copyright 2021 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import requests
import textwrap
from datetime import date


todays_date = date.today().strftime("%d/%m/%y")
baseurl = "https://api.github.com/"
# You need a GitHub token
token = ""
headers = {"Authorization": "token {}".format(token)}
data = requests.get(baseurl + "orgs/NeuroML/repos", headers=headers)
neuroml_repos = data.json()

data = requests.get(baseurl + "orgs/LEMS/repos", headers=headers)
lems_repos = data.json()


extra_repos_list = ['NeuralEnsemble/libNeuroML']
extra_repos = []
for er in extra_repos_list:
    data = requests.get(baseurl + "repos/" + er, headers=headers)
    extra_repos.append(data.json())

master_list = {}
all_repos = neuroml_repos + lems_repos + extra_repos
for repo in all_repos:
    contributors_url = repo['contributors_url']
    data = requests.get(contributors_url, headers=headers)
    contributors = data.json()
    for contributor in contributors:
        # they'll get overwritten but we still only get each user once
        if "dependabot" not in contributor['login']:
            master_list[contributor['login']] = contributor['html_url']

# Write docs page
docs_page = "../../source/NeuroMLOrg/Contributors.md"
with open(docs_page, 'w') as f:
    print(textwrap.dedent(
        """\
        (neuromlorg:contributors)=
        # NeuroML contributors

        This page lists contributors to the various NeuroML and related repositories, listed in no particular order.
        It is generated periodically, most recently on {}.

        """.format(todays_date)), file=f)
    # A blank line
    print("", file=f)

    for key, val in master_list.items():
        print("- [@{}]({})".format(key, val), file=f)

    print(textwrap.dedent(
        """
        ## Repositories

        """
    ), file=f)

    for repo in all_repos:
        print("- [{}]({})".format(repo['full_name'], repo['html_url']), file=f)
