#!/usr/bin/python3
# Write a Fabric script that distributes an archive to your web servers,using the function do_deploy
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.157.136.99', '54.173.109.63'] ['<IP web-01>', 'IP web-02']

