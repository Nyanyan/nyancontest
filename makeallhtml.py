import subprocess

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy', 'FloppyGhost', 'Void', 'Kilominx']

for arg in events:
    print(arg)
    command = ['python3', 'makehtml.py', arg]
    subprocess.run(command)

