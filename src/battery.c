#include "battery.h"


void initializeBattery(BatteryCell cells[], int number_of_cells)
{

    for(int i = 0; i < number_of_cells; i++)
    {

        cells[i].voltage = 3.75 + (i * 0.01);
        cells[i].temperature = 25.0 + (i * 0.5);
        cells[i].state_of_charge = 80.0;
        cells[i].health = 100.0;

    }

}


void chargeBattery(BatteryCell cells[], int number_of_cells)
{

    for(int i = 0; i < number_of_cells; i++)
    {

        if(cells[i].state_of_charge < 100)
        {
            cells[i].state_of_charge += 1;
            cells[i].voltage += 0.01;
            cells[i].temperature += 0.05;
        }

    }

}


void dischargeBattery(BatteryCell cells[], int number_of_cells)
{

    for(int i = 0; i < number_of_cells; i++)
    {

        if(cells[i].state_of_charge > 0)
        {
            cells[i].state_of_charge -= 1;
            cells[i].voltage -= 0.01;
            cells[i].temperature += 0.02;
        }

    }

}