# 10. Bus Passenger Occupancy Simulation

## Problem statement
Track passengers boarding and leaving a bus at successive stops and report occupancy and capacity violations.

## Objectives
Use loops, lists, tuples, arithmetic, and conditional statements to simulate changing passenger counts.

## Assumptions
The bus starts empty. Capacity is a positive integer. Boarding and alighting counts are non-negative. Passengers cannot alight if fewer passengers are on board than the requested count.

## Algorithm
1. Read bus capacity and number of stops. 2. Start passenger count at zero. 3. For each stop, read boarding and alighting counts. 4. Validate counts. 5. Apply alighting then boarding. 6. Check capacity. 7. Store and print stop-wise occupancy.

## Flowchart
```text
Start → Input capacity and stops → Set passengers=0 → Loop stops → Input board/alight → Validate → Update passengers → Capacity exceeded? → Record status → Final report → End
```

## Pseudocode
```text
INPUT capacity, stop_count\npassengers = 0; records = empty list\nFOR each stop:\n  INPUT boarding, alighting\n  IF values negative OR alighting > passengers: reject input\n  ELSE: passengers = passengers - alighting + boarding\n  IF passengers > capacity: status = OVER CAPACITY ELSE status = OK\n  append stop record\nPRINT records and final occupancy
```

## Python source code
See `bus_occupancy.py` in this folder. Run it with:

```bash
python bus_occupancy.py
```

## Test cases
Capacity=40. Stop 1: board 25, alight 0 → 25 (OK). Stop 2: board 20, alight 5 → 40 (OK). Stop 3: board 3, alight 0 → 43 (OVER CAPACITY).

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The simulation demonstrates sequential updates using loops and stores stop-wise results as tuples.
