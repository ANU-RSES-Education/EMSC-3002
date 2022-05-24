#! /usr/bin/env bash

# This will build all the reveal.md files it finds in the root directory
# These files are also ignored by the jupyterbook script. 


if ! command -v reveal-md &> /dev/null
then
    npm install -g reveal-md 
fi

mkdir -p static_slides
reveal-md  --static static_slides/slideshows \
           --theme https://anu-rses-education.github.io/EMSC-3002/slideshows/_assets/css/anu.css \
           --highlight-theme github \
           --glob '**/*.reveal.md' \
           --separator '<--o-->' \
           --vertical-separator '<--v-->' \
           --static-dirs \
movies,\
images,\
data,\
Module-ii-Figures-Structural-Geology-And-Crustal-Deformation,\
Module-iii-Theory,\
Module-iv-Brittle-Deformation,\
Module-v-Ductile-Deformation
