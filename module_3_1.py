calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [name.lower() for name in list_to_search]
    if string.lower() in list_to_search:
        print(True)
    else:
        print(False)



print(string_info('Capybara'))
print(string_info('Armageddon'))
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
