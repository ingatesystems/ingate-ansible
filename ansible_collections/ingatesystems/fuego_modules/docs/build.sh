#!/usr/bin/env bash
set -e
cd /home/erik/git/ingate-ansible/ansible_collections/ingatesystems/fuego_modules/docs

# Install requirements.
pip3 install -r requirements.txt

# Create collection documentation into temporary directory
rm -rf temp-rst
mkdir -p temp-rst
chmod 700 temp-rst
antsibull-docs collection \
    --use-current \
    --squash-hierarchy \
    --no-use-html-blobs \
    --breadcrumbs \
    --indexes \
    --dest-dir temp-rst \
    ingatesystems.fuego_modules

# Copy collection documentation into source directory
rsync -cprv --delete-after temp-rst/ rst/

# Build Sphinx site
[ -d html ] && rm -rf html
mkdir -p html
sphinx-build -M html rst build -c . -W --keep-going && \
    mv build/html/* html/

