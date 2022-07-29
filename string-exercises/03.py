s1 = "America"
s2 = "Japan"

#printing the first characters from the string
first_char = s1[0] + s2[0]

##printing the middle chars from the string
l = len(s1)
mi = int(l/2)
l2 = len(s2)
mi2= int(l2/2)
second_char = s1[mi] + s2[mi2]

#printing the last chars from the two string
last_char = s1[-1] + s2[-1]

##adding all the characters for the final string
final_chars = first_char + second_char + last_char
print(final_chars)