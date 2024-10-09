def string_calculator(numbers):
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    else:
        delimiter = ","

    numbers = numbers.replace("\n", delimiter)
    nums = [int(num) for num in numbers.split(delimiter)]
    
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
    
    return sum(num for num in nums if num <= 1000)