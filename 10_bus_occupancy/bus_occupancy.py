def main():
    try:
        capacity = int(input("Bus capacity: "))
        stop_count = int(input("Number of stops: "))
        if capacity <= 0 or stop_count < 0:
            raise ValueError("Capacity must be positive and stop count non-negative.")

        passengers = 0
        records = []

        for stop in range(1, stop_count + 1):
            print(f"\\nStop {stop}")
            boarding = int(input("Passengers boarding: "))
            alighting = int(input("Passengers alighting: "))

            if boarding < 0 or alighting < 0:
                raise ValueError("Passenger counts cannot be negative.")
            if alighting > passengers:
                raise ValueError("Alighting count exceeds passengers currently on board.")

            passengers = passengers - alighting + boarding
            status = "OVER CAPACITY" if passengers > capacity else "OK"
            records.append((stop, boarding, alighting, passengers, status))

        print("\\n========== BUS OCCUPANCY REPORT ==========")
        for stop, boarding, alighting, occupancy, status in records:
            print(
                f"Stop {stop}: Boarded={boarding}, Alighted={alighting}, "
                f"On board={occupancy}, Status={status}"
            )
        print(f"Final passengers on board: {passengers}")
        print(f"Available seats (if within capacity): {max(0, capacity - passengers)}")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
