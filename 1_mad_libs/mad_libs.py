def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f""""Once upon a type there was a {noun1} who lived in a village.
The {noun1} loved to {verb1}.
But the {noun1} had a {noun2} and {verb2} to keep the {noun1} happy.
So the {noun1} {verb2} to the {noun2} and keep the {noun1} happy.
The end"""

print(story)
