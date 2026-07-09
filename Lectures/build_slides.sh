#! /usr/bin/env bash

# This will build all the reveal.md files it finds in the root directory
# These files are also ignored by the jupyterbook script. 


if ! command -v reveal-md &> /dev/null
then
    # Pinned: reveal-md is unmaintained (last release 6.1.4). Pin so an npm change
    # cannot break slide generation mid-term. reveal-md is being replaced by MkSlides
    # in the Jupyter Book 2 migration; this pin keeps the current site stable until then.
    npm install -g reveal-md@6.1.4
fi

mkdir -p static_slides
reveal-md  --static static_slides/slideshows \
           --theme https://anu-rses-education.github.io/EMSC-3002/slideshows/css/anu.css \
           --highlight-theme github  \
           --glob '**/*.reveal.md' \
           --separator '<--o-->' \
           --vertical-separator '<--v-->' \
           --static-dirs \
css,\
movies,\
images,\
data,\
Module-ii-Figures-Structural-Geology-And-Crustal-Deformation,\
Module-iii-Theory,\
Module-iv-Brittle-Deformation,\
Module-v-Ductile-Deformation
