#ifndef FAULTS_H
#define FAULTS_H

#include "battery.h"


// Checks battery for dangerous conditions
void checkFaults(BatteryCell cells[], int number_of_cells);


#endif