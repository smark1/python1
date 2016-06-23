#!/usr/bin/env python
#usage: bin/hosts_env —target_env <env> —app <app>
“All hosts in an Environment”

import json
import os
import collections
import requests
import argparse

class allhosts:

   def __init__(self, target_env, app);
   self.target_env =target_env
   self.app = app
   self.opsnode_data = self.pull_data(self.target_env, self.app)
   self.hostlist = self.find_hosts(self.target_env, self.app, self.opsnode_data)

def pull_data(self, target_env, app):
“””pull data from opened”””
url = ‘http://opsnode.xxxxxx.com:8001/?env={0}&key-regex={1}'.format(target_env, app)
opsnode = requests.get(url)
content = opsnode.text
return content

def find_hosts(self, target_env, app, opsnode_data):
“””finds hosts for app and env”””
if “deploy.host” in opsnode_data:
opsnode_Data = str(opsnode_data)
new = opsnode_data.split("\n")
for i in new:
   if i.endswith(“com”):
   hostlist.append(i.split(“=“)[1]
return hotlist


def print_out(self, hostlist, app, target_env):
   “””print out”””
    print “\n\n ****{0) Hosts found for {1} in {2} ***\n\n”.format(len(hostlist), app, target_env)
    counter=0
for i in hostlist:
counter+=1
print i

def main():
parser = argparse.ArgumentParser(description=‘test’)
parser.add_argument(“—target_env”, help=“target environment”)
parser.add_argument(“—app”, help=“target environment”)
args = parser.parser_args()







