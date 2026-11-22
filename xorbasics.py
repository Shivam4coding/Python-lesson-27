"""
1) Add the file and topic details.
   a) Mention the file name as `01-xor-identity-cancel.py`.
   b) Mention the topic as "XOR Identity and Equality, XOR Cancellation".
   c) Introduce the program as a way to understand how XOR behaves with 0, itself, and repeated numbers.

2) Demonstrate XOR with 0.
   a) Pause the program before showing the examples.
   b) Use `5 ^ 0` to show that XOR with 0 keeps the number unchanged.
   c) Use `9 ^ 0` to show the same rule with another number.

3) Demonstrate XOR with itself.
   a) Pause the program before showing the examples.
   b) Use `5 ^ 5` to show that a number XORed with itself becomes 0.
   c) Use `9 ^ 9` to show the same rule with another number.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 6 or 11.
   c) Convert the input into an integer.

5) Ask for a XOR cancellation prediction.
   a) Ask the user to guess the result of `3 ^ n ^ 3`.
   b) Store the user's guess.

6) Demonstrate XOR cancellation.
   a) Pause before running the final example.
   b) Show that 3 appears twice in the expression.
   c) Explain that repeated XOR values cancel out.
   d) Calculate and print `3 ^ n ^ 3`.

7) Display the final result.
   a) Print the XOR expression.
   b) Print the calculated answer.
   c) Show the user's original guess.
"""

input("XOR with 0: Press Enter to see how XOR behaves with 0...")
print(" 5 ^ 0 =", 5 ^ 0)
print(" 9 ^ 0 =", 9 ^ 0)

input("XOR with itself: Press Enter to see how XOR behaves with itself...")
print(" 5 ^ 5 =", 5 ^ 5)
print(" 9 ^ 9 =", 9 ^ 9)

n = int(input("Enter a number (e.g., 6 or 11): "))
guess = input("Guess the result of 3 ^ n ^ 3 (where n is your number): ")
input("XOR cancels - 3 appears twice so it dissapears: Press Enter ")
print(" 3 ^", n, "^ 3 =", 3 ^ n ^ 3, " your guess was:", guess)