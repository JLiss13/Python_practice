# Create a function that reverses a string
# Input 'Hi my name is Jordan'
# Output 'nadroJ si eman ym iH'

# Space complexity O(n)
# Time complexity O(n)
def reverseString(input_str):

    # Let's add error checks
    if not isinstance(input_str, str) or len(input_str) < 1:
        return print("input was not string")
    
    temp_str = list(input_str)
    reverse_str=''
    for i in range(1,len(temp_str)+1,1):
        reverse_str=reverse_str + temp_str[-i]
    
    return print(reverse_str)
    

example_str = "Hi my name is Jordan"
print(" case  1 ")
reverseString(example_str)

example_str = 102
print(" case  2 ")
reverseString(example_str)

example_str = ""
print(" case  3 ")
reverseString(example_str)