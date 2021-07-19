#! /usr/bin/env bash

# This will build all the reveal.md files it finds in the root directory
# These files are also ignored by the jupyterbook script


if ! command -v reveal-md &> /dev/null
then
    npm install -g reveal-md 
fi


mkdir -p static_slides
reveal-md  --static static_slides/slideshows \
           --theme css/anu.css --glob '**/*.reveal.md' \
           --separator '<--o-->' \
           --vertical-separator '<--v-->' \
           --static-dirs movies,images,images,Figures-Fold-Geometry-1,Figures-Folds-and-Folding-Mechanisms,Figures-Shear_zones,Figures-Structural-Geology-And-Crustal-Deformation,Figures-Structures-Associated-with-Folding-1,Figures-Structures-Associated-with-Folding-2,Figures-Structures-Associated-with-Folding-3,Figures-Brittle_deformation1,Figures-Brittle_deformation2,Figures-Brittle_deformation3,Figures-Brittle_deformation4
