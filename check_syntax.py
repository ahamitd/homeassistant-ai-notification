import py_compile
import sys
import os

files = [
    "custom_components/ai_notification/__init__.py",
    "custom_components/ai_notification/config_flow.py",
    "custom_components/ai_notification/const.py"
]

has_error = False
for f in files:
    if not os.path.exists(f):
        print(f"File not found: {f}")
        continue
    try:
        py_compile.compile(f, doraise=True)
        print(f"OK: {f}")
    except py_compile.PyCompileError as e:
        print(f"ERROR in {f}: {e}")
        has_error = True
    except Exception as e:
        print(f"EXCEPTION in {f}: {e}")
        has_error = True

if has_error:
    sys.exit(1)
