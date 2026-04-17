import sys
import traceback

try:
    # ... your existing code ...
except Exception:
    traceback.print_exc()
    sys.exit(1)
