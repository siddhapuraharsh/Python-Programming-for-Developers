course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0:1]))


# Escape Sequences
# \"
# \'
# \\
# \n
message = "Python \"Programming"
print(message)


# Formatting Strings
first = "Harsh"
last = "Siddhapura"
fullName = f"{first} {last}"
print(fullName)

# String Methods
course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("Pro"))
print(course.replace('P', "-"))
print("Pro" in course)