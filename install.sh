#!/bin/zsh

DIR_USR="$HOME/bin/"

cp bulkcrop.py bulkcrop
chmod +x bulkcrop

if [ -d "$DIR_USR" ]; then
    mv bulkcrop "$DIR_USR"
fi

# alternative installation paths to be added later