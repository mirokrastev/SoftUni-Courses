def exchange(ind, lst):
    if ind > len(lst) - 1 or ind < 0:
        print('Invalid index')
        return lst
    else:
        new = lst[ind + 1:] + lst[:ind + 1]
        return new
 
 
def get_odds(lst):
    return [x for x in lst if x % 2 != 0]
 
 
def get_even(lst):
    return [x for x in lst if x % 2 == 0]
 
 
def get_index_of_number(lst, number):
    return [ind for ind, num in enumerate(lst) if num == number]
 
 
def duplicate_val(lst,number):
    seen = set()
    res = []
    for ind, num in enumerate(lst):
        if num == number and num not in seen:
            seen.add(num)
        else:
            if num == number:
                res.append(ind)
    return max(res)
 
 
def get_element(lst, max_min, check, all_numbers=None):
    if all_numbers is None:
        all_numbers = []
    checks = {'even': get_even(lst), 'odd': get_odds(lst),
              'max': lambda x: max(x) if x else 'No matches',
              'min': lambda x: min(x) if x else 'No matches'}
    function = checks.get(check)
    all_numbers = function
    number = checks[max_min](all_numbers)
    if isinstance(number, int):
        return max(get_index_of_number(lst, number))
    else:
        return number
 
 
def first(lst_check, count, lst):
    if count > len(lst):
        return 'Invalid count'
    if not lst_check:
        return lst_check
    return lst_check[:count]
 
 
def last(lst_check, count, lst):
    if count > len(lst):
        return 'Invalid count'
    if not lst_check:
        return lst_check
    return lst_check[-count:]
 
 
def first_last(lst, check, even_odd, count, lst_check=None):
    funcs_for_lists = {'odd': lambda x: get_odds(x), 'even': lambda x: get_even(x)}
    lst_check = funcs_for_lists[even_odd](lst)
    checks = {'first': first(lst_check, count, lst), 'last': last(lst_check, count, lst)}
    result = checks[check]
    return result
 
 
numbers = [int(x) for x in input().split()]
commands = input()
 
while commands != 'end':
    lst_commands = commands.split()
    if lst_commands[0] == 'exchange':
        index = int(lst_commands[1])
        numbers = exchange(index, numbers)
    elif lst_commands[0] == 'max' or lst_commands[0] == 'min':
        maxi_mini = lst_commands[0]
        odd_even = lst_commands[1]
        print(get_element(numbers, maxi_mini, odd_even))
    elif lst_commands[0] == 'first' or lst_commands[0] == 'last':
        chk = lst_commands[0]
        counter = int(lst_commands[1])
        odd_even = lst_commands[2]
        print(first_last(numbers, chk, odd_even, counter))
    commands = input()
 
print(numbers)