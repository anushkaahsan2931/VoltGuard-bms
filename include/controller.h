#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "battery.h"


typedef enum
{
    IDLE,
    CHARGING,
    DISCHARGING,
    FAULT

} BatteryState;


// Checks battery conditions
void monitorBattery(BatteryCell cells[], int number_of_cells);


// Update current system state
void updateState(BatteryState *state, BatteryCell cells[], int number_of_cells);


// Display current state
void printState(BatteryState state);


#endif