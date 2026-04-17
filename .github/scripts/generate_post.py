import os
import json
import sys

# Print to log so we know it started
print("Script started successfully!")

# Check if API Key exists
if "GEMINI_API_KEY" not in os.environ:
    print("Error: GEMINI_API_KEY not found!")
    sys.exit(1)

try:
    # Minimal test to see if it crashes
    print("Attempting to load products.json...")
    with open('products.json', 'r') as f:
        data = json.load(f)
    print(f"Successfully loaded {len(data)} items.")
except Exception as e:
    print(f"CRASHED: {e}")
    sys.exit(1)
