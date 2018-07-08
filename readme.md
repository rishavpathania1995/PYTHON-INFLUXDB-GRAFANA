# Pythonscript-Influxdb-Grafana

### Project Title

Python Script which send Device usage statistics to InfluxDb and We Monitor it using Grafana Dashboard.

### Prerequisite

Need to setup Docker environment .
Install [Docker](https://docs.docker.com/install/) , [Docker-Compose](https://docs.docker.com/compose/install/) .
Clone this [Directory](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA) to you server.

```
USED PORTS:
Grafana Webadmin:3000
Chronograf Webadmin:8888
Influxdb :8086
```

### Installation

First you need to install INfluxdb , Chronograf ,Grafana.
I use AWS EC2 instance for this purpose, you can use your own virtual environment.

Run the [docker-compose.yml](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/app/docker-compose.yml)
```
docker-compose up
```
#### NOTE: Make sure you are in [app](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/tree/master/app) directory of the repository.
This script will automatically start docker containers,with configurations that are setup in [docker-compose.yml](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/app/docker-compose.yml).


### Configuring App

After containers are Up and  ready , login to Grafana.

```
http://<server ip>:3000/login

Use default username: admin and password :admin
```
Then add datasource with this configuration i.e [influxdb](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/pics/add_influxdb.PNG).
```
URL : http://influxdb:8086
Database name : test
username :test
password :test
```
[Save and test](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/pics/save_Influxdb.PNG) the data source .
Import [grafana-dashboard.json](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/app/grafana-dashboard.json) file  in your Grafana Dashboard.

Now application is setup ,we need to start [Python Script](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/tree/master/python) , you will find documentation in python folder.

### Demo
Final Grafana Dashboad Look like [this](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/blob/master/pics/grafana_dashboard1.PNG).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.