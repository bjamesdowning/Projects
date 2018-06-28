#! /usr/bin/python3

import requests
import json
import sys

switchIPFile = sys.argv[1]
cmdFile = sys.argv[2]
switchUser = "admin"
switchPass = "admin"
headers = {"content-type": "application/json-rpc"}


def configControl(IP, cmd):
    url = "http://{}/ins".format(IP)
    payload = [
        {"jsonrpc": "2.0", "method": "cli",
         "params": {"cmd": "conf t", "version": 1},
         "id": 1},
        {"jsonrpc": "2.0", "method": "cli",
            "params": {"cmd": "{}".format(cmd), "version": 1},
         "id": 1}
    ]
    resp = requests.post(url, data=json.dumps(payload), headers=headers,
                         auth=(switchUser, switchPass)).json()
    print(resp)


switchIP = [line.rstrip("\n") for line in open(switchIPFile)]
cmds = [line.rstrip("\n") for line in open(cmdFile)]

for IP in switchIP:
    print(IP)
    for cmd in cmds:
        print(cmd)
        configControl(IP, cmd)
