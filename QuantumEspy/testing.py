import os
import json 
import subprocess 
'''
files = os.listdir()
x = os.path.join('c:', 'pw.x')
for i in files:
    if x in files:
        data_captured = json.loads(open(x).read())
        print(data_captured)
    else:
        print("File doesn't exist !!")
'''

outdir = subprocess.check_output("plocate espresso.scf.in", shell=True)
#quantum_file = subprocess.check_output(f"cat {outdir}/espresso.scf.in", shell=True)
#(out, err) = proc.communicate()
#print("program File:", quantum_file)
#out = f"{outdir}".removeprefix("espresso.scf.in")
print("Outdir:", outdir)
