#include <stdio.h>
#include "controller.h"


void monitorBattery(BatteryCell cells[], int number_of_cells)
{

    for(int i = 0; i < number_of_cells; i++)
    {

        if(cells[i].temperature > 60)
        {
            printf("WARNING: Cell %d overheating!\n", i + 1);
        }


        if(cells[i].voltage > 4.2)
        {
            printf("WARNING: Cell %d over-voltage!\n", i + 1);
        }


        if(cells[i].voltage < 3.0)
        {
            printf("WARNING: Cell %d under-voltage!\n", i + 1);
        }

    }

}



void updateState(BatteryState *state, BatteryCell cells[], int number_of_cells)
{

    for(int i = 0; i < number_of_cells; i++)
    {

        if(cells[i].temperature >= 60)
        {
            *state = FAULT;
            return;
        }

    }


    if(*state == IDLE)
    {
        *state = CHARGING;
    }

}



void printState(BatteryState state)
{

    switch(state)
    {

        case IDLE:
            printf("System State: IDLE\n");
            break;


        case CHARGING:
            printf("System State: CHARGING\n");
            break;


        case DISCHARGING:
            printf("System State: DISCHARGING\n");
            break;


        case FAULT:
            printf("System State: FAULT\n");
            break;

    }

}