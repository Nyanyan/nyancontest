import subprocess

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
#events = [0, 1, 8, 13, 14]
events = [8]

for i in events:
    arg = sessions[i]
    print(arg)
    command = ['python', 'makehtml.py', arg]
    subprocess.run(command)