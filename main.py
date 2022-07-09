import time
import board
import adafruit_dht
import psutil

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
        
sensor = adafruit_dht.DHT11(board.D4)
while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity
        temp_float = float(temperature)
        print("temperature: {}*C".format(temp_float))
        if temperature < 20:
            print ("kurang baik")
        elif temperature > 25:
            print ("over")
        else:
            print ("normal")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
        
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(1.0)