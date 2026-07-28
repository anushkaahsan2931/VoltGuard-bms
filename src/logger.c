#include <stdio.h>
#include "logger.h"


void logEvent(char message[])
{

    printf("[LOG] %s\n", message);

}


void saveTelemetry(BatteryCell cells[], int number_of_cells)
{

    FILE *file;

    file = fopen("data/telemetry.csv", "w");


    if(file == NULL)
    {
        printf("Error opening telemetry file\n");
        return;
    }


    fprintf(file, "Cell,Voltage,Temperature,SOC\n");


    for(int i = 0; i < number_of_cells; i++)
    {

        fprintf(
            file,
            "%d,%.2f,%.2f,%.2f\n",
            i + 1,
            cells[i].voltage,
            cells[i].temperature,
            cells[i].state_of_charge
        );

    }


    fclose(file);

}