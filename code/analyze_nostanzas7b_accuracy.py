import pandas as pd
import glob
import json
import numpy as np
from sklearn.metrics import mean_absolute_error, accuracy_score, confusion_matrix, classification_report
import sys

fi = pd.read_excel("../prompts_gold_values.xlsx")

gold_num = int(sys.argv[1])

prompts_of_interest = list(fi[fi['No of stanzas'] == gold_num]['Unnamed: 2'])

responsenums_of_interest = []
for file in glob.glob("../dataset/topic_defined/responses7b/prompt*"):
	#We get the content of the prompt and we remove the last word, as it is just a number from 0 to 9
	f=open(file)
	prompt = " ".join(f.read().strip().split(" ")[:-1])
	f.close()
	if prompt in prompts_of_interest:
		response_num = file[:-4].split("t")[-1] #All files have the following name: DIR/DIR/.../promptDIG+.txt
		responsenums_of_interest.append(response_num)

nostanzas = []
for rnoi in responsenums_of_interest:
	filename = "../dataset/topic_defined/responses7b/response"+rnoi+"_clean.txt.analysis"
	f=open(filename)
	result = json.load(f)
	f.close()
	nostanzas.append(result['stanzacount'])

goldvals = [gold_num]*len(nostanzas)

print (classification_report(goldvals,nostanzas))
print (confusion_matrix(goldvals,nostanzas))
print (accuracy_score(goldvals,nostanzas))

print ()
print (mean_absolute_error(goldvals,nostanzas))
print (len(nostanzas))
