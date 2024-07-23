import pandas as pd
import glob
import json
import numpy as np
from sklearn.metrics import mean_absolute_error,accuracy_score,confusion_matrix
import sys


def flatten(l):
	return [subel for el in l for subel in el]



fi = pd.read_excel("../prompts_gold_values.xlsx")

gold_num = int(sys.argv[1])

prompts_of_interest = list(fi[fi['No of syllables per line'] == gold_num]['Unnamed: 2'])

responsenums_of_interest = []
for file in glob.glob("../dataset/topic_defined/responses/prompt*"):
	#We get the content of the prompt and we remove the last word, as it is just a number from 0 to 9
	f=open(file)
	prompt = " ".join(f.read().strip().split(" ")[:-1])
	f.close()
	if prompt in prompts_of_interest:
		response_num = file[:-4].split("t")[-1] #All files have the following name: DIR/DIR/.../promptDIG+.txt
		responsenums_of_interest.append(response_num)

nosylls = []
for rnoi in responsenums_of_interest:
	filename = "../dataset/topic_defined/responses/response"+rnoi+"_clean.txt.analysis"
	f=open(filename)
	result = json.load(f)
	f.close()
	nosyllsperline = flatten(result['No. of syllables per line']) #This includes a list of lists, for the case we have more than one stanza
	if isinstance(nosyllsperline, list):
		nosylls = nosylls + nosyllsperline

goldvals = [gold_num]*len(nosylls)

print (accuracy_score(goldvals,nosylls))
print (sorted(set(nosylls)))
print (mean_absolute_error(goldvals,nosylls))
#print (confusion_matrix(goldvals,nosylls,labels=sorted(set(nosylls))))
print (len(nosylls))
