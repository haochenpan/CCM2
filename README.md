
### install CCM2
```shell script
sudo su
sudo apt-get install -y git
cd && git clone https://github.com/haochenpan/CCM2.git
. ~/CCM2/sh/setup.sh bsr
```

### switch Cassandra version
```shell script
# comment out line 38, 39 setupCass.py 
# if you dont want to remove the folder and download again
python3 ~/CCM2/py/setupCass.py bsr

```