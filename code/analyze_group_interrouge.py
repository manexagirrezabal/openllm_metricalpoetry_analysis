import pandas as pd
import glob
import json
import numpy as np
from sklearn.metrics import mean_absolute_error
import sys
import re


#experiment_ucloud_groupanalyses/experiment_ucloud_withoutotopic/groupresponses/groupno4.analysis
#experiment_ucloud_groupanalyses/experiment_ucloud_withoutotopic/responses/prompt40.txt

results_notopic = {}
for filename in glob.glob("dataset_groups/topic_undefined/groupresponses/groupno*analysis"):
	filenamev = filename.split("/")
	groupnumber = re.sub("[^0-9]","",filenamev[-1])
	promptfile = "/".join(filenamev[:-2])+"/responses/prompt"+groupnumber+"0.txt"
#	print (filename)
#	print (promptfile)
	f=open(promptfile)
	prompt = f.readline().strip()
	f.close()
	f=open(filename)
	currentjson = json.load(f)
	f.close()
	results_notopic[prompt] = currentjson['acrossnovelty (lbyl, alllines, singlestr)'][2]

results_topic = {}

for filename in glob.glob("dataset_groups/topic_defined/groupresponses/groupno*analysis"):
	filenamev = filename.split("/")
	groupnumber = re.sub("[^0-9]","",filenamev[-1])
	promptfile = "/".join(filenamev[:-2])+"/responses/prompt"+groupnumber+"0.txt"
#	print (filename)
#	print (promptfile)
	f=open(promptfile)
	prompt = f.readline().strip()
	f.close()
	f=open(filename)
	currentjson = json.load(f)
	f.close()
	results_topic[prompt] = currentjson['acrossnovelty (lbyl, alllines, singlestr)'][2]

r1s_notopic = [results_notopic[prompt][0]  for prompt in results_notopic.keys()]
r1s_topic = [results_topic[prompt][0]  for prompt in results_topic.keys()]

r2s_notopic = [results_notopic[prompt][1]  for prompt in results_notopic.keys()]
r2s_topic = [results_topic[prompt][1]  for prompt in results_topic.keys()]

r3s_notopic = [results_notopic[prompt][2]  for prompt in results_notopic.keys()]
r3s_topic = [results_topic[prompt][2]  for prompt in results_topic.keys()]

r4s_notopic = [results_notopic[prompt][3]  for prompt in results_notopic.keys()]
r4s_topic = [results_topic[prompt][3]  for prompt in results_topic.keys()]

rls_notopic = [results_notopic[prompt][4]  for prompt in results_notopic.keys()]
rls_topic = [results_topic[prompt][4]  for prompt in results_topic.keys()]

rsgs_notopic = [results_notopic[prompt][5]  for prompt in results_notopic.keys()]
rsgs_topic = [results_topic[prompt][5]  for prompt in results_topic.keys()]


print ("No topic vs. Specified topic")
print ("R1", np.mean(r1s_notopic),np.mean(r1s_topic))
print ("R2", np.mean(r2s_notopic),np.mean(r2s_topic))
print ("R3", np.mean(r3s_notopic),np.mean(r3s_topic))
print ("R4", np.mean(r4s_notopic),np.mean(r4s_topic))
print ("RLCS", np.mean(rls_notopic),np.mean(rls_topic))
print ("RSU4", np.mean(rsgs_notopic),np.mean(rsgs_topic))
