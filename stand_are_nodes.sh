#!/bin/sh

echo "           __                          .___                                                          .___                   
  ______ _/  |_  _____      ____     __| _/     _____    _______    ____         ____     ____     __| _/   ____     ______ 
 /  ___/ \   __\ \__  \    /    \   / __ |      \__  \   \_  __ \ _/ __ \       /    \   /  _ \   / __ |  _/ __ \   /  ___/ 
 \___ \   |  |    / __ \_ |   |  \ / /_/ |       / __ \_  |  | \/ \  ___/      |   |  \ (  <_> ) / /_/ |  \  ___/   \___ \  
/____  >  |__|   (____  / |___|  / \____ |      (____  /  |__|     \___  >     |___|  /  \____/  \____ |   \___  > /____  > 
     \/               \/       \/       \/           \/                \/           \/                \/       \/       \/  "

echo "Welcome in Stand are Nodes project !"
echo "Options:
    1. Populate the database
    2. Vizualize the database
    Other to skip and end"
echo "Choose your option here :"
read -r option
echo "$option"

case "$option" in
    1)
    echo "Precise the json in file name (with json extension) :"
    read -r namein
    echo "Precise the json output file name (with json extension) :"
    read -r nameout
    python3 standarenodesPARENT.py -i "$namein" -o "$nameout"
    ;;
    2)
    echo "Precise the json in file name (with json extension) :"
    read -r namein
    echo "Precise the name output file name (with html extension) :"
    read -r nameout
    echo "Precise the json file used in input of the database (with json extension) :"
    read -r namebase
    echo "Choose type of vizualization :
        1. Network
        2. Circle"
    read -r option_viz
    case "$option_viz" in
        1)
        python3 vizdata.py -b "$namebase" -i "$namein" -o "$nameout"
        ;;
        2)
        python3 vizdatacircle.py -i "$namein" -o "$nameout"
        ;;
        *)
        echo "bad option"
        ;;
    esac
    ;;
    *)
    echo "bad option"
    ;;
esac
echo "End
Edit by Gauthier Vigouroux
In collaboration with Pedro Merino Laso and Christophe Claramunt"