import os
import json
import google.generativeai as genai

# 1. Setup the AI
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    print(f"Error setting up AI: {e}")
    exit(1)

# 2. Ask AI for the trend
prompt = "Find one trending Samsung or Google Pixel phone in Uganda today. Return ONLY a JSON object with: name, price_ugx, and description."
response = model.generate_content(prompt)

# 3. Create the new item
new_item = {
    "name": "Samsung Galaxy S24 Ultra", # Script will update this
    "price": "5,100,000 UGX",
    "description": response.text,
    "image": "https://m.media-amazon.com/images/I/71RZA9S878L.jpg"
}

# 4. Find the products.json file (Checking two locations just in case)
file_path = 'products.json'
if not os.path.exists(file_path):
    file_path = '../../products.json' # Look in the main folder

# 5. Save the update
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
    data.append(new_item)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Successfully updated products.json")
except Exception as e:
    print(f"Could not update file: {e}")
    exit(1)
