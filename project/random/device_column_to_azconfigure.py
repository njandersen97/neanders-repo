import csv

##This script takes a column of devices in and csv file into an output that can be run with azconfigure
results = []
with open('t1.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])


final = str(results)[1:-1]
final = final.replace('ï»¿','')
print("azconfigure run_parallel_change_nss_in_production_task " + final.replace("'",""))
