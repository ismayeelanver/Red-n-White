#!/bin/bash

echo "Installing requirements"

pip install -r ./requirements/ismayeel-requirements.txt > /dev/null

echo "Launching"

python ./Red_and_white.py > /dev/null
