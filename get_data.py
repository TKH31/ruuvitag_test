from ruuvitag_sensor.ruuvitag import RuuviTag
sensor = RuuviTag('DE:E5:EA:C5:9C:3E')







state = sensor.update()
state = sensor.state
print(state)


