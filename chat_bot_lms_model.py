import lmstudio as  lms
model = lms.llm("google/gemma-4-e2b")

history = []

while True:
    print("To Stop Conversation , Please enter 'exit', or 'quit', or 'stop' ")
    user_input = input("Start Your Conversation: ")
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Happy Conversation Good Bye !!")
        break
    else:
        history.append({"role":"user","content":user_input})
    print("AI Assistant: ",end="")
    with model.respond_stream({"messages": history}) as streamed_data:
        response = ""
        for chunk in streamed_data:
            print(chunk.content,end="",flush=True)
            response += chunk.content
        print()
        history.append({"role":"assistant","content":response})

