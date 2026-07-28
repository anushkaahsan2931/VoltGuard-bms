#ifndef LOGGER_H
#define LOGGER_H

#include "battery.h"


void logEvent(char message[]);


void saveTelemetry(BatteryCell cells[], int number_of_cells);


#endif