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
		int global_counter;
		



	public:

		int is_enabled;

		L1HitPredictor(int history_table_size, int critical_table_size){
			history_table = new int[history_table_size];
			std::fill(history_table, history_table + history_table_size, 0);
			critical_table = new int[critical_table_size];
			std::fill(critical_table, critical_table + critical_table_size, 0);
			global_counter=0;
			is_enabled=0;
			
		}

		void note_L1_hit(unsigned int pc){
			if(is_enabled) {
				DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Noted\n");
				pc = pc & 0x7ff; 

				if(global_counter!=15) {
					global_counter++;
				}
			
				if(history_table[pc] !=2){
					history_table[pc]++;
				}
			}
		}

		void note_L1_miss(unsigned int pc){
			if(is_enabled){
				DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Noted\n");
				pc = pc & 0x7ff; 

				if(global_counter!=0) {
					global_counter-= 2;
				}
			
				if(history_table[pc] !=0){
					history_table[pc]--;
				}
			}
		}


		void note_criticality( unsigned int pc , int criticality){
			if(is_enabled){
				pc = pc & 0x7ff; 
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
				if(global_counter>=8){
					DPRINTF(DBGCUR, "[L1HitPredictor] L1 Hit Predicted\n");
					return 1;
				} else {
					DPRINTF(DBGCUR, "[L1HitPredictor] L1 Miss Predicted\n");
					return 0;
				}
			} else { return 1;}
		}			
		

		
};
}
}


#endif
