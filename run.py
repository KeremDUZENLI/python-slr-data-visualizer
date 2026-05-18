import os
import subprocess


package_name = "xamples"
files = os.listdir(package_name)

for filename in files:
    if filename.endswith(".py"):
        module_name = filename[:-3]
        full_module_path = f"{package_name}.{module_name}"
        
        print(f"\n--- Running: python -m {full_module_path} ---")
        subprocess.run(["python", "-m", full_module_path])
