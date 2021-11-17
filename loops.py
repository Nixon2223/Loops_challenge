# counter = 0
# my_number = 5

# while (counter < my_number):
#     print(f"counter is {counter}")
#     counter += 1

# Challenge (loops): using loops calculate the factorial of a given number n (by the user). The notation is n! (read “n factorial”). For example, five factorial would be, 5! = 5 * 4 * 3 * 2 * 1 = 120. Your programme should ask the user for a value and later say (if the value is 5), “5! = 120". Challenge plus: print the answer in the format shown (For example 4! = 4 * 3 * 2 * 1 = 24).

user_input = int(input("Input number: "))
n = user_input

# factorial = 1
# while n != 0:
#     factorial *= n
#     n -= 1

# print(f"{user_input}! = {factorial}")

l = [i for i in range(n+1)]
l.remove(0)
l.reverse()

factorial = 1
output_str = ""
for number in l:
    factorial *= number
    if number > 1:
        output_str += f"{number} * "
    else:
        output_str += "1"
        
print(f"{user_input}! = {output_str} = {factorial}" )