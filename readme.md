# Pythonscript-Influxdb-Grafana

### Project Title

Python Script which send Device usage statistics to InfluxDb and We Monitor it using Grafana Dashboard.

### Prerequisite

Need to setup Docker environment .
Install [Docker](https://docs.docker.com/install/) , [Docker-Compose](https://docs.docker.com/compose/install/) .


```
USED PORTS
Grafana webpanel:3000
Chronograf webpanel:8888
Influxdb :8086
```

### Installation

First you need to install INfluxdb , Chronograf ,Grafana.
I use aws ec2 instance for this purpose, you can use your own virtual environment.
```
Run the docker-compose.yml
```
docker-compose up
#### NOTE: Make sure you are in the same directory  i.e  app folder of the repository.
This script will automatically start docker containers,with configurations that are setup in docker-compose.yml.


### Configuring App

After containers are Up and  ready , we first login to Grafana.

```
http://<server ip>:3000/login
```
Use default username: admin and password :admin

Then add datasource with this configuration i.e influxdb.
```
URL : http://influxdb:8086
Database name : test
username :test
password :test
```
Save and test the data source once its done , Import grafana-dashboard.json file  in your Grafana Dashboard.

Now application is setup ,we need to start [Python Script](https://github.com/rishavpathania1995/PYTHON-INFLUXDB-GRAFANA/tree/master/python) , you will find documentation in python folder.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details