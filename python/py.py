

import sys
import argparse
import psutil
import time
import datetime
from influxdb import InfluxDBClient


def get_json_data():
    Total_pid=len(psutil.pids())
    Total_cpu=psutil.cpu_count()
    Usage_per_cpu=psutil.cpu_percent(interval=1)
    Total_memory=psutil.virtual_memory()
    Total_swap_memory=psutil.swap_memory()
    Total_network_stat=psutil.net_io_counters(pernic=False,nowrap=True)
    

    json_data = [
        {
            "measurement": "systemstats",
            "tags": {
                "host": "mypc",
                "region": "India"
            },
            "time": datetime.datetime.utcnow().isoformat(),
            "fields": { 
                    "total_process":int(Total_pid),
                    "total_cpu":int(Total_cpu),
                    "total_memory":int(Total_memory.total),
                    "used_memory":int(Total_memory.used),
                    "free_memory":int(Total_memory.free),
                    "memory_usage":int(Total_memory.percent),
                    "swap_total":int(Total_swap_memory.total),
                    "swap_used":int(Total_swap_memory.used),
                    "swap_free":int(Total_swap_memory.free),
                    "swap_usage":int(Total_swap_memory.percent),
                    "cpu_0":int(Usage_per_cpu),
                   #"cpu_0":Usage_per_cpu[1],
                   #"cpu_1":Usage_per_cpu[1],
                   #"cpu_2":Usage_per_cpu[2],
                   #"cpu_3":Usage_per_cpu[3],
                    "bytes_sent":int(Total_network_stat.bytes_sent),
                    "bytes_recv":int(Total_network_stat.bytes_recv),
                    "packet_sent":int(Total_network_stat.packets_sent),
                    "packet_recv":int(Total_network_stat.packets_recv)
                                             }  
     }
        ]
    print(json_data)
    return(json_data)


if __name__ == "__main__":
    
    parser=argparse.ArgumentParser()

    parser.add_argument("--DBserver",help="DB server")
    parser.add_argument("--DBname",help="DB name")
    parser.add_argument("--DBusername",help="username for DB")
    parser.add_argument("--DBpassword",help="password for Database")
    parser.add_argument("--Port",help="Port where db server listen ")
    args = parser.parse_args()

    Influxdb_ip=args.DBserver
    Influxdb_port=args.Port
    Influxdb_name=args.DBname
    Influxdb_user=args.DBusername
    Influxdb_pass=args.DBpassword

    try:
        client = InfluxDBClient(Influxdb_ip, Influxdb_port, Influxdb_name, Influxdb_user,Influxdb_pass)

    except:
        print("error connecting to Database server!!! Please add credential correctly")

    else:
        print("Successfully connected to DB")

    while True:
        try:
            print(client.write_points(get_json_data()))
        
        except:
            print("Error inserting data to DB!!! Check Json Data")

        time.sleep(2)
    
   