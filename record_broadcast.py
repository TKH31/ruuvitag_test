from ruuvitag_sensor.ruuvitag import RuuviTag
import time

mac_addr = 'DE:E5:EA:C5:9C:3E'
count = 0
sensor = RuuviTag(mac_addr)

while count < 2:
    count = count + 1
    state = sensor.update()
    myoutput = sensor.state
    
    myoutput["MAC"] = mac_addr
    myoutput["count"] = count

    f = open("broadcast.log", "a")
    f.write(str(myoutput))
    f.close()
    
    print(str(myoutput))
    
    time.sleep(60)

print "End"
