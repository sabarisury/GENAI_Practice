import lmstudio as lms
model = lms.llm("google/gemma-4-e2b")

with model.complete_stream("Hi My Name is Sabari ! How are you ! I am telling you a story , " \
"There is one big Lion in forest then") as stream_data:
    for chunk in stream_data:
        print(chunk.content,end="",flush=True)