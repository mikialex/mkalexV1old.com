#! /bin/bash
rsync -azv --exclude ENV3.6 --delete ./* root@mkalex.com:/var/www/preview
