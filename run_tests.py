import subprocess, sys
subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], check=False)
