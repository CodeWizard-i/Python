import statistics
import time

def get_numbers_from_user():
    print("Statistic Calculator")
    time.sleep(1)
    print()
    print("Please enter numbers separated by commas (e.g., 1, 2, 3, 4, 5):")
    a = input("Enter numbers = ")
    try:
        numbers = [float(num.strip()) for num in a.split(',')]
        return numbers
    except ValueError:
        print("Invalid Input. Please enter numeric values separated by commas.")
        return None

def calculate_statistics(numbers):
    stats = {}
    stats['mean'] = statistics.mean(numbers)
    stats['median'] = statistics.median(numbers)
    try:
        stats['mode'] = statistics.mode(numbers)
    except statistics.StatisticsError:
        stats['mode'] = "No unique mode"

    stats['simple standard deviation'] = statistics.stdev(numbers)
    stats['variance'] = statistics.variance(numbers)
    stats['geometric mean'] = statistics.geometric_mean(numbers)
    stats['range'] = max(numbers) - min(numbers)
    stats['largest'] = max(numbers)
    stats['smallest'] = min(numbers)
    return stats

def main():
    numbers = None
    while numbers is None:
        numbers = get_numbers_from_user()
    
    stats = calculate_statistics(numbers)
    print("\nCalculated Statistics:")
    for stat, value in stats.items():
        print(f"{stat.capitalize()}: {value}")

if __name__ == "__main__":
    main()