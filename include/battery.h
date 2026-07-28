#ifndef BATTERY_H
#define BATTERY_H


typedef struct {

    float voltage;
    float temperature;
    float state_of_charge;
    float health;

} BatteryCell;


// Initialize battery pack
void initializeBattery(BatteryCell cells[], int number_of_cells);


// Simulate charging
void chargeBattery(BatteryCell cells[], int number_of_cells);


// Simulate discharging
void dischargeBattery(BatteryCell cells[], int number_of_cells);


#endif