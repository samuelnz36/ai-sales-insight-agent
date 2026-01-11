from llama.llama_client import llama_response

with open("agent_prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

print(llama_response(prompt))
