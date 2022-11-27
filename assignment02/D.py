student = ("12210001", "12210002", "12210003", "12210004")
score = ("90", "99", "85", "97")
gpa = ('4.0', '4.0', '3.5', '4.0')
level = ("A+", "A+", "A", "A+")

rev = {}
for i in range(0, 4):
    rev[student[i]] = i

idx = rev[input()]
s = score[idx]

res = (student[idx], score[idx], gpa[idx], level[idx])
print(res)
# FILE MODIFY