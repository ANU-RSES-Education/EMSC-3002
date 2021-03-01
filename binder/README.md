# Notes for binder deployment

This repository is set up to manage it's own jupyterhub but it can also run on an existing environment like binder.

In that case, it is necessary to populate this folder with build instructions for binder. That could be a dockerfile or a requirement.txt file for pip or a conda environment. 

It may be fine to make a link to the conda_packages file in the home directory but, if you need a different setup, this is the place to do it. 

For information see ... on mybinder.org