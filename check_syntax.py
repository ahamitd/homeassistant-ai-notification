import py_compile
import sys
import os

files = [
    "custom_components/notifyai/__init__.py",
    "custom_components/notifyai/config_flow.py",
    "custom_components/notifyai/const.py"
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
