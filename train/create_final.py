import os,sys,ast, numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

os.chdir(r"D:/Coding/2017/ccbd/NEW PAYLOAD/run1/xml")
mapTime = []
mapResources = []
mapID = []
jobName = []

ff = open("../paramfile.txt","w")

for folder in os.listdir():

    params = folder.split("-")
    ff.write(params[1] + "," + params[2] + "," + params[3] + "," + params[4] + "," + params[5] + "," + params[6] + "," + "\n")

    for subfolder in ["job1","job2","job3","job4","job5","job6"]:
        z = "D:/Coding/2017/ccbd/NEW PAYLOAD/run1/xml/" + folder + "/" + subfolder
        os.chdir(z)
        f = open(subfolder + '.xml',"r")
        data = ast.literal_eval(f.read())['tasks']['task']
        for dt in data:
            if dt['id'][-8] is not "r":
                mapTime.append(dt['elapsedTime']/1000)
                mapID.append(dt['id'])
                jobName.append(folder[:-1])
                mapFile = open("task-" + dt['id'][-8] + dt['id'][-2:] + ".xml","r")
                mapData = ast.literal_eval(mapFile.read())['jobTaskCounters']['taskCounterGroup']
                tempMapRes = []
                for i in mapData:
                    if i['counterGroupName'] == "org.apache.hadoop.mapreduce.TaskCounter":
                        mapCounter = i['counter']
                        for j in mapCounter:
                            if j['name'] == 'CPU_MILLISECONDS':
                                tempMapRes.append(j['value'])
                            if j['name'] == 'PHYSICAL_MEMORY_BYTES':
                                tempMapRes.append(j['value'])
                            if j['name'] == 'VIRTUAL_MEMORY_BYTES':
                                tempMapRes.append(j['value'])
                            if j['name'] == 'COMMITTED_HEAP_BYTES':
                                tempMapRes.append(j['value'])
                mapResources.append(tempMapRes)

ff.close()

nMapTime = np.array(mapTime).reshape(len(mapTime),1)

os.chdir(r"D:/Coding/2017/ccbd/NEW PAYLOAD/run1")

tagTimeClustering = AgglomerativeClustering(n_clusters=2)
tagTimeClustering.fit(nMapTime)
timeClusterList = list((tagTimeClustering.fit_predict(nMapTime)))

f = open("taskfile.txt","w")
for i in range(1600):
    f.write(','.join(list(map(str,mapResources[i]))) +','+ str(timeClusterList[i]) + "\n") # str(mapTime[i]) +','+ str(timeClusterList[i]) + "\n")
    
    #print ( str(i) + " == " + (','.join(list(map(str,mapResources[i]))) +','+ str(mapTime[i]) +','+ str(timeClusterList[i]) + "\n") )

f.close()
