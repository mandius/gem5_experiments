import m5
from m5.objects import *

# Add the common scripts to our path
m5.util.addToPath("../")

from common import SimpleOpts



top_dir = "/home/maninder/private/ECE752/project/spec/benchspec/CPU2006/"
binary_dir = "/home/maninder/private/ECE752/project/spec/benchspec/CPU2006/"
data_dir = "/home/maninder/private/ECE752/project/spec/benchspec/CPU2006/401.bzip2/data/all/input"


#401.bzip2
b_name = "401.bzip2"
#binary_dir= top_dir + b_name +  "/exe/"
data_dir = top_dir + b_name +  "/data/test/input/"
bzip2 = Process()
#bzip2.executable =  binary_dir+'bzip2_base.amd64-m32-gcc42-nn'
bzip2.executable = "/home/maninder/private/ECE752/project/gem5_experiments/configs/ECE_752_project/test"
data=data_dir+'dryer.jpg'
#bzip2.cmd = [bzip2.executable] + [data, '1']
bzip2.cmd = [bzip2.executable]
bzip2.output = 'input.program.out'
