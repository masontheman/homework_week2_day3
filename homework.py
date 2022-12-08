def num_negative(nums):
    print([num*-1 for num in nums])
def numbers_only_from_string(string_you_want_redacted):
   print([numbers for numbers in string_you_want_redacted if numbers.isdigit()]) 
def string_to_int_plus_one_backto_string(string_you_want_changed):
    print(str((int(string_you_want_changed)+1)))
