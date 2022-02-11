# put your code here
STOPX = 55
looped = 0
input_sum = 0
x = int(input())
while x != STOPX:
    input_sum += x
    looped += 1
    x = int(input())
print(looped)
print(input_sum)
print(round(input_sum / looped))
