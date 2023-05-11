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
test.cmd = [test.executable] + ["/home/maninder/Projects/Gem5/spec_execs/data/in_file"]
test.input =  "/home/maninder/Projects/Gem5/spec_execs/data/in_file"
#401.bzip2
B_NAME = "bzip2"
BINARY_PATH= EXE_ROOT + "bzip2_base.i386-m32-gcc42-nn"
IN_PATH =  DATA_ROOT + B_NAME +  "/input.source"
IN_ARG = " 280"

bzip2 = Process()
bzip2.executable =  BINARY_PATH
bzip2.cmd = [bzip2.executable] + [IN_PATH, IN_ARG]
bzip2.output = "bzip2.out"


#libquantum
B_NAME = "libquantum"
BINARY_PATH= EXE_ROOT + "libquantum_base.i386-m32-gcc42-nn"
IN_PATH = ""
IN_ARG = "1397 8"

libquantum = Process()
libquantum.executable =  BINARY_PATH
libquantum.cmd = [libquantum.executable] + [IN_ARG]
libquantum.output = "libquantum.out"

#gamess
B_NAME = "gamess"
BINARY_PATH= EXE_ROOT + "gamess_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT + B_NAME +  "/cytosine.2.config"
IN_ARG = ""

gamess = Process()
gamess.executable =  BINARY_PATH
gamess.cmd = [gamess.executable] + [IN_PATH]
gamess.output = "gamess.out"


#gobmk
B_NAME = "gobmk"
BINARY_PATH= EXE_ROOT + "gobmk_base.linux32.ia32"

IN_PATH = DATA_ROOT + B_NAME +  "/13x13.tst"
IN_PATH = "/home/maninder/Projects/Gem5/spec2006/gobmk/score2.tst"
IN_ARG =  "-opts --quiet --mode gtp"


gobmk = Process()
gobmk.executable =  BINARY_PATH
gobmk.cmd = [gobmk.executable] + [IN_ARG]
gobmk.input = IN_PATH
gobmk.output = "gobmk.out"


#GemsFDTD
B_NAME = "GemsFDTD"
#BINARY_PATH= EXE_ROOT + "GemsFDTD_base.i386-m32-gcc42-nn"
BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/GemsFDTD/GemsFDTD_base.x86_64_sse"
IN_PATH = ""
IN_ARG = "/"

GemsFDTD = Process()
GemsFDTD.executable =  BINARY_PATH
GemsFDTD.cmd = [GemsFDTD.executable] + [IN_ARG]
GemsFDTD.output = "GemsFDTD.out"


#soplex
B_NAME = "soplex"
BINARY_PATH= EXE_ROOT + "soplex_base.x86_64_sse"
IN_PATH = DATA_ROOT+B_NAME+"/pds-50.mps"
IN_ARG = "-sl -e -m45000"

soplex = Process()
soplex.executable =  BINARY_PATH
soplex.cmd = [soplex.executable] + [IN_ARG, IN_PATH]
soplex.output = "soplex.out"


#gromacs
B_NAME = "gromacs"
#BINARY_PATH= EXE_ROOT + "gromacs_base.i386-m32-gcc42-nn"
BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/gromacs/gromacs_base.linux32.ia32"
IN_PATH = " "
IN_ARG = "-silent -deffnm gromacs -nice 0"

gromacs = Process()
gromacs.executable =  BINARY_PATH
gromacs.cmd = [gromacs.executable] + [IN_ARG, IN_PATH]
gromacs.output = "gromacs.out"

#milc
B_NAME = "milc"
BINARY_PATH= EXE_ROOT + "milc_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT + B_NAME + "/su3imp.in"


milc = Process()
milc.executable =  BINARY_PATH
milc.cmd = [milc.executable] 
milc.input = IN_PATH
milc.output = "milc.out"


#mcf
B_NAME = "mcf"
BINARY_PATH= EXE_ROOT + "mcf_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/inp.in"
IN_ARG = ""

mcf = Process()
mcf.executable =  BINARY_PATH
mcf.cmd = [mcf.executable] + [IN_ARG, IN_PATH]
mcf.output = "mcf.out"

#leslie3d
B_NAME = "leslie3d"
BINARY_PATH= EXE_ROOT + "leslie3d_base.x86_64_sse"
IN_PATH = DATA_ROOT+B_NAME+ "/leslie3d.in"
IN_ARG = ""

leslie3d = Process()
leslie3d.executable =  BINARY_PATH
leslie3d.cmd = [leslie3d.executable] + [IN_PATH] 
leslie3d.input = IN_PATH
leslie3d.output = "leslie3d.out"


#namd
B_NAME = "namd"
BINARY_PATH= EXE_ROOT + "namd_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/namd.input"
IN_ARG = " --input "+ IN_PATH+ " --iterations 38 "

namd = Process()
namd.executable =  BINARY_PATH
namd.cmd = [namd.executable] + [IN_ARG]
namd.output = "namd.out"


#povray
B_NAME = "povray"
BINARY_PATH= EXE_ROOT + "povray_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/SPEC-benchmark-ref.ini"
IN_ARG = ""

povray = Process()
povray.executable =  BINARY_PATH
povray.cmd = [povray.executable] + [IN_ARG, IN_PATH]
povray.output = "povray.out"



#hmmer
B_NAME = "hmmer"
BINARY_PATH= EXE_ROOT + "hmmer_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/nph3.hmm"
IN_PATH2 = DATA_ROOT+B_NAME+ "/swiss41"
IN_ARG = ""

hmmer = Process()
hmmer.executable =  BINARY_PATH
hmmer.cmd = [hmmer.executable] + [IN_PATH] + [IN_PATH2]
hmmer.output = "hmmer.out"


#sjeng
B_NAME = "sjeng"
BINARY_PATH= EXE_ROOT + "sjeng_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/ref.txt"
IN_ARG = ""

sjeng = Process()
sjeng.executable =  BINARY_PATH
sjeng.cmd = [sjeng.executable] + [IN_ARG, IN_PATH]
sjeng.output = "sjeng.out"


#h264ref
B_NAME = "h264ref"
BINARY_PATH= EXE_ROOT + "h264ref_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/foreman_ref_encoder_baseline.cfg"
IN_ARG = ""

h264ref = Process()
h264ref.executable =  BINARY_PATH
h264ref.cmd = [h264ref.executable] + [IN_ARG, IN_PATH]
h264ref.output = "h264ref.out"



#lbm
B_NAME = "lbm"
BINARY_PATH= EXE_ROOT + "lbm_base.i386-m32-gcc42-nn"
BINARY_PATH= "/home/maninder/Projects/Gem5/spec2006/lbm/lbm_base.x86_64_sse"
IN_PATH = DATA_ROOT+B_NAME+ "/100_100_130_ldc.of]"
IN_ARG = "3000 reference.dat 0 0 [" + IN_PATH 

lbm = Process()
lbm.executable =  BINARY_PATH
lbm.cmd = [lbm.executable] + [IN_ARG] 
lbm.output = "lbm.out"


#omnetpp
B_NAME = "omnetpp"
BINARY_PATH= EXE_ROOT + "omnetpp_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/omnetpp.ini"
IN_ARG = ""

omnetpp = Process()
omnetpp.executable =  BINARY_PATH
omnetpp.cmd = [omnetpp.executable] + [IN_PATH]
omnetpp.output = "omnetpp.out"


#astar
B_NAME = "astar"
BINARY_PATH= EXE_ROOT + "astar_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/rivers.cfg"
IN_ARG = ""

astar = Process()
astar.executable =  BINARY_PATH
astar.cmd = [astar.executable] + [IN_ARG, IN_PATH]
astar.output = "astar.out"

#sphinx
B_NAME = "sphinx"
BINARY_PATH= EXE_ROOT + "sphinx_base.i386-m32-gcc42-nn"
IN_PATH = DATA_ROOT+B_NAME+ "/an4.ctl"+ " . " + DATA_ROOT+B_NAME+ "/args.an4.test"
IN_ARG = ""

sphinx = Process()
sphinx.executable =  BINARY_PATH
sphinx.cmd = [sphinx.executable] + [IN_ARG, IN_PATH]
sphinx.output = "sphinx.out"

