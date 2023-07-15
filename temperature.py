def convert_cel_to_far(cel):
    far = cel * 9/5 + 32
    return far

def convert_far_to_cel(far):
    cel = (far - 32) * 5/9
    return cel

far = input("Enter a temperature in Fahrenheit: ")
# newfar = convert_far_to_cel(int(far))
print(f"{far} degrees F = {convert_far_to_cel(int(far)):.2f} degrees C")
print("")
cel = input("Enter a temperature in degrees C: ")
print(f"{cel} degrees F = {convert_cel_to_far(int(cel)):.2f} degrees F")
