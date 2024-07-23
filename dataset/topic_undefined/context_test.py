import ollama
import sys

prompt = 'Please write me a poem with three stanzas'


f=open("prompts.txt")
prompts = [line.strip() for line in f]
f.close()

ident = 0
for prompt in prompts:
	#For each of the prompts we start with an empty memory
	#We keep it this way to make it easier to generate varied poems, without repetition, without tweaking the temperature and top_p parameters
	messages = []
	for k in range(10):
		print (ident)
		response = ollama.chat(model='llama2:70b', messages=messages + [
	  {
	    'role': 'user',
	    'content': prompt,
	  },
	])
		resp = response['message']['content']

		fw=open("responses/prompt"+str(ident),"w")
		fw.write(prompt+ " " + str(k))
		fw.close()

		fw=open("responses/response"+str(ident),"w")
		fw.write(resp)
		fw.close()



		current_response_user = {}
		current_response_user['role']="user"
		current_response_user['content']=prompt
		messages.append(current_response_user)

		current_response_assis = {}
		current_response_assis['role']="assistant"
		current_response_assis['content']=resp
		messages.append(current_response_assis)
		ident +=1
