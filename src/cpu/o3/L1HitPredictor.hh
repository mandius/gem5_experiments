#include <iostream>
#include  "debug/DBGCUR.hh"

#ifndef L1HitPredictor_guard
#define L1HitPredictor_guard


namespace gem5{
namespace o3{


class L1HitPredictor{
	

	private: 
		int* history_table;
		int* critical_table;
		int* silent_bits;
		int global_counter;
		int silence_update_cycle;
		int history_table_size_local;
		



	public:

		int is_enabled;

		L1HitPredictor(int history_table_size, int critical_table_size){
			history_table = new int[history_table_size];
			std::fill(history_table, history_table + history_table_size, 0);
			critical_table = new int[critical_table_size];
			std::fill(critical_table, critical_table + critical_table_size, 0);
			silent_bits = new int[history_table_size];
			std::fill(silent_bits, silent_bits + history_table_size, 0);
	
			history_table_size_local = history_table_size;

			global_counter=0;
			is_enabled=0;
			silence_update_cycle =0;
			reset_silent_bits();
			
		}

		void reset_silent_bits(){
			for( int i=0; i< history_table_size_local; i++){
				silent_bits[i]=0;
			}
		}


		void silence_cycle_update(){

			if(silence_update_cycle == 1000){
				silence_update_cycle=0;
			} else {
				silence_update_cycle++;
			}

			if(silence_update_cycle==0){
				reset_silent_bits();
			}


		}

			

		void note_L1_hit(unsigned int pc){
			if(is_enabled) {
				DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Noted\n");
				pc = pc & 0x7ff; 

				if(global_counter!=15) {
					global_counter++;
				}
			
				if(!silent_bits[pc]){

					//Set the silence bit on going from a saturated state to a non saturated state
					if(history_table[pc]==0){
						silent_bits[pc]=1;
					}
					if(history_table[pc] !=3){
						history_table[pc]++;
					}
				}
				
				silence_cycle_update();


			}
		}

		void note_L1_miss(unsigned int pc){
			if(is_enabled){
				DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Noted\n");
				pc = pc & 0x7ff; 

				if(global_counter-2 >=0) {
					global_counter-= 2;
				} else {
					global_counter=0;
				}
			
				if( !silent_bits[pc]){ 
					//Set the silence bit on going from a saturated state to a non saturated state
					if(history_table[pc]==3){
						silent_bits[pc]=1;
					}

					if(history_table[pc] !=0){
						history_table[pc]--;
					}
				}

				silence_cycle_update();
			}
		}


		void note_criticality( unsigned int pc , int criticality){
			if(is_enabled){
				pc = pc & 0x1fff; 
				if(criticality) {
					if(critical_table[pc] != 15){
						critical_table[pc] ++;
					}
				}else {
					if(critical_table[pc] != 0){
						critical_table[pc] --;
					}
				}
			}
		}
			
		int ret_prediction(unsigned int pc){
			if(is_enabled){
				pc = pc & 0x7ff;
				
				if(!silent_bits[pc]){
					if(history_table[pc]>=2){
						DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Predicted\n");
						return 1;
					} else {
						DPRINTF(DBGCUR, "[L1HitPredictor] L1 Miss Predicted\n");
						return 0;
					}
				} else {	
					
					if(global_counter>=8){
						DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Predicted\n");
						return 1;
					} else {
						DPRINTF(DBGCUR, "[L1HitPredictor] L1 Miss Predicted\n");
						return 0;
					}
				}
			} else { return 1;}
		}			
		

		
};
}
}


#endif
