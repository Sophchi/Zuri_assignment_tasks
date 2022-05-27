# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(phrase1, phrase2):
    # [assignment] Add your code here
    print('Checking the anagrammatic relation between {} and {}........\n'.format(phrase1, phrase2))
    
    str_list1 = list(phrase1.lower())
    str_list1.sort()
    if " " in str_list1:
        str_list1.remove(' ')
    str_list2 = list(phrase2.lower())
    str_list2.sort()
    if " " in str_list2:
        str_list2.remove(' ')

    print('Comparing....{} and {}.......\n'.format(str_list1, str_list2))

    if  len(str_list1) == len(str_list2) and (str_list1 == str_list2):
        return True
    else:
        return False


phrase1 = input('Enter a phrase: ')
phrase2 = input('Enter another phrase: ')

print(find_anagrams(phrase1, phrase2))