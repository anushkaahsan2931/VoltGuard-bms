#include <stdio.h>
#include "faults.h"


void checkFaults(BatteryCell cells[], int number_of_cells)
{

    FILE *file = fopen("data/fault_log.txt", "w");


    if(file == NULL)
    {
        printf("Unable to create fault log\n");
        return;
    }


    int fault_detected = 0;


    fprintf(file, "===== FAULT MONITORING REPORT =====\n\n");


    printf("\n===== FAULT MONITORING REPORT =====\n");


    for(int i = 0; i < number_of_cells; i++)
    {

        if(cells[i].temperature >= 60)
        {
            printf("[FAULT] Cell %d: Over Temperature\n", i + 1);

            fprintf(file,
            "[FAULT] Cell %d: Over Temperature (%.2f C)\n",
            i + 1,
            cells[i].temperature);

            fault_detected = 1;
        }


        else
        {
            fprintf(file,
            "[OK] Cell %d Temperature Normal\n",
            i + 1);
        }



        if(cells[i].voltage >= 4.2)
        {
            printf("[FAULT] Cell %d: Over Voltage\n", i + 1);

            fprintf(file,
            "[FAULT] Cell %d: Over Voltage (%.2f V)\n",
            i + 1,
            cells[i].voltage);

            fault_detected = 1;
        }


        else if(cells[i].voltage <= 3.0)
        {
            printf("[FAULT] Cell %d: Under Voltage\n", i + 1);

            fprintf(file,
            "[FAULT] Cell %d: Under Voltage (%.2f V)\n",
            i + 1,
            cells[i].voltage);

            fault_detected = 1;
        }


        else
        {
            fprintf(file,
            "[OK] Cell %d Voltage Normal\n",
            i + 1);
        }

    }


    if(fault_detected == 0)
    {
        fprintf(file,
        "\nSYSTEM STATUS: NO CRITICAL FAULTS\n");

        printf("\nSYSTEM STATUS: NO CRITICAL FAULTS\n");
    }


    else
    {
        fprintf(file,
        "\nSYSTEM STATUS: FAULTS DETECTED\n");

        printf("\nSYSTEM STATUS: FAULTS DETECTED\n");
    }


    fclose(file);

}