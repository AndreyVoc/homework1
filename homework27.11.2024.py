calls =  0
def count_calls(n):
    global  calls
    calls += n
    return calls
def string_info(string):
    count_calls(1)
    return len(string), str.upper(string), str.lower(string)
def is_contains(string, list_to_search):
    count_calls(1)
    if string.casefold() in list_to_search:
        print(string,  list_to_search, 'True')
        return True
    else:
        print(string, list_to_search, 'False')
        return False
print(string_info('мельпопс'))
print(string_info('ням ням ням'))
print(string_info('жу жу жу'))
is_contains('жу жу жу',['жу жу жу','мельпопс','ням ням ням'])
is_contains('жу жу',['жу жу жу','мельпопс','ням ням ням'])
print( 'Счетчик: ', calls)