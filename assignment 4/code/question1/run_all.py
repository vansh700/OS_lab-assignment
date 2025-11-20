import subprocess

scripts = ['script1.py', 'script2.py', 'script3.py']

for script in scripts:
    print(f"Executing {script}...")
    subprocess.call(['python3', script])
