from llama.llama_client import llama_response

prompt = """
You are a business analyst.

Sales summary:
- Total sales declined in the last quarter
- West and Central regions underperformed
- Furniture category showed volatility

Explain possible reasons in simple business language.
"""

print(llama_response(prompt))
