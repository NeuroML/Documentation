#!/bin/bash

# Copyright 2020 Ankur Sinha
# Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
# File : build-helper.sh
#
# Shell script to build and publish the book when needed

VENV_DIR="$(readlink -f .venv)"
VENV_ACTIVATE_SCRIPT="$VENV_DIR/bin/activate"
VENV_STATUS="inactive"

if [[ -z "${PYTHON}" ]]
then
    PYTHON="python3"
fi

function enable_virtenv() {
    if [[ -z "${VIRTUAL_ENV}" ]];
    then
        echo "No virtual environment active."
    else
        # Check if it is the correct virtual env
        if [[ "$VIRTUAL_ENV" == "$VENV_DIR" ]];
        then
            echo "Virtual env in $VENV_DIR already active."
            VENV_STATUS="active"
        else
            echo "Another virtual env is active:"
            echo "Deactivating $VIRTUAL_ENV".
            deactivate
        fi
    fi

    if [[ "$VENV_STATUS" != "active" ]]
    then
        if  [[ -e "$VENV_ACTIVATE_SCRIPT" ]];
        then
            echo "Activating virtual env in $VENV_DIR."
            source "$VENV_ACTIVATE_SCRIPT"
            VENV_STATUS="active"
        else
            echo "No virtual environment found in $VENV_DIR."
            echo "Creating new."
            create_virtenv
            VENV_STATUS="active"
        fi
    fi
}

function create_virtenv() {
    if [[ -e "$VENV_ACTIVATE_SCRIPT" ]];
    then
        echo "Virtual environment activation script already exists: $VENV_ACTIVATE_SCRIPT."
        echo "Please delete it and re-run to create a new one."
    else
        echo "Setting up new virtual environment in $VENV_DIR."
        $PYTHON -m venv "$VENV_DIR"

        echo "Activating virtual environment."
        source "$VENV_ACTIVATE_SCRIPT"

        echo "Installing required dependencies in virtual environment."
        pip install wheel
        pip install -r requirements-book.txt
        # pip install -r requirements.txt

        echo
        echo "Virtual environment created."
        echo "Activate using:"
        echo "source $VENV_ACTIVATE_SCRIPT"
    fi
}

function build_book() {
    enable_virtenv
    echo "Building book."
    jupyter-book build ./source
}

function publish_book() {
    enable_virtenv
    echo "Publishing book."
    ghp-import -c "docs.neuroml.org" -n -p -f ./source/_build/html
}

function clean_book() {
    enable_virtenv
    echo "Cleaning book."
    jupyter-book clean ./source
}

function watch_and_build () {
    if ! command -v inotifywait > /dev/null
    then
        echo "inotifywait command could not be found. Please install inotify-tools."
    else
        build_book
        while true
        do
            echo "Watching source dir for changes and re-building as required. Use Ctrl C to stop."
            inotifywait -q -e modify,create,delete,move -r source && echo "Change detected, rebuilding.." && build_book
        done
    fi
}

build_pdf () {
    enable_virtenv
    echo "Building book PDF using LaTeX."
    rm -rf ./source/_build/latex/*
    jupyter-book build ./source --builder pdflatex

    echo "Installing book to _static directory"
    mv source/_build/latex/neuroml-documentation.pdf source/_static/files/
}

function usage() {
    echo "$0: helper script to work with docs locally"
    echo "OPTIONS:"
    echo
    echo "-h: print help message"
    echo "-c: create new virtual environment in $VENV and install packages."
    echo "-b: build book"
    echo "-f: build pdf (using LaTeX)"
    echo "-w: watch source directory for changes and build as necessary, requires inotifywait"
    echo "-p: publish book to GitHub pages (requires commit access to repo)"
    echo "-X: clean book"
}

if [ $# -lt 1 ]
then
    usage
    exit 1
fi

# parse options
while getopts "bpchwfX" OPTION
do
    case $OPTION in
        b)
            build_book
            exit 0
            ;;
        w)
            watch_and_build
            exit 0
            ;;
        f)
            build_pdf
            exit 0
            ;;
        p)
            publish_book
            exit 0
            ;;
        c)
            create_virtenv
            exit 0
            ;;
        X)
            clean_book
            exit 0
            ;;
        h)
            usage
            exit 0
            ;;
        ?)
            usage
            exit 1
            ;;
    esac
done
