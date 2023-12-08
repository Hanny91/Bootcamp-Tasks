#Prints a given single string with appropriate spaces, in capitals, and reversed.

single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog"

spaced = single_string.replace("!", " ")
print(spaced)

capitalized = spaced.upper()
print(capitalized)

reversed = spaced[::-1]
print(reversed)