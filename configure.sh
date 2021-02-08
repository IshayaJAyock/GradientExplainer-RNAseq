#!/bin/bash

SETUP_PATH=./setup.py
META_PATH=./meta.yaml

# Get user input
echo "Please follow the prompts for configuration [default values will be in square brackets]."
echo " "

read -p "What is the name of the project? (This will be used in imports) [mk_project_template]: " project_name
project_name=${project_name:-mk_project_template}
project_name=${project_name//-/_} # convert dashes to underscores for proper naming

read -p "Type a short description of the project []: " project_description
project_description=${project_description:-}

read -p "Enter the github repo url [https://github.com/MaxKelsen/mk-project-template.git]: " git_url
git_url=${git_url:-http://github.com/MaxKelsen/mk-project-template.git}

read -p "Enter your name [Max Kelsen]: " author_name
author_name=${author_name:-Max Kelsen}

read -p "Enter your MK email []: " author_email
author_email=${author_email:-}

read -p "Enter the required python version [3.6]: " python_version
python_version=${python_version:-3.6}

# Rename src folder
mv src $project_name 

# Reconfigure setup.py
# the replacement str in description has an extra space because the regex needs to match 
# a space in front of description instead of the _ to avoid replacing long_description 
sed -i".original" "s|name=.*|name=\"${project_name}\",|" $SETUP_PATH
sed -i".original" "s|[^_]description=.*| description=\"${project_description}\",|" $SETUP_PATH 
sed -i".original" "s|url=.*|url=\"${git_url}\",|" $SETUP_PATH
sed -i".original" "s|author=.*|author=\"${author_name}\",|" $SETUP_PATH
sed -i".original" "s|author_email=.*|author_email=\"${author_email}\",|" $SETUP_PATH
sed -i".original" "s|python_requires=.*|python_requires=\">=${python_version}\",|" $SETUP_PATH

rm -- "${SETUP_PATH}.original"

# Reconfigure meta.yaml
sed -i".original" "s|name:.*|name: ${project_name}|" $META_PATH
sed -i".original" "s|git_url:.*|git_url: ${git_url}|" $META_PATH
sed -i".original" "s|- python.*|- python>=${python_version}|" $META_PATH
sed -i".original" "s|home:.*|home: ${git_url}|" $META_PATH
sed -i".original" "s|description:.*|description: ${project_description}|" $META_PATH

rm -- "${META_PATH}.original"

echo "Adding newly renamed source code dir, as well as altered setup.py and meta.yaml to git staging area."
git add ./$project_name $SETUP_PATH $META_PATH ./src
