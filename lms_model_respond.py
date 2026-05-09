import lmstudio as lms
model = lms.llm('google/gemma-4-e2b')


#respond - remembers history -- one time 1. 🗣️ Chat Mode (like ChatGPT) 👉 remembers conversation
response_respond = model.respond("Hi My Name is Sabari ! How are you ! I am telling you a story , There is one big Lion in forest then")
print(response_respond.content)

