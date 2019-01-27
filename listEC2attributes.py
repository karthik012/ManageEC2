from pprint import pprint
from boto import ec2
import datetime
from dateutil.parser import *

# specify AWS keys


def main():
    ec2conn = ec2.connection.EC2Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    reservations = ec2conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        launch_time = datetime.datetime.strptime(i.launch_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        pprint(launch_time)
        instance_id = i.id
        current_time = datetime.datetime.now()
        pprint(current_time)
        strval = timetimeDiff(launch_time, current_time)
        if(strval):
            pprint("yes !!")
            stop_instance(instance_id,ec2conn)

def timetimeDiff(launch_time,current_time):
      delta = abs(current_time - launch_time)
      if((delta.seconds/60)>=120):
          str = True
          return str

def stop_instance(instance,ec2conn):
    ec2conn.stop_instances(instance_ids=[instance])
    pprint("Successfully stopped the instance : {}".format(instance))

if __name__ == '__main__':
    main()













