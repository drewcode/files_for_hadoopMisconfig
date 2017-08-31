import os,sys,requests
from xml.dom import minidom
from bs4 import BeautifulSoup
import urllib
import xml.etree.ElementTree as ET
import ast
os.chdir("D:/Coding/2017/ccbd/MIXED2/mixRun4/")


count = 0
rContent = requests.get('http://10.10.1.58:19888/ws/v1/history/mapreduce/jobs/').content
jobDetails = []
with open("../jobDetails.xml","wb") as f:
    f.write(rContent)
    jobDetails = ast.literal_eval(open('../jobDetails.xml',"r").read())["jobs"]["job"]

for f in os.listdir():
    if f.endswith("stderr"):
        print(os.getcwd())
        lines = open(f,"r").readlines()
        for line in lines:

            try:
                if "completed successfully" in line:
                    print(f)
                    if(os.path.exists("../mixCounters4/mixCounters4/" + f[:-7])== False):
                        os.mkdir("../mixCounters4/mixCounters4/" + f[:-7])
                        os.mkdir("../mixCounters4/mixCounters4/" + f[:-7] + "/pagerank/")
                        os.mkdir("../mixCounters4/mixCounters4/" + f[:-7] + "/terasort/")
                        
                    jobID = line[42:64]
                    print(jobID)
                    for i in jobDetails:
                        if i["id"] == jobID:
                            if i["name"].startswith("Pagerank"):
                                os.chdir("../mixCounters4/mixCounters4/" + f[:-7] + "/pagerank/")
                            else:
                                os.chdir("../mixCounters4/mixCounters4/" + f[:-7] + "/terasort/")
                    #os.mkdir(".../mixCounters1/" + f[:-6] + "/job" +jobID[-1])
                    r = requests.get('http://10.10.1.58:19888/ws/v1/history/mapreduce/jobs/'+  jobID +'/tasks')
                    os.mkdir(jobID)
                    with open(jobID + "/" +jobID + '.xml', "wb") as code:
                        code.write(r.content)
                        code.close()
                    data = ast.literal_eval(open(jobID + "/" + jobID + '.xml',"r").read())['tasks']['task']
                    taskID = list(map(lambda x:x['id'],data))
                    sortList = list(map(lambda x: int(x.split('_')[-1]),taskID))
                    taskID = [x for (y,x) in sorted(zip(sortList,taskID))]
                    #taskID[0],taskID[1] = taskID[1],taskID[0]
                    for ID in taskID:
                        #to get task counters/resources, change 'attempts' to 'counters'.
                        r1 = urllib.request.urlopen('http://10.10.1.58:19888/ws/v1/history/mapreduce/jobs/'+  jobID +'/tasks/' + ID + '/counters')
                        with open(jobID + "/task-" + ID[-8] + ID[-2:]  + ".xml", "wb") as f1:
                            f1.write(r1.read())
                            f1.close()
                    os.chdir("D:/Coding/2017/ccbd/MIXED2/mixRun4/")
            except Exception:
                #print(vars(Exception))
                os.chdir("D:/Coding/2017/ccbd/MIXED2/mixRun4/")
                pass
