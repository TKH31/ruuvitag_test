from ruuvitag_sensor.ruuvi import RuuviTagSensor






count = 0
def handle_data(found_data):
    global count
    count = count + 1



    sensor = RuuviTag('DE:E5:EA:C5:9C:3E')


    



state = sensor.update()
state = sensor.state
print(state)
    
    
    
    myoutput = found_data[1]
    myoutput["MAC"] = str(found_data[0])
    myoutput["count"] = count
    f = open("broadcast.log", "a")
    f.write(str(myoutput))
    f.close()
    print(str(myoutput))
RuuviTagSensor.get_datas(handle_data)
