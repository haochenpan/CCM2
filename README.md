
### benchmark workflow
- start Cassandra and YCSB servers on GCP (requires Ubuntu 16.04 or above)
- install CCM2 for each of them (see below)
- update cassandra.yaml (see below)
- if the implementation needs some changes in a java file, do so, and run `ant` in `~/cassandra` to build again
- start each Cassandra server: `cd ~/cassandra && ./bin/cassandra -R`
- at a Cassandra server, check node join: `cd ~/cassandra && ./bin/nodetool status`
- use cqlsh to create the column family `ycsb` and the table `usertable` (see below)
- generate ycsb commands (see below) and run each command shown on a ycsb server
- run `fuser -k 7199/tcp` on each Cassandra server to kill Cassandra
- run `ps -fe | grep java` to check
- run `rm ~/cassandra/data ~/cassandra/logs -rf` to completely remove data and log folders
### install CCM2 
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

### update cassandra.yaml
```shell script
# step 1: modify ~/CCM2/py/conf.py to set parameters

# step 2:
python3 ~/CCM2/py/changeYaml.py

```

### create the table
```shell script
# select a internal ip from shown in ./notetool status
cd ~/cassandra &&  ./bin/cqlsh <internal-ip> -e "CREATE KEYSPACE ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': <num-of-servers>};"
cd ~/cassandra &&  ./bin/cqlsh <internal-ip> -e "CREATE TABLE ycsb.usertable ( y_id varchar primary key, field0 varchar);"

#e.g.
./bin/cqlsh 10.142.0.30 -e "create keyspace ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1};"
./bin/cqlsh 10.142.0.30 -e "CREATE TABLE ycsb.usertable(y_id varchar PRIMARY KEY, field0 varchar);"

# different implementations requires different schemas, see https://github.com/haochenpan/CCM#cassandra-table-schemas
```

### generate ycsb commands
```shell script
# assume parameters in modify ~/CCM2/py/conf.py are set
# step 1: modify ~/CCM2/py/ycsb.py to set parameters 

# step 2: try
python3 ~/CCM2/py/ycsb.py load 3 5
python3 ~/CCM2/py/ycsb.py run 3 5

# step 3: try
python3 ~/CCM2/py/ycsb.py # to see the help message
```


### switch Cassandra version
```shell script
# to remove the cassandra folder and reinstall a branch
python3 ~/CCM2/py/setupCass.py base
python3 ~/CCM2/py/setupCass.py bsr

# just switch a branch and recompile
python3 ~/CCM2/py/setupCass.py bsr no-rm
python3 ~/CCM2/py/setupCass.py base no-rm

```