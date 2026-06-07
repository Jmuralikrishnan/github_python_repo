text = input("Enter a string : ")

vowels="AEIOUaeiou"

vowel_count=sum(1 for char in text if char in vowels)
print(f"Number of vowels: {vowel_count}")