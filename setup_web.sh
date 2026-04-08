#!/bin/bash

# Create directories for web infrastructure
mkdir -p web/html
mkdir -p web/css
mkdir -p web/js
mkdir -p web/data

# Create a README file in each directory
for dir in html css js data; do
  echo "# This directory is for $dir files" > web/$dir/README.md
  echo "Directory for storing $dir files" > web/$dir/README.txt

done

echo "Web infrastructure setup completed."