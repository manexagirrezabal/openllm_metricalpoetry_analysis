import pandas as pd
import glob
import json
import numpy as np
from sklearn.metrics import mean_absolute_error, confusion_matrix, classification_report, accuracy_score
import sys

fi = pd.read_excel("../prompts_gold_values.xlsx")

gold_num = int(sys.argv[1])

try:
	inparg = sys.argv[2]
	goldstruc = np.array(sys.argv[2].split("-"),dtype=int)
	assert gold_num == sum(goldstruc)
except IndexError:
	goldstruc = None

prompts_of_interest = list(fi[fi['No of lines (ignoring empty lines or line breaks)'] == gold_num]['Unnamed: 2'])

#In this case, the distinction between simple and complex structures happens
#when the word "each" appears in the prompt.
complex=True #4*
#complex=False #4

if complex:
	prompts_of_interest = [pr for pr in prompts_of_interest if "each" in pr]
else:
	prompts_of_interest = [pr for pr in prompts_of_interest if "each" not in pr]

if goldstruc is None and gold_num == 14:
	prompts_of_interest = [pr for pr in prompts_of_interest if not "stanzas" in pr]
elif goldstruc is not None and gold_num == 14:
	prompts_of_interest = [pr for pr in prompts_of_interest if "stanzas" in pr]

print ("I am considering these prompts")
for p in prompts_of_interest:
	print (p)

responsenums_of_interest = []
for file in glob.glob("../dataset/topic_defined/responses/prompt*"):
	#We get the content of the prompt and we remove the last word, as it is just a number from 0 to 9
	f=open(file)
	prompt = " ".join(f.read().strip().split(" ")[:-1])
	f.close()
	if prompt in prompts_of_interest:
		response_num = file[:-4].split("t")[-1] #All files have the following name: DIR/DIR/.../promptDIG+.txt
		responsenums_of_interest.append(response_num)

nolines = []
goldvals = []
for rnoi in responsenums_of_interest:
	filename = "../dataset/topic_defined/responses/response"+rnoi+"_clean.txt.analysis"
	f=open(filename)
	result = json.load(f)
	f.close()
	if goldstruc is not None:
		for (linecount, goldlinecount) in zip(result['linecount'], goldstruc):
			nolines.append(linecount)
			goldvals.append(goldlinecount)
	elif isinstance(result['linecount'], list):
#	if len(result['linecount']) ==1: #We want to make sure that the number of stanzas is 1
		sumnolines = sum(result['linecount'])
		nolines.append(sumnolines)
		goldvals.append(gold_num)


print (mean_absolute_error(goldvals,nolines))
print (len(nolines))

print (confusion_matrix(goldvals,nolines))
print (classification_report(goldvals,nolines))
print (accuracy_score(goldvals,nolines))
