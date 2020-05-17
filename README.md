
### benchmark workflow
- start Cassandra and YCSB servers
- install CCM2 for each of them (see below)
- update cassandra.yaml (see below)
- start each Cassandra server: `cd ~/cassandra/bin && ./cassandra -R`
- at a Cassandra server, check node join: `cd ~/cassandra/bin && ./notetool status`
- use cqlsh to create the column family `ycsb` and the table `usertable` (see below)
- generate ycsb commands (see below) and run each command shown 
### install CCM2 (requires Ubuntu 16.04)
```shell script
# to install a branch recorded in ~/CCM2/py/setupCass.py
sudo su
sudo apt-get install -y git
cd && git clone https://github.com/haochenpan/CCM2.git
. ~/CCM2/sh/setup.sh bsr

# to install only ycsb
sudo su
sudo apt-get install -y git
cd && git clone https://github.com/haochenpan/CCM2.git
. ~/CCM2/sh/setup.sh no-cass

```

### switch Cassandra version
```shell script
# to remove the cassandra folder and reinstall a branch
python3 ~/CCM2/py/setupCass.py bsr

# just switch a branch and recompile
python3 ~/CCM2/py/setupCass.py bsr no-rm

```

### create the table
```shell script
# select a internal ip from shown in ./notetool status
./cqlsh <internal-ip>
CREATE KEYSPACE ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': <num-of-servers>};
CREATE TABLE ycsb.usertable ( y_id varchar primary key, field0 varchar);
```

### update cassandra.yaml
```shell script
# step 1: modify ~/CCM2/py/conf.py to set parameters

# step 2:
python3 ~/CCM2/py/changeYaml.py

```

### generate ycsb commands
```shell script
# step 1: modify ~/CCM2/py/ycsb.py to set parameters

# step 2: try:
python3 ~/CCM2/py/ycsb.py load 3 5
# try:
python3 ~/CCM2/py/ycsb.py # to see the help message
```