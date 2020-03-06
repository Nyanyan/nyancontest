import subprocess

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy', 'FloppyGhost', 'Void']

for arg in events:
    print(arg)
    command = ['python', 'makehtml.py', arg]
    subprocess.run(command)