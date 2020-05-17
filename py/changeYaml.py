import yaml
import pprint
import os
from conf import *


def generate_cass_yaml():
    with open('/root/CCM2/res/cassandra.yaml') as inFile:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        cassandra_yaml = yaml.load(inFile, Loader=yaml.FullLoader)

    del cassandra_yaml['listen_address']
    del cassandra_yaml['rpc_address']
    cassandra_yaml['listen_interface'] = interface
    cassandra_yaml['rpc_interface'] = interface
    cassandra_yaml['auto_snapshot'] = False
    cassandra_yaml['seed_provider'][0]['parameters'][0]['seeds'] = hosts

    with open('~/cassandra/conf/cassandra.yaml', 'w') as outFile:
        documents = yaml.dump(cassandra_yaml, outFile)


if __name__ == '__main__':
    generate_cass_yaml()


