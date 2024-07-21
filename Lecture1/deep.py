user_question = input("What is the answer to the Great Question of Life, the Universe and Everything?")

# Apply space and case insensitivity
user_question = user_question.strip().lower()

# Conditional Logic 
if user_question == "42" or user_question == "forty two" or user_question == "forty-two":
    print("Yes")
else: 
    print("No")