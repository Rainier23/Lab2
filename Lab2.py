def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    temperature = input("Input temperatures: ")
    Temp_list = temperature.split()
    for i in range(len(Temp_list)):
        Temp_list[i] = float(Temp_list[i])
    return Temp_list

def calc_average_temperature(temperature):
    average = sum(temperature) / len(temperature)
    print("Average temperture:" , average)

def calc_min_max_temperature(temperature):
    minimum = min(temperature)
    maximum = max(temperature)
    print("Minimum temperature:" , minimum)
    print("maximum temperature:" , maximum)



def calc_median_temperature(temperature):
    import statistics
    median = statistics.median(temperature)
    print("Median: " , median)



def main():
    inputs = get_user_input()
    calc_average_temperature(inputs)
    calc_min_max_temperature(inputs)
    calc_median_temperature(inputs)


if __name__ == "__main__":
    main()