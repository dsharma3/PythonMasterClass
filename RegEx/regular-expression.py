import re
'''
#part 1
patterns = ["item1","item2"]

phrase = "This is a string with item2 and doesnt have the other item1!"

for pattern in patterns:
    print("iam searching for pattern",pattern)

    if re.search(pattern, phrase):
        print('match')
    else:
        print('No Match')
'''
'''
#part 2
phrase = "this is item1!"
match = re.search('item1', phrase)
print(type(match))
print(len(phrase))
print(match.start())
print(match.end())
'''
# email = 'user@gmail.com'
# print(re.split('@', email))

#email = 'user@gmail.com'
# print(re.split('@', email))
'''
part 3
def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print("searchin for pattern ", pattern)
        print(re.findall(pattern, phrase))

phrase = 'sdsd..sssddd..sdddsddd...dss'
patterns = ['s[sd]+']

multi_re_find(patterns, phrase)
'''
#exclusion

email= 'abc#@gmail.com'
username='dsharma3'
phrase='This is my PHRASE with whitespace'
alphanumeric_phrase='This is my phrase with alphanumeric123 and its fun!'

pattern_for_capital_letters =['[A-Z]+']
pattern_for_small_letters =['[A-Z]+']
pattern_for_digit_letters =[r'\d+']
pattern_for_nondigit_letters =[r'\D+']
pattern_for_space_letters =[r'\s+']
pattern_for_nonspace_letters =[r'\S+']
pattern_for_alphanumeric_letters =[r'\W+']




def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print("searchin for pattern ", pattern)
        print(re.findall(pattern, phrase))

multi_re_find(pattern_for_capital_letters, phrase)








