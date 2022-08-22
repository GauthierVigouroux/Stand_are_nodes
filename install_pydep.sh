#!/bin/sh

echo "Start of installation of libraries !"

#Requests HTML is modify by my self so we need to install it manually to accept # in href fields.
python3 /requests-html/setup.py

#Classic python installation of libraries
python3 -m pip install -r requirements.txt

echo "End of installation of libraries !"