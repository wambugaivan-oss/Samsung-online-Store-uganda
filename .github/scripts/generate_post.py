import os
import json
import google.generativeai as genai

# 1. Setup the AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# 2. Ask AI for the latest tech trend in Uganda
prompt = "Find a trending smartphone currently popular in Uganda. Provide a name, a price in UGX, and a short 1-sentence description."
response = model.generate_content(prompt)

# 3. Process the AI's response (simplified)
# Note: In a real scenario, you'd add error handling here.
# For now, we assume the AI returns a clean response.
new_product = {
    "name": "Trending Phone", # Ideally, parse this from response.text
    "price": "Market Price",
    "description": response.text,
    "image": "https://via.placeholder.com/150"
}

# 4. Read the existing products and append the new one
try:
    with open('products.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

data.append(new_product)

# 5. Save the updated list back to the file
with open('products.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Product list updated successfully!")

