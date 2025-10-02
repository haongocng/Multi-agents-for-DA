import subprocess
import sys

# Install xgboost using pip
subprocess.check_call([sys.executable, "-m", "pip", "install", "xgboost"])