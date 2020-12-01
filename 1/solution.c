#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 256
#define MAX_NBR_VALUES 1024

void findTwo(int *values, int numberOfValues)
{
    for(int x=0; x < numberOfValues; x++)
    {
        for(int y=0; y < numberOfValues; y++)
        {
            if (values[x] + values[y] == 2020)
            {
                printf("Solution 1: %d (%d, %d)\n",
                    values[x] * values[y], values[x], values[y]);
                return;
            }
        }
    }
}

void findThree(int *values, int numberOfValues)
{
    for(int x=0; x < numberOfValues; x++)
    {
        for(int y=0; y < numberOfValues; y++)
        {
            for(int z=0; z < numberOfValues; z++)
            {
                if (values[x] + values[y] + values[z] == 2020)
                {
                    printf("Solution 1: %d (%d, %d, %d)\n",
                        values[x] * values[y] * values[z], values[x], values[y], values[z]);
                    return;
                }
            }
        }
    }
}

int main(void)
{
    char  fileName[] = "input.txt";
    char  line[MAX_LINE_LENGTH];
    int   values[MAX_NBR_VALUES];
    int   numberOfValues = 0;

    FILE* file = fopen(fileName, "r");
    while (fgets(line, sizeof(line), file)) {
        values[numberOfValues++] = atoi(line);
    }
    fclose(file);

    findTwo(values, numberOfValues);
    findThree(values, numberOfValues);

    return 0;
}
