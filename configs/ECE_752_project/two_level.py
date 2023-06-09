# -*- coding: utf-8 -*-
# Copyright (c) 2015 Jason Power
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" This file creates a single CPU and a two-level cache system.
This script takes a single parameter which specifies a binary to execute.
If none is provided it executes 'hello' by default (mostly used for testing)

See Part 1, Chapter 3: Adding cache to the configuration script in the
learning_gem5 book for more information about this script.
This file exports options for the L1 I/D and L2 cache sizes.

IMPORTANT: If you modify this file, it's likely that the Learning gem5 book
           also needs to be updated. For now, email Jason <power.jg@gmail.com>

"""

# import the m5 (gem5) library created when gem5 is built
import m5

# import all of the SimObjects
from m5.objects import *
from gem5.runtime import get_runtime_isa

# Add the common scripts to our path
m5.util.addToPath("../")

# import the caches which we made
from caches import *

import Mybench

# import the SimpleOpts module
from common import *

# Default to running 'hello', use the compiled ISA to find the binary
# grab the specific path to the binary
thispath = os.path.dirname(os.path.realpath(__file__))
default_binary = os.path.join(
    thispath,
    "../../",
    "tests/test-progs/hello/bin/x86/linux/hello",
)

# Binary to execute
SimpleOpts.add_option("benchmark", nargs="?", default="bzip2")

#Add option for Issue to Execute Delay
SimpleOpts.add_option("I2E_delay", nargs="?", default="1")


#adding an option for the max number of instructions to be executed per thread.
SimpleOpts.add_option("spec_sched", nargs="?", default="True")

SimpleOpts.add_option("L1preden", nargs="?", default="True")

#adding an option for the max number of instructions to be executed per thread.
SimpleOpts.add_option("maxinsts", nargs="?", default="1000000")





# Finalize the arguments and grab the args so we can pass it on to our objects
args = SimpleOpts.parse_args()

# create the system we are going to simulate
system = System()

# Set the clock frequency of the system (and all of its children)
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = "1GHz"
system.clk_domain.voltage_domain = VoltageDomain()

# Set up the system
system.mem_mode = "timing"  # Use timing accesses
system.mem_ranges = [AddrRange("1GB")]  # Create an address range

# Create an O3 CPU
system.cpu = O3CPU()
system.cpu.issueToExecuteDelay = args.I2E_delay
system.cpu.spec_sched = args.spec_sched
system.cpu.L1preden = args.L1preden

### Fixed parameters according to the configuration
system.cpu.LQEntries = 72
system.cpu.SQEntries = 48
system.cpu.max_insts_any_thread = args.maxinsts;


# Create an L1 instruction and data cache
system.cpu.icache = L1ICache(args)
system.cpu.dcache = L1DCache(args)

# Connect the instruction and data caches to the CPU
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# Create a memory bus, a coherent crossbar, in this case
system.l2bus = L2XBar()

# Hook the CPU ports up to the l2bus
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# Create an L2 cache and connect it to the l2bus
system.l2cache = L2Cache(args)
system.l2cache.connectCPUSideBus(system.l2bus)

# Create a memory bus
system.membus = SystemXBar()

# Connect the L2 cache to the membus
system.l2cache.connectMemSideBus(system.membus)

# create the interrupt controller for the CPU
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Connect the system up to the membus
system.system_port = system.membus.cpu_side_ports

# Create a DDR3 memory controller
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports



# Create a process for a simple "Hello World" application
#process = Process()
# Set the command
# cmd is a list which begins with the executable (like argv)
#process.cmd = [args.binary]
# Set the cpu to use the process as its workload and create thread contexts
if args.benchmark == 'bzip2':
	process = Mybench.bzip2
elif args.benchmark == 'libquantum':
	process = Mybench.libquantum
elif args.benchmark == 'gamess':
	process = Mybench.gamess
elif args.benchmark == 'gobmk':
	process = Mybench.gobmk
elif args.benchmark == 'GemsFDTD':
	process = Mybench.GemsFDTD
elif args.benchmark == 'soplex':
	process = Mybench.soplex
elif args.benchmark == 'test':
	process = Mybench.test
elif args.benchmark == 'gromacs':
	process = Mybench.gromacs
elif args.benchmark == 'milc':
	process = Mybench.milc
elif args.benchmark == 'mcf':
	process = Mybench.mcf
elif args.benchmark == 'leslie3d':
	process = Mybench.leslie3d
elif args.benchmark == 'namd':
	process = Mybench.namd
elif args.benchmark == 'povray':
	process = Mybench.povray
elif args.benchmark == 'hmmer':
	process = Mybench.hmmer
elif args.benchmark == 'sjeng':
	process = Mybench.sjeng
elif args.benchmark == 'h264ref':
	process = Mybench.h264ref
elif args.benchmark == 'lbm':
	process = Mybench.lbm
elif args.benchmark == 'omnetpp':
	process = Mybench.omnetpp
elif args.benchmark == 'astar':
	process = Mybench.astar
elif args.benchmark == 'sphinx':
	process = Mybench.sphinx
else:
	print("Benchmark not found")
	exit(0)


system.workload = SEWorkload.init_compatible(process.executable)
system.cpu.workload = process

print("Process Information:")
print(process.cmd)
print("\n")

	
system.cpu.createThreads()

# set up the root SimObject and start the simulation
root = Root(full_system=False, system=system)
# instantiate all of the objects we've created above
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print("Exiting @ tick %i because %s" % (m5.curTick(), exit_event.getCause()))
