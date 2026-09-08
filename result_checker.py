# Student Result Checker
# This program checks marks and sorts students into Pass and Fail lists

passing_marks = 40

students = [
    ("Aman", 85),
    ("Priya", 45),
    ("Rohit", 92),
    ("Sara", 38),
    ("Vikram", 67)
]

pass_list = []
fail_list = []

for name, marks in students:
    if marks >= passing_marks:
        pass_list.append(name)
    else:
        fail_list.append(name)

print("Pass List:")
for name in pass_list:
    print(name)

print("\nFail List:")
for name in fail_list:
    print(name)