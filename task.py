

def checkout_time_for_customers(customers,cashregisters:int):
    if cashregisters == 1:
        return sum(customers)
    elif len(customers) <= cashregisters:
        return max(customers)

    registers = {}
    for i in range(cashregisters):
        registers[i] = customers.pop(0)

    total_time_taken = 0
    while any(registers.values()):
        for r in registers.copy():
            registers[r] -= 1
            if registers[r] <= 0:
                try:
                    registers[r] = customers.pop(0)
                except IndexError:
                    registers[r] = 0

        total_time_taken += 1
    return total_time_taken

print( checkout_time_for_customers([5, 1, 3], 1))



def check_string(string_list):
    str1 , str2 = string_list
    set_str1 = set()
    for i in str1:
        set_str1.add(i.lower())

    for i in str2:
        if i.lower() not in set_str1:
            return False
    return True


print(check_string(["hello", "Hello"]))
print(check_string(["hello", "hey"]))
print(check_string(["Alien", "line"]))

