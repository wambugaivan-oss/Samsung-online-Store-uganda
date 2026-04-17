name: Daily Uganda Tech Trends
on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Run Debug Script
        run: |
          echo "Checking folder structure:"
          ls -R
          echo "Running Python version:"
          python --version
          echo "Attempting to run script:"
          python generate_post.py || echo "FAILED WITH EXIT CODE $?"
