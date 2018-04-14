import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosv = driver('10.0.0.1','cisco','cisco')
iosv.open()

print('Accessing 10.0.0.1')
iosv.load_merge_candidate(filename='ACL1.cfg')
iosv.commit_config()
iosv.close()