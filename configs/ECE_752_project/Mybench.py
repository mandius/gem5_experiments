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
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = DATA_ROOT + B_NAME +  "/input.source"
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = "280"

bzip2 = Process()
bzip2.executable =  BINARY_PATH
bzip2.cmd = [bzip2.executable] + [IN_PATH, IN_ARG]
bzip2.output = "bzip2.out"


#libquantum
B_NAME = "libquantum"
BINARY_PATH= EXE_ROOT + "libquantum_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = ""
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = "1397 8"

libquantum = Process()
libquantum.executable =  BINARY_PATH
libquantum.cmd = [libquantum.executable] + [IN_ARG]
libquantum.output = "libquantum.out"

#gamess
B_NAME = "gamess"
BINARY_PATH= EXE_ROOT + "gamess_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = DATA_ROOT + B_NAME +  "/cytosine.2.config"
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = ""

gamess = Process()
gamess.executable =  BINARY_PATH
gamess.cmd = [gamess.executable] + [IN_PATH]
gamess.output = "gamess.out"


#gobmk
B_NAME = "gobmk"
BINARY_PATH= EXE_ROOT + "gobmk_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = DATA_ROOT + B_NAME +  "/13x13.tst"
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = ""

gobmk = Process()
gobmk.executable =  BINARY_PATH
gobmk.cmd = [gobmk.executable] + [IN_PATH]
gobmk.output = "gobmk.out"


#GemsFDTD
B_NAME = "GemsFDTD"
BINARY_PATH= EXE_ROOT + "GemsFDTD_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = ""
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = "/"

GemsFDTD = Process()
GemsFDTD.executable =  BINARY_PATH
GemsFDTD.cmd = [GemsFDTD.executable] + [IN_PATH]
GemsFDTD.output = "GemsFDTD.out"


#soplex
B_NAME = "soplex"
BINARY_PATH= EXE_ROOT + "soplex_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = "pds-50.mps"
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = "-sl -e -m45000"

soplex = Process()
soplex.executable =  BINARY_PATH
soplex.cmd = [soplex.executable] + [IN_ARG, IN_PATH]
soplex.output = "soplex.out"


#gromacs
B_NAME = "gromacs"
BINARY_PATH= EXE_ROOT + "gromacs_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = " "
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = "-silent -deffnm gromacs -nice 0"

gromacs = Process()
gromacs.executable =  BINARY_PATH
gromacs.cmd = [gromacs.executable] + [IN_ARG, IN_PATH]
gromacs.output = "gromacs.out"

#milc
B_NAME = "milc"
BINARY_PATH= EXE_ROOT + "milc_base.i386-m32-gcc42-nn"
#BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/bzip2/bzip2_base.linux32.ia32"
IN_PATH = DATA_ROOT + B_NAME + "/su3imp.in"
#IN_PATH = "/home/maninder/Projects/Gem5/spec2006/bzip2/input/input.source"
IN_ARG = " "

milc = Process()
milc.executable =  BINARY_PATH
milc.cmd = [milc.executable] + [IN_ARG, IN_PATH]
milc.output = "milc.out"


