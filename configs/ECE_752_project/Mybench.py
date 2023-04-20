import os
import m5
from m5.objects import *

EXE_ROOT = os.getenv('EXE_ROOT')
DATA_ROOT = os.getenv('DATA_ROOT')
GEM5_CONFIG = os.getenv('GEM5_CONFIG')

print("EXE_ROOT:")
print(EXE_ROOT)
print("\n")

print("DATA_ROOT:")
print(DATA_ROOT)
print("\n")


print("GEM5_CONFIG:")
print(GEM5_CONFIG)
print("\n")


# Add the common scripts to our path
m5.util.addToPath("../")

from common import SimpleOpts


#Test

test = Process()
test.executable = GEM5_CONFIG + '/' +"test"
test.cmd = [test.executable]
test.output = 'test.out'

#401.bzip2
B_NAME = "bzip2"
BINARY_PATH= EXE_ROOT + "bzip2_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT + B_NAME +  "/input/input.source"
IN_ARG = "280"

bzip2 = Process()
bzip2.executable =  BINARY_PATH
bzip2.cmd = [bzip2.executable] + [IN_PATH, IN_ARG]
bzip2.output = "bzip2.out"
