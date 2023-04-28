import math
def is_square(n):    
    if n>= 0:
        print(str(math.sqrt(n)))
        print(str(math.sqrt(n))[-2::])
    if n>= 0 and str(math.sqrt(n))[-2::] == '.0':
        return True
    else : return False

import math
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0


def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = sorted(numbers, key=int)
    return numbers [-1] + ' ' + numbers[0]
    

def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))



def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return[]
    positive_count = sum([1 for i in arr if i > 0])
    negative_sum = sum([i for i in arr if i <0])
    return [positive_count, negative_sum]


def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg] 


