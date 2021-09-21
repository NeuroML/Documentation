# Contribution guidelines

- Jupyter-book supports [multiple content types](https://jupyterbook.org/file-types/index.html). Their flavour of Markdown is preferred.
- Please start each sentence on a new line in the documentation. This allows
  for better diffs and pull requests.


## Building docs locally

The documentation currently uses [Jupyter-book](https://jupyterbook.org/).

Please note that Jupyterbook does not yet support Sphinx v4, and Sphinx v3 does not run correctly with Python 3.10.
Therefore, until Jupyterbook is updated to support Sphinx v4, please use Python `<= 3.9` for your virtual environment.

To build the documentation locally, to test before opening Pull Requests for example, a virtual environment can be used:

```

  # Create a new virtual environment
  $ python3 -m venv ./.venv
  # Activate the virtual environment
  $ source .venv/bin/activate
  # Install the necessary Python packages
  $ pip install -r requirements-book.txt
  # Build the docs
  $ jupyter-book build ./source
  # This will create the HTML files in ./source/_build/html
```


To deactivate the virtual environment:

```

  $ deactivate
```

More information on Python virtual environments can be found in the Python documentation [here](https://docs.python.org/3.9/library/venv.html).

## Publishing the book

The book is published using GitHub pages, using the `ghp-import` tool.

```

  # Use ghp-import
  $ ghp-import -n -p -f ./source/_build/html
```

This will import the HTML files built by `jupyter-book` to the `gh-pages` branch.
More information on this can be found in the [official documentation](https://jupyterbook.org/publish/gh-pages.html).

A helper script `./build-helper.sh` is present in the repository to assist with these steps.


## Updating schema pages

The schema pages are generated using the script provide in the scripts/schemas directory.
This uses a copy of the NeuroML2 repository to parse the XML core type definitions to generate the myAST docs using Jinja templates.
It also goes through the examples to extract XML example snippets.
Finally, it inspects the libNeuroML Python API to include constructor definitions where they are available.

Please remember to commit the newly generated schema doc files after running the script.
