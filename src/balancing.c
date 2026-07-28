#include <stdio.h>
#include "balancing.h"


void balanceCells(BatteryCell cells[], int number_of_cells)
{

    float highest_voltage = cells[0].voltage;
    float lowest_voltage = cells[0].voltage;

    int highest_cell = 0;
    int lowest_cell = 0;


    // Find highest and lowest voltage cells

    for(int i = 1; i < number_of_cells; i++)
    {

        if(cells[i].voltage > highest_voltage)
        {
            highest_voltage = cells[i].voltage;
            highest_cell = i;
        }


        if(cells[i].voltage < lowest_voltage)
        {
            lowest_voltage = cells[i].voltage;
            lowest_cell = i;
        }

    }


    float difference = highest_voltage - lowest_voltage;


    printf("\n===== CELL BALANCING REPORT =====\n");


    printf("Highest Cell: %d (%.3f V)\n",
           highest_cell + 1,
           highest_voltage);


    printf("Lowest Cell: %d (%.3f V)\n",
           lowest_cell + 1,
           lowest_voltage);


    printf("Voltage Difference: %.3f V\n",
           difference);



    if(difference > 0.05)
    {

        printf("\nSTATUS: IMBALANCE DETECTED\n");

        printf("ACTION: Balancing activated\n");


        // Save status for dashboard

        FILE *file = fopen("data/status.txt", "w");


        if(file != NULL)
        {
            fprintf(file, "BALANCING ACTIVE");
            fclose(file);
        }


        // Simulate passive balancing
        cells[highest_cell].voltage -= 0.02;


        printf("Cell %d voltage reduced for balancing\n",
               highest_cell + 1);

    }


    else
    {

        printf("\nSTATUS: CELLS BALANCED\n");


        // Save status for dashboard

        FILE *file = fopen("data/status.txt", "w");


        if(file != NULL)
        {
            fprintf(file, "SYSTEM NORMAL");
            fclose(file);
        }

    }


}