# Setting up

## Step 1) Find the original model code

The original code is published on [ModelDB](https://modeldb.science/262670).

## Step 2) Create GitHub and Open Source Brain accounts for sharing the code

### 2a) Sign up to GitHub and Open Source Brain

We signed in to GitHub and OSBv1

### 2b) Create GitHub repository

ModelDB provides GitHub repositories for all its models now.
This model is available on GitHub here: https://github.com/ModelDBRepository/262670.
The Open Source Brain (OSB) organization on GitHub also keeps a "fork" of these repositories to allow users to easily add them to both Open Source Brain v1 and v2.
This fork is here, and is the one that we will work with: https://github.com/OpenSourceBrain/262670.

For the conversion, I (Ankur) created a fork of this repository with a new branch to work in: https://github.com/sanjayankur31/262670.
A pull request work flow was used to submit converted bits back to the repository.

The first step was to re-organise the code to prepare it for conversion.
All the existing code was moved to a new NEURON folder, and a new NeuroML2 folder set up to store the NeuroML version.

### 2c) Create Open Source Brain project

A new project was created on OSBv1 and linked to the OSB repository: https://v1.opensourcebrain.org/projects/locust-mushroom-body.


