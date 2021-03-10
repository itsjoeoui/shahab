#!/bin/sh
pkill screen
git reset --hard
git pull
screen -S lavalink -dm bash -c "java -jar Lavalink.jar"
pipenv sync
screen -S bot -dm bash -c "pipenv shell 'python3 src/bot.py'"
screen -ls
