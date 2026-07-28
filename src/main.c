#include <stdio.h>
#include "battery.h"
#include "controller.h"
#include "faults.h"
#include "logger.h"
#include "balancing.h"


int main()
{
    BatteryState system_state = IDLE;

    BatteryCell battery_pack[4];


    initializeBattery(battery_pack, 4);


    printf("VoltGuard Battery Simulation\n\n");


    printf("Initial State:\n");


    for(int i = 0; i < 4; i++)
    {
        printf("Cell %d: %.2fV | %.2f%% SOC\n",
        i + 1,
        battery_pack[i].voltage,
        battery_pack[i].state_of_charge);
    }


    printf("\nCharging...\n\n");


    chargeBattery(battery_pack, 4);


    for(int i = 0; i < 4; i++)
    {
        printf("Cell %d: %.2fV | %.2f%% SOC\n",
        i + 1,
        battery_pack[i].voltage,
        battery_pack[i].state_of_charge);
    }
    printf("\nChecking battery safety...\n");

    monitorBattery(battery_pack, 4);
    printf("\nRunning fault analysis...\n");

    checkFaults(battery_pack, 4);

    logEvent("Battery analysis completed");
    printf("\nUpdating system state...\n");

    updateState(&system_state, battery_pack, 4);

    printState(system_state);
    printf("\nChecking cell balance...\n");

    balanceCells(battery_pack, 4);
    printf("\nSaving battery telemetry...\n");

    saveTelemetry(battery_pack,4);
    return 0;
}