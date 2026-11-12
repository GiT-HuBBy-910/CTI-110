import time

# Learning to use FOR loops

# for loop needs the range function     range(start, end)

for num in range(10):
    print(num)
    time.sleep(1)


for num in range(2,11,2):
    print(num)
    time.sleep(1)


# Loop through a list

classes = ['Math', 'Science', 'Reading', 'P.E.']

for subject in classes:
    print(subject + "!")