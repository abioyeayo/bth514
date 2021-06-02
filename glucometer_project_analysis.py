#
#  Author: Ayo Abioye (abioyeayo@gmail.com)
#  Date: Wed 26-May-2021
#  Filename: glucometer_project_analysis.py
#  Description: - A program to plot captured glucometer data for further analysis
#               - Demonstrated in BTH514 Biotechnology Robotics class
#


import matplotlib.pyplot as plt
import csv
  
plt.figure(1)
x = []
y = []
  
with open('20201208_1835_control_solution.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float(row[0])*1.0) #data was captured every second, i.e. at 1s intervals
        y.append(float(row[1]))
  

#plt.plot(x, y, color = 'g', linestyle = 'dashed', marker = 'o',label = "Raw Voltage Data")
plt.plot(x, y, label = "Raw Voltage Data")
plt.ylim(2,4)
plt.xlim(0,100)
plt.xlabel('Duration (s)')
plt.ylabel('Voltage (V)')
#plt.title('Raw Glucose Strip Electrical Reading', fontsize = 20)
plt.title('Unknown / Test Solution Reading', fontsize = 14)
plt.grid()
plt.legend()
#plt.show()



plt.figure(2)
x = []
y = []
  
with open('20201208_1904_10mg_per_dl.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float(row[0])*0.2) #data was captured at 1/5 of a second, i.e. at 0.2s intervals
        y.append(float(row[1]))
  

#plt.plot(x, y, color = 'g', linestyle = 'dashed', marker = 'o',label = "Raw Voltage Data")
plt.plot(x, y, label = "Raw Voltage Data")
plt.ylim(2,4)
plt.xlim(0,150)
plt.xlabel('Duration (s)')
plt.ylabel('Voltage (V)')
plt.title('10 mg/dl Solution Reading', fontsize = 14)
plt.grid()
plt.legend()
#plt.show()



plt.figure(3)
x = []
y = []
  
with open('20201208_1848_20mg_per_dl.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float(row[0])*0.2) #data was captured at 1/5 of a second, i.e. at 0.2s intervals
        y.append(float(row[1]))
  

#plt.plot(x, y, color = 'g', linestyle = 'dashed', marker = 'o',label = "Raw Voltage Data")
plt.plot(x, y, label = "Raw Voltage Data")
plt.ylim(2,4)
plt.xlim(0,150)
plt.xlabel('Duration (s)')
plt.ylabel('Voltage (V)')
plt.title('20 mg/dl Solution Reading', fontsize = 14)
plt.grid()
plt.legend()
#plt.show()



plt.figure(4)
x = []
y = []
  
with open('20201208_1843_100mg_per_dl.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float(row[0])*0.2) #data was captured at 1/5 of a second, i.e. at 0.2s intervals
        y.append(float(row[1]))
  

#plt.plot(x, y, color = 'g', linestyle = 'dashed', marker = 'o',label = "Raw Voltage Data")
plt.plot(x, y, label = "Raw Voltage Data")
plt.ylim(2,4)
plt.xlim(0,150)
plt.xlabel('Duration (s)')
plt.ylabel('Voltage (V)')
plt.title('100 mg/dl Solution Reading', fontsize = 14)
plt.grid()
plt.legend()
#plt.show()



plt.figure(5)
x = []
y = []
  
with open('20201208_1855_200mg_per_dl.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float(row[0])*0.2) #data was captured at 1/5 of a second, i.e. at 0.2s intervals
        y.append(float(row[1]))
  

#plt.plot(x, y, color = 'g', linestyle = 'dashed', marker = 'o',label = "Raw Voltage Data")
plt.plot(x, y, label = "Raw Voltage Data")
plt.ylim(2,4)
plt.xlim(0,300)
plt.xlabel('Duration (s)')
plt.ylabel('Voltage (V)')
plt.title('200 mg/dl Solution Reading', fontsize = 14)
plt.grid()
plt.legend()
#plt.show()


plt.show()
