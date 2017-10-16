from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import argparse

parser = argparse.ArgumentParser(description='Check for infinite loop.')
parser.add_argument("is_inifinte", action='store_const')
input = parser.parse_args()

mac_addr = 'DE:E5:EA:C5:9C:3E'
count = 0
sensor = RuuviTag(mac_addr)

while count < 2:
    if input.is_inifinte == "":
        count = count + 1
    state = sensor.update()
    myoutput = sensor.state
    
    myoutput["MAC"] = mac_addr
    myoutput["count"] = count
    myoutput["timestamp"] = time.time()
    myoutput["ctime"] = time.ctime()
    
    f = open("broadcast.log", "a")
    f.write(str(myoutput))
    f.write("\n")
    f.close()
    
    print(str(myoutput))
    
    time.sleep(60)

print "End"
