import math

def analyze_sample():
    # 1. Ask for sample name
    sample_name = input("Enter sample name: ")

    # 2. Ask for number of replicates
    n = int(input("Enter number of replicates: "))

    # 3. Ask for measured values
    values_input = input("Enter measured values separated by commas: ")
    values = [float(v.strip()) for v in values_input.split(",")]

    # Basic validation
    if len(values) != n:
        print("Warning: Number of values does not match number of replicates.")

    # 4. Calculate Average
    average = sum(values) / len(values)

    # Calculate Standard Deviation (sample standard deviation)
    variance = sum((x - average) ** 2 for x in values) / (len(values) - 1)
    stdev = math.sqrt(variance)

    # Calculate %CV
    cv = (stdev / average) * 100 if average != 0 else 0

    # 5. Print results
    print("\nSample name:", sample_name)
    print("Average:", average)
    print("STDEV:", stdev)
    print("%CV:", cv)

# Run the function
analyze_sample()