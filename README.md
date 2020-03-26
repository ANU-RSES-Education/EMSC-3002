# Set up and run jupyterhub on a DigitalOcean droplet

This repository can build itself into a digital ocean droplet that runs (the littlest) jupyterhub with the underlying dependencies that you specify in a conda environment `yml` file. The configuration of the droplet
is stored in the repository secret variables.

Actions are configured so that the server status is frequently checked:  ![Health check](https://github.com/ANU-RSES-Education/droplet-template/workflows/Health%20check/badge.svg)

This is a template repository that can be copied or forked to run a particular droplet.

## Nbgitpuller

To make a "binder-like" link to a repository on a droplet that you have set up, you can do this:

http://128.199.153.60/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FANU-RSES-Education%2Fdroplet-template&urlpath=tree%2Fdroplet-template%2FStartHere.ipynb&branch=testing


