# Pythonscript-Influxdb-Grafana

# Project Title

Python Script which send Device usage statistics to InfluxDb.

### Prerequisites

You Need to install python3.5 or above to Run this .

### Features

Publish CPU usage ,Memory usage ,Network statistics.

### Installation 

First Install the requirements form requirements.txt file , for testing we are using Ubuntu 16.04.

```
pip3 install -r requirements.txt
```
## Usage

```
   python3 py.py --DBserver <server ip> --DBname <db name> --DBusername <db username> --DBpassword <dbpassword> --Port <port no>
```

For Help

```
python3 py.py --help

```
