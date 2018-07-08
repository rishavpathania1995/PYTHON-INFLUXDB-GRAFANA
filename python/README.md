### Prerequisites

You Need to install python 3.5 or above and pip to Run this .

### Features

Publish CPU usage ,Memory usage ,Network statistics.

### Installation 

First Install the requirements form [requirements.txt file](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/python/requirements.txt) , for testing we are using Ubuntu 16.04.

```
pip3 install -r requirements.txt
```
## RUN
Run [py.py](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/python/py.py) file 
```
python3 py.py --DBserver <server ip> --DBname <db name> --DBusername <db username> --DBpassword <dbpassword> --Port <port no>
```
To Run this Script in linux shell background

```

nohup python3 py.py --DBserver <server ip> --DBname <db name> --DBusername <db username> --DBpassword <dbpassword> --Port <port no> &

```

For Help

```
python3 py.py --help

```
