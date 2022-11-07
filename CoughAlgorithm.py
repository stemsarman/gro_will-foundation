print("*****ALGORITHM FOR COUGH HISTORY*****")

result = {"Name": input("What's your name? ")}

# Accept age.
try:
    age = int(input("What's your age? (in years): "))
except ValueError:
    print("Please enter your age in numbers!")
    age = int(input("What's your age? "))
else:
    result["Age"] = age

result["Religion"] = input("What's your religion? ")
result["Occupation"] = input("What's your occupation? ")
result["Residency"] = input("What's your residency? ")

# Accept sex.
print("What's your sex? (1/2/3)")
print("1: Male")
print("2: Female")
print("3: Others")
try:
    sex = int(input())
except ValueError:
    print("Please reply with 1, 2 or 3 (which is correct)")
    sex = int(input("What's your sex? (1/2/3)"))
else:
    result["Sex"] = sex

print("What are your present symptoms->")

# Accept is_cough.
print("Q1: Cough? (1/2)")
print("1: Yes")
print("2: No")
try:
    is_cough = int(input())
except ValueError:
    print("Please reply 1 for Yes and 2 for No...")
    is_cough = int(input("Q1: Cough? (1/2)"))
else:
    if is_cough == 1:
        result["Cough"] = "Yes"
    else:
        result["Cough"] = "No"

print("Anything else along with Cough->")

# Accept Duration of cough.
print("Q2: Duration of cough? (1/2/3)")
print("1: Acute < 3 weeks")
print("2: Subacute 3 to 8 weeks")
print("3: Chronic > 8 weeks")
try:
    duration_of_cough = int(input())
except ValueError:
    print("Please reply with option 1, 2 or 3 which applicable.")
    duration_of_cough = int(input("Duration of cough? "))
else:
    if duration_of_cough == 1:
        result["Duration of Cough"] = "Acute < 3 Weeks"
    elif duration_of_cough == 2:
        result["Duration of Cough"] = "Subacute 2 to 8 Weeks"
    else:
        result["Duration of Cough"] = "Chronic > 8 Weeks"

# Continue from here!!

try:
    pass
except ValueError:
    pass
else:
    pass

# Accept is_this_developed.
print("Q3 Is this developed: (1/2)")
print("1: Suddenly")
print("2: Gradually, with time")
try:
    is_this_developed = int(input())
except ValueError:
    is_this_developed = int(input("Reply with option 1 or 2: "))
else:
    if is_this_developed == 1:
        result["Developed"] = "Suddenly"
    else:
        result["Developed"] = "Gradually, with time."


# Accept is the cough.
print("Q1 Is the cough: (1/2)")
print("1: Persistent")
print("2: Occasional")
try:
    is_the_cough = int(input())
except ValueError:
    is_the_cough = int(input("Reply with option 1 or 2"))
else:
    if is_the_cough == 1:
        result["Cough is"] = "Persistent"
    else:
        result["Cough is"] = "Occasional"

# Get keys list and values.
list_of_keys = list(result.keys())
list_of_values = list(result.values())

# Create final string.
result_str = "YOUR COUGH REPORT IS READY...\n"
for key in list_of_keys:
    index = list_of_keys.index(key)
    result_str = result_str + "\n" + key + " : " + str(list_of_values.__getitem__(index))

# Write the final string to result file.
with open("result.txt", "w") as file:
    file.write(result_str)
    file.close()

print("Your Cough report is generated and saved as 'result.txt'")
