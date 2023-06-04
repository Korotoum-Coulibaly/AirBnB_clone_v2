#!/usr/bin/python3
"""Write a Fabric script that distributes an archive to your web servers function do_deploy."""
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['100.27.5.96', '100.25.180.2'] 

def do_deploy(archive_path):
    """ Fabric script that distributes an archive to my web servers"""
    if exists(archive_path) is false:
	return False 
    filename = archive_path.split('/')[-1]
    tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
	put(archive_path, "/tmp/")
	run("mkdir -p {}/".format(tgz))
	run("tar -xzf {} -C {}/".format(tmp, tgz))
	run("rm {}".format(tmp))
	run("mv {}/web_static/* {}/".format(tgz, tgz))
	run("rm -rf {}/web_static".format(tgz))
	run("rm -rf /data/web_static/current")
	run("ln -s {}/ /data/web_static/current".format(tgz))
	return True
    except:
	return False


