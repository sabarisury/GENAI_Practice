#Chat BOT AI POWERED
import lmstudio as lms

model = lms.llm("google/gemma-4-e2b")

file_path = '/Users/sabarisury/Desktop/GENAI_LLM_LOCAL/GENAI_Practice/big_text_for_summary.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    prompt_text = file.read()

print(model.count_tokens(prompt_text))

chunk_size = 2500

chunks = [
    prompt_text[i:i + chunk_size] for i in range(0, len(prompt_text), chunk_size)
]

chunk_summaries = []

for i, chunk in enumerate(chunks):
    response = model.respond(
        f"Summarize this text clearly:\n\n{chunk}"
    )
    
    summary = response.content
    chunk_summaries.append(summary)

    print(f"Chunk {i+1} done")

final_input = "\n\n".join(chunk_summaries)

final_summary = model.respond(
    f"Your input is list summary of big text ,Combine all summary and refine this into a final summary:\n\n{final_input}"
)

print("\nFINAL SUMMARY:\n")
print(final_summary.content)


rating = model.respond(
    f"Based on this summary can you rate the candiate within ['Poor','Average','Good','Excellent'] {final_summary}"
)

print("Candiate Rating: ", rating)