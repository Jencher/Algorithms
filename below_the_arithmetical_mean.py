# The arithmetical mean is the sum of elements divided by the number of elements
# Example: [1, 3, 5, 6, 4, 10, 2, 3] the arithmetical mean = (1+3+5+6+4+10+2+3=34) / 8= 4,25
# Answer: [1, 3, 4, 2, 3] all numbers in list below 4,25

def below_arithmetical_mean(arr):
    arithm_mean = float(sum(arr) / len(arr))

    result = []
    for char in arr:
        if char < arithm_mean:
            result.append(char)
    return result


arr1 = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_arithmetical_mean(arr1))
