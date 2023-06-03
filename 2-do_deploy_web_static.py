#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['100.27.5.96', '100.25.180.2']
#<IP web-01>', 'IP web-02'

def do_deploy(archive_path):
    """ Fabric script that distributes an archive
    to my web servers"""

    if exists(archive_path) is false:
	return False 
	#returns false if the file at archive_path doesnt exist
    filename = archive_path.split('/')[-1]
    tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
	put(archive_path, "/tmp/")
	#download the archive file to the tmp directory
	run("mkdir -p {}/".format(tgz))
	#dzip archive to the folder /data/web_static/releases/
	run("tar -xzf {} -C {}/".format(tmp, tgz))
	run("rm {}".format(tmp))
	run("mv {}/web_static/* {}/".format(tgz, tgz))
	run("rm -rf {}/web_static".format(tgz))
	#delete archive
	run("rm -rf /data/web_static/current")
	#delete symbolic link
	run("ln -s {}/ /data/web_static/current".format(tgz))
	#create a new symbolic linc
	return True
    except:
	return False


