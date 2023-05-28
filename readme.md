


#To Build the Gem5:

1. scons build/X86/gem5.fast

#To run a sample sieve of Eratosthenes program for the three modes:
#1. without speculative scheduling
#2. with speculative scheduling but without load filtering
#3. with speculative scheduling and with load filtering
cd configs/ECE_752_project
gcc test2.c -o test -static
cd ../..
source setup.csh
./run 

#Key results are captured in the file <log_book>
#Project Report =>  Final_Report.pdf
