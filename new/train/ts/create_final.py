import os,sys,ast, numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

os.chdir(r"D:/Coding/2017/ccbd/MIXED2/mixCounters3/mixCounters3/")
mapTime = []
mapResources = []
mapID = []
jobName = []

ff = open("../ts/paramfile.txt","w")

for folder in os.listdir("D:/Coding/2017/ccbd/MIXED2/mixCounters3/mixCounters3/"):

    params = folder.split("-")
    #ff.write(params[1] + "," + params[2] + "," + params[3] + "," + params[4] + "," + params[5] + "," + params[6] + "," + "\n")
    z = "D:/Coding/2017/ccbd/MIXED2/mixCounters3/mixCounters3/" + folder + "/terasort"
    
    for subfolder in os.listdir(z):
        os.chdir(z + "/" + subfolder)
        f = open(subfolder + '.xml',"r")
        data = ast.literal_eval(f.read())['tasks']['task']
        for dt in data:
            if dt['id'][-8] is not "r":
                # if dt['elapsedTime']/1000 > 100:
                #     continue
                ff.write(params[1] + "," + params[2] + "," + params[3] + "," + params[4] + "," + params[5] + "," + params[6] + "," + "\n")
                
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
        os.chdir(r"D:/Coding/2017/ccbd/MIXED2/mixCounters3/mixCounters3/")

ff.close()

nMapTime = np.array(mapTime).reshape(len(mapTime),1)

os.chdir(r"D:/Coding/2017/ccbd/MIXED2/mixCounters3/ts")
'''
tagTimeClustering = AgglomerativeClustering(n_clusters=2)
tagTimeClustering.fit(nMapTime)
timeClusterList = list((tagTimeClustering.fit_predict(nMapTime)))
'''

import matplotlib.pyplot as plt
nMapTime = [x for x in nMapTime]
x = [x for x in range(len(nMapTime))]
y = sorted(nMapTime)

plt.plot(x,y)
plt.show()


tagTimeClustering = KMeans(n_clusters=2)
tagTimeClustering.fit(nMapTime)
timeClusterList = list((tagTimeClustering.predict(nMapTime)))


f1 = open("taskfile.txt","w")

for i in range(len(mapResources)):
    f1.write(','.join(list(map(str,mapResources[i]))) + "," + str(timeClusterList[i]) + "\n") # str(mapTime[i]) +','+ str(timeClusterList[i]) + "\n")
    
    #print ( str(i) + " == " + (','.join(list(map(str,mapResources[i]))) +','+ str(mapTime[i]) +','+ str(timeClusterList[i]) + "\n") )

f1.close()
