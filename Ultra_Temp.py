# from gpiozero import DistanceSensor
# import adafruit_dht
# import board
import time
import matplotlib.pyplot as plt
import os
import random
import pandas as pd
import numpy as np
from datetime import datetime


# dht_device = adafruit_dht.DHT11(board.D17)
# ultrasonic = DistanceSensor(echo =  18, trigger = 4)

data = open("data.log",'a')

TempList = []
DisList = []
TimeList = []

StartTime =time.time()

#Interactive Plotting
# plt.ion()  
# fig, (TempPlot,DisPlot) = plt.subplots(2,1,figsize=(8, 8))

fig,(TempPlot)  = plt.subplots(figsize=(8, 8))

# Templine, = TempPlot.plot(TimeList, TempList, marker='o', linestyle='-', color='blue')
# TempPlot.set_xlabel("Time (seconds)")
# TempPlot.set_ylabel("Temperature (°C)")
# TempPlot.set_title("Temperature")

# Disline, = DisPlot.plot(TempList, TempList, marker='x', linestyle='-', color='red')
# DisPlot.set_xlabel("Time (seconds)")
# DisPlot.set_ylabel("Distance (cm)")
# DisPlot.set_title("Distance")

try :
    while True:

        currentDateTime = datetime.now()
        
        currentDateTimeLogFile = currentDateTime.strftime("%d-%m-%Y %H:%M:%S")
        currentDateTimeStr = str(currentDateTimeLogFile)

        currentTime = time.time() - StartTime

        # temperature_c = dht_device.temperature
        # distance = ultrasonic.distance
        
        temperature_c = random.randint(0,50) 
        distance = random.randint(0,400)
        
        TempList.append(temperature_c)
        DisList.append(distance)
        TimeList.append(currentTime)

        print(f"Seconds : {currentTime}")
        print(f"Temperature: {temperature_c}\u00b0C")
        print(f"Distance : {distance} cm")
        
        data.writelines(f"{currentDateTimeStr} Temperature = {temperature_c} Distance = {distance}\n")

        #Interactive Plotting
        # Templine.set_xdata(TimeList)
        # Templine.set_ydata(TempList)
        # Disline.set_xdata(TimeList)
        # Disline.set_ydata(DisList)
        
        # TempPlot.relim()
        # TempPlot.autoscale_view(True,True,True)
        # DisPlot.relim()
        # DisPlot.autoscale_view(True,True,True)

        # plt.draw()
        # plt.pause(1)

        time.sleep(1)

except KeyboardInterrupt:
    
    data.close()

    #Interactive Plotting
    
    # plt.ioff()
    # Templine, = TempPlot.plot(TimeList, TempList, marker='o', linestyle='-', color='blue')
    # TempPlot.set_xlabel("Time (seconds)")
    # TempPlot.set_ylabel("Temperature (°C)")
    # TempPlot.set_title("Temperature")
    
    # Disline, = DisPlot.plot(TempList, TempList, marker='x', linestyle='-', color='red')
    # DisPlot.set_xlabel("Time (seconds)")
    # DisPlot.set_ylabel("Distance (cm)")
    # DisPlot.set_title("Distance")

    plt.plot(TimeList,TempList)
    plt.figure()
    plt.plot(TimeList,DisList,'ro-')
    plt.show()