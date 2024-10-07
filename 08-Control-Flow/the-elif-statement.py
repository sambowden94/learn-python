def positive_or_negative(number):
    if number > 0:
        return "positive!"
    elif number < 0:
        return "negative!"
    elif number == 0:
        return "neither its zero"
    
print(positive_or_negative(5))
