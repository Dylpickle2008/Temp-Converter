print("Welcome to Temperature Converter, a lightweight utility for converting temperature")

#create variables for the units that are being converted to the temperature
unit = input("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature value you want converted: "))


#Converts C to F
def c_to_f(temp_c):
    converted_c = temp_c * (9/5) + 32
    return converted_c 

#Converts F to C
def f_to_c(temp_f):
    converted_f = (temp_f - 32) * (5/9)
    return converted_f 

def main():
    if(unit == "C"):
        celcius_to_farenheit = c_to_f(value) 
        return celcius_to_farenheit 
    elif(unit == "F"):
        farenheit_to_celcius = f_to_c(value)
        return farenheit_to_celcius
    else:
        warning="Please enter C or F to specify unit"
        return warning
    
#Print Results
result= main()
print("Your value is: " + str(result))
