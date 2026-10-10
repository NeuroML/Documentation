(devdocs:devsop)=
# Contribution guidelines

Thank you for your interest in contributing to NeuroML.
Welcome!

This page documents the contribution guidelines for all NeuroML related repositories.

Please do remember that these are *guidelines* but not rules that must be strictly followed.
We think these are reasonable ideas to follow and they help us maintain a high code quality while making it easier and more efficient for all of us to work together.
However, there may be cases where they can not be followed, and that's fine too.

(devdocs:devsop:coc)=
## Code of conduct

All NeuroML projects are governed by the {ref}`Code of Conduct <coc>`.
By participating, you are expected to uphold this code.
Please report unacceptable behaviour to the moderators of the communication channel you are in.

(devdocs:devsop:repos)=
## Structure of repositories

- All NeuroML repositories use the [Git](https://git-scm.com/) version control system.
- Contributions are made using [pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
- Each NeuroML software tool resides in its own GitHub repository under the [NeuroML GitHub Organization](https://github.com/NeuroML), apart from [libNeuroML](https://github.com/NeuralEnsemble/libNeuroML) which is developed in collaboration with the [NeuralEnsemble community](http://neuralensemble.org/) and so lives under their GitHub organization.
- LEMS repositories are housed under the [LEMS GitHub Organization](https://github.com/LEMS).

You can find links to these on the respective pages for each {ref}`software tool <userdocs:software>`.

The NeuroML standard itself (schema and ComponentType definitions) is housed in its own repository [here](https://github.com/NeuroML/NeuroML2).

(devdocs:devsop:repos:zenhub)
### Kanban board on Zenhub

An overview of the various repositories, tasks, issues, and so on can be seen on the [NeuroML Kanban board on Zenhub](https://app.zenhub.com/workspaces/neuroml-development-605c92c7c670460016e497ab/board?filterLogic=any&repos=7225220,6579766,7225426,299352189,78101103,129064858,8460738,6171449,6171626,27832592,78100679,6171646,3740176,4614078,7146844,4326891&showPipelineDescriptions=false).


(devdocs:devsop:versioning)=
## Versioning

All NeuroML repositories (including the standard) follow [Semantic versioning](https://semver.org/).
This means that the version string consists of three components: `MAJOR.MINOR.PATCH`:

- the MAJOR version is incremented when incompatible API changes are made,
- the MINOR version is incremented when functionality is added in a backwards compatible manner, and
- the PATCH version is incremented when backwards compatible bug fixes are made.

(devdocs:devsop:branches)=
## Git branches

- Please develop against the `development` branch in all repositories.
  This branch is merged into `master` via a pull request when a new release is made.
  This ensures that all tests are run at each step to verify correctness.
  As a result, the `master` branch of all repositories holds the stable version of the standard and tools, while the `development` branch holds the next, unstable version that is being worked upon.

- For branch names, please consider using the [Git flow](https://nvie.com/posts/a-successful-git-branching-model/) naming convention (not mandatory but strongly suggested):

  - prefix feature branches with `feat/` or `enh/` (for enhancement)
  - prefix bugfix branches with `bugfix/` or `fix/`
  - pull requests addressing specific tickets may also mention them in the branch name. E.g., `bugfix/issue-22`.

(devdocs:devsop:commits)=
## Git commits

Git commit messages are extremely important because they allow us to nicely track the complete development history of the project.
Here are some guidelines on writing good commit messages:

- Each commit should ideally only address one issue.
  It should be self-contained (should not group together lots of changes).
  Tip: use `git add -p` to break your work down into logical, small commits).
- Write good commit messages.
  Read [this post](https://chris.beams.io/posts/git-commit/) to see how to write meaningful, useful commit messages and why they are important.
- We strongly suggest using the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) specification.
  In short:

  - Each commit is of the form `<type>[optional scope]: description`, followed by the text body of the commit after a blank line, and then any optional references etc. as footer.
  - The `type` can be one of: `fix`, `feat`, `build`, `chore`, `ci`, `docs`, `refactor`, `perf`, `test`, and so on depending on what the commit is doing.
  - Any backwards incompatible, breaking change must be clearly noted in the commit using the `BREAKING CHANGE` phrase.
    This corresponds to a major version update (as noted above in the versioning section).

(devdocs:devsop:style:java)=
## Code style: Java

TODO

(devdocs:devsop:style:python)=
## Code style: Python

- While Python 2 is still supported even though it is [no longer supported by the Python community](https://pythonclock.org), given that most Python modules (numpy/scipy/matplotlib/sphinx) have dropped support for this deprecated Python version, NeuroML will also drop support in the near future.
  Therefore, we strongly suggest using Python 3.
- For Python repositories, please use [Black](https://black.readthedocs.io/) to format your code before committing and submitting a pull request.
- We also strongly suggest linting using [flake8](https://flake8.pycqa.org/).
- Please use [type hints](https://docs.python.org/3/library/typing.html?highlight=type%20hint) in your code and run [mypy](https://mypy.readthedocs.io/en/stable/) to test it for correctness.
  You can see the [mypy cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet.html) to quickly see how to do this.
  Since NeuroML is currently still supporting Python 2, we use the Python 2 style to maintain compatibility (this also works with Python 3).
- Deprecations should be clearly noted in the code, and in the commit message.
  You may use the [Sphinx deprecated directive](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated) along with the Python [DeprecationWarning](https://docs.python.org/3/library/exceptions.html#DeprecationWarning), for example.

(devdocs:devsop:docs)=
## Documentation

All tools include their own documentation in their repositories.
Please feel free to improve this documentation and submit pull requests.

When contributing fixes and enhancements, please remember to document your classes/functions and code in general.
Not only does this allow others to understand your code, it also allows us to auto-generate documentation using various tools.

- For the Java repositories, please use the standard [Javadoc](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html) syntax.
- For the Python repositories, please document your code using the standard [Sphinx reStructuredText](https://www.sphinx-doc.org) system.
  For functions and so on, you can use the provided [fields](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html?#python-signatures).

Where applicable, please add examples and so on to the software documentation to ensure that users can find the information quickly.
Additionally, please remember to consider if this primary NeuroML documentation here needs to be updated.

Please use [Semantic Line Breaks](https://sembr.org/) wherever possible.

(devdocs:devsop:testing)=
## Testing

- Before submitting a pull request, please run the various tests to confirm your changes.
  You can see how they are run in the various GitHub workflow files (in the `.github/workflows/` folder in each repository).
  They will be run on all pull requests automatically so you can also verify your changes there.
- For a new feature addition, please remember to include a unit test.
- For a bug fix, please include a regression test.
