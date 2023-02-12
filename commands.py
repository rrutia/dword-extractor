import sys
import r2pipe

r = r2pipe.open()
r.cmd('aaa')

error = None
try:
    result = r.cmd("pdf @main")
except Exception as e:
    error = str(e)

if error:
    print("Error: ", error)
else:
    lines = result.splitlines()
    for line in lines:
        index = line.find("'")
        if index != -1:
            letter = line[index+1]
            print(letter)
