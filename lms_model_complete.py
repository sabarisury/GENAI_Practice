import lmstudio as lms

model = lms.llm("google/gemma-4-e2b")

response_complete = model.complete("Hi My Name is Sabari ! How are you ! I am telling you a story , " \
"There is one big Lion in forest then")
print(response_complete)