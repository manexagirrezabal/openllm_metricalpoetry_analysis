import ollama
import sys
import os

prompt = 'Please write me a poem with three stanzas'


f=open("prompts.txt")
prompts = [line.strip() for line in f]
f.close()

f=open("topics.txt")
topics = [line.strip() for line in f]
f.close()

ident = 0
for topic in topics:
	print (topic)
	for prompt in prompts:
		print (prompt)
		#For each of the prompts we start with an empty memory
	        #We keep it this way to make it easier to generate varied poems, without repetition, without tweaking the temperature and top_p parameters

		messages = []
		for k in range(10):
			if os.path.isfile("responses/prompt"+str(ident)):
				print ("Ignore this file")
				print (ident)
				ident+=1
				continue
			print (ident)
			print (prompt + " about "+topic)
			wholeprompt = prompt + " about "+topic

			response = ollama.chat(model='llama2:70b', messages=messages + [
		  {
		    'role': 'user',
		    'content': wholeprompt,
		  },
		])
			resp = response['message']['content']

			fw=open("responses/prompt"+str(ident),"w")
			fw.write(wholeprompt+ " " + str(k))
			fw.close()

			fw=open("responses/response"+str(ident),"w")
			fw.write(resp)
			fw.close()



			current_response_user = {}
			current_response_user['role']="user"
			current_response_user['content']=wholeprompt
			messages.append(current_response_user)

			current_response_assis = {}
			current_response_assis['role']="assistant"
			current_response_assis['content']=resp
			messages.append(current_response_assis)
			ident +=1
