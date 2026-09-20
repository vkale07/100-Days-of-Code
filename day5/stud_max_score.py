student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 85, 90, 78, 92, 88 ]

# total_stu_score = sum(student_scores)
# print(f"Total student score (using sum function): {total_stu_score}")


# total = 0
# for score in student_scores:
#     total += score
# print(f"Total student score (using for loop): {total}")

num = 0
for score in student_scores:
    if score > num:
        num = score
print(f"Highest student score (using for loop): {num}")




# sum of first 100 natural numbers using Range()
tot = 0
for i in range(1, 101):
    tot += i
print(f"Total sum (using for loop): {tot}")