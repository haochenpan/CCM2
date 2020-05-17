# import os.path
#
# """
#     CONSTANTS
# """
#
# CCM2_dir = os.path.abspath('../CCM2')
# linux_username = 'root'
# ssh_secret_key = os.path.join(CCM2_dir, 'res/id')
# ycsb_bin = '~/ycsb-0.15.0/bin/ycsb'
# cqlsh_bin = '~/cassandra/bin/cqlsh'
# nodetool_bin = '~/cassandra/bin/nodetool'
#
# # print(CCM2_dir)
# # print(ssh_secret_key)
# # print(ycsb_bin)
# # print(cqlsh_bin)
# # print(nodetool_bin)

"""
    PARAMETERS
"""

interface = 'ens4'  # 14.04: eth0, 16.04: ens4, 18.04: ens33; use the ifconfig commmand to confirm
cass_hosts = ["10.142.0.30"]  # internal ips of Cassandra instances
hosts = ",".join(cass_hosts)
