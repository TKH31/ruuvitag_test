from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import sys

arg_1 = sys.argv[1]

mac_addr = 'DE:E5:EA:C5:9C:3E'
count = 0
sensor = RuuviTag(mac_addr)

while count < 2:
    if arg_1 == "":
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
