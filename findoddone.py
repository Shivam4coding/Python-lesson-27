"""
1) Add the file and topic details.
   a) Mention the file name as `02-odd-occurring.py`.
   b) Mention the topic as "One Odd-Occurring Number".
   c) Introduce the program as a way to find the number that appears once.

2) Explain the XOR idea.
   a) Show that XOR can cancel pairs.
   b) Explain that numbers appearing twice cancel out.
   c) Explain that the odd-occurring number stays.

3) Show a fixed example.
   a) Pause the program before showing the example.
   b) Print the list `[2, 3, 4, 3, 2]`.
   c) Use XOR on all values in the list.
   d) Print the odd-occurring number.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 7 or 11.
   c) Convert the input into an integer.

5) Create a custom list.
   a) Create a list named `nums`.
   b) Add paired numbers like 3 and 5.
   c) Add the user's number once so it becomes the odd-occurring number.

6) Ask for a prediction.
   a) Show the custom list to the user.
   b) Ask which number appears once.
   c) Store the user's guess.

7) Find the odd-occurring number.
   a) Start `result` from 0.
   b) Use a for loop to go through every number in `nums`.
   c) Use `result ^= x` to XOR each number into the result.
   d) Let paired numbers cancel out.

8) Display the final result.
   a) Pause before showing the answer.
   b) Print the custom list.
   c) Print the odd-occurring number.
   d) Show the user's original guess.
"""

input("XOR cancels pairs: Press Enter to see how XOR can find the odd-occurring number...")
print(" list = [2, 3, 4, 3, 2]")
print(" odd-occurring number =", 2^3^4^3^2)

n = int(input("Enter a number (e.g., 7 or 11): "))
nums = [3, 5, 3, 5, n]
guess = input("Which number in " + str(nums) + " appears once? ")
result = 0
for x in nums:
      result ^= x
input("XOR cancels pairs - the odd one survives: Press Enter ")
print( " list =", nums, " odd-occurring number =", result, " your guess was:", guess)