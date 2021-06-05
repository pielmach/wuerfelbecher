#!/bin/bash

pip install --upgrade --force-reinstall -r requirements.txt

pip freeze > requirements.txt.pinned
