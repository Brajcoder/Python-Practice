# Input Format

# The first line contains the integer n, the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.


# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    avg = sum(student_marks[query_name])/3
print("{:.2f}".format(avg))