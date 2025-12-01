def main():
    display_main_menu()        
    nums = get_user_input()     
    calc_average(nums)
    find_min_max(nums)

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    arraylist = []
    print("get_user_input")
    inputstr = input()
    numlist = inputstr.split(",")
    
    for eachnum in numlist:
        arraylist.append(float(eachnum.strip()))

    print(arraylist)

    return arraylist

def calc_average(nums):
    print("calc_average")
    total = sum(nums)
    count = len(nums)
    average = total/count

    print("Average: " , average)
    return average

def find_min_max(nums):
    print("find_min_max")
    min_temp = min(nums)
    max_temp = max(nums)
    print("Min:", min_temp, "Max:", max_temp)
    return [min_temp, max_temp]

def sort_temperature(values):
    print("sort_temperature")

def calc_median_temperature(values):
    print("calc_median_temperature")

if __name__ == "__main__":
    main()