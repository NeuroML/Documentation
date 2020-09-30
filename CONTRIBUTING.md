# Contribution guidelines

- Markdown is preferred to Restructured Text
- Please start each sentence on a new line. This allows for better diffs and
  pull requests.


## Building docs locally

The documentation currently uses Sphinx.
To build the documentation locally, for example, to test before opening Pull Requests, a virtual environment can be used:

  # Create a new virtual environment
  $ python3 -m venv ./.venv
  # Activate the virtual environment
  $ source .venv/bin/activate
  # Install the necessary Python packages
  $ pip install -r requirements.txt
  # Build the docs
  $ make html

This will create the HTML documentation in `build/html`.
You can view the generated documentation by opening the `build/html/index.html` file in your preferred browser.


To deactivate the virtual environment:

  $ deactivate

More information on Python virtual environments can be found in the Python documentation [here](https://docs.python.org/3.9/library/venv.html).
