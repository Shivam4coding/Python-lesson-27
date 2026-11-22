"""
1) Add the file and topic details.
   a) Mention the file name as `03-two-odd-split.py`.
   b) Mention the topic as "XOR of Two Odd-Occurring Numbers, Splitting by the Rightmost Set Bit".
   c) Introduce the program as a way to split numbers into groups using a bit check.

2) Explain the XOR idea.
   a) Show that XOR cancels matching pairs.
   b) Explain that two odd-occurring numbers remain after pairs cancel.
   c) Pause the program before showing the example.

3) Show a fixed XOR example.
   a) Use the list `[1, 4, 3, 3]`.
   b) XOR all numbers together.
   c) Print the XOR result.
   d) Print the binary form of the XOR result.

4) Explain the split bit.
   a) Use bit 0 as the split bit.
   b) Place numbers with bit 0 ON into group A.
   c) Place numbers with bit 0 OFF into group B.

5) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 6 or 9.
   c) Convert the input into an integer.

6) Ask for a prediction.
   a) Ask whether bit 0 of the number is ON.
   b) Store the user's guess.

7) Check bit 0.
   a) Pause before running the check.
   b) Use `n & 1` to check the last bit.
   c) If the result is true, bit 0 is ON.
   d) Otherwise, bit 0 is OFF.

8) Display the group result.
   a) Print the number.
   b) Print its binary form using `bin(n)[2:]`.
   c) Show whether it belongs to group A or group B.
   d) Show the user's original guess.
"""

input("XOR all - pairs cancel, two odd-occurring numbers remain: Press Enter to see how XOR can find the two odd-occurring numbers...")
print(" list = [1, 4, 3, 3]")
print(" split bit 1 -> group A (bit 0 ON): group B (bit 0 OFF): 4")

n = int(input("Enter a number (e.g., 6 or 9): "))
guess = input("Is bit 0 of " + str(n) + " ON? (yes/no): ")
input ("Check the split bit. Press Enter ")
if n & 1:
    print(" ", n, " binary:", bin(n) [2:], " bit 0 ON - group A your guess:", guess)
else:
    print (" ", n, " binary:", bin(n)[2:], " bit 0 OFF - group B your guess:", guess)
