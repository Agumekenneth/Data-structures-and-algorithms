# functions
'''def calc_area(l,w):
    Area_of_the_rectangle =l * w
    return Area_of_the_rectangle

length = float(input("Enter the length"))
width = float(input("Enter the width"))
the_Area_of_the_rectangle = calc_area(length,width)
print(f"The area of the rectangke is: {the_Area_of_the_rectangle}")'''

'''def calc_average(num1,num2,num3):
    sum = num1 + num2 + num3
    average = sum/3
    return average

print(f"This program will calculate the average of 3 numbers")
average = calc_average(10,11,12)
print(f"The average of the numbers is: {average}")

list_num =[1,2,3,4,5,6]
num_elements = len(list_num)
sum_elements = 0
for i in list_num:
    sum_elements = sum_elements + i
    average_elements = sum_elements/num_elements

print(sum_elements)   
print(average_elements)

def my_list(numbers):
   max_number = max(numbers)
   print(f"The maximum number is: {max_number}")
   min_number =min(numbers)
   print(f"the minimum number is: {min_number}")
   return max_number,min_number
numbers= [2,5,6,8,10]
my_list(numbers)

def sample_list(numbers):
   numbers = sum(numbers)
   print(f"The expected output is: {numbers}")
   return numbers
my_numbers= [8,2,3,0,7]
sample_list(my_numbers)

from functools import reduce
from operator import mul
from numpy import average

def sample_list(multiple):
   multiple =reduce(mul,multiple)
   print(f"The expected output is: {multiple}")
   return multiple
my_multiples = [8,2,3,-1,7]
sample_list(my_multiples)

def reverse_string(reverse):
   my_reverse = reverse[::-1]
   print(f"my reversed string is: {my_reverse}")
   return my_reverse
reverse ='1234abcd'
reverse_string(reverse)

def number_range(number):
      if number in range(1,21):
         return number
      else:
         return None
number = int(input("Enter any number"))
result = number_range(number)
if result is not None:
   print(f"the number: {result} is within the range")
else:
   print(f"the number is not within the range ")

def area_of_a_circle(area):
 area = radius *Pi
 print(f"The area of the circle is: {area}")
 return area
Pi = 3.142
radius = float(input('Enter your radius'))
area = radius* Pi
area_of_a_circle(area)

def perimetr_of_a_rectangle(perimeter):
 perimeter = 2*(length + width)
 print(f"The perimeter of the rectangle is: {perimeter}")
 return perimeter
length = int(input("Enter the length of the rectangle"))
width = int(input("Enter the width of the rectangle"))
perimeter = 2*( length+width)
perimetr_of_a_rectangle(perimeter)

def store_marks(assignment):
 
 average = sum(assignment)/len(assignment)
 assignment.append(50)
 print(f"The average of the scores is: {average}")
 if average < 35:
  print(f"The student is not qualified")
 else:
  print("The student is qualified")
 return average
  
assignment = [80,70,70,90]
store_marks(assignment)

for i in range(1,8):
      for j in range(1,8):
         product = i * j
         print(f"{i}*{j} = {product} ")
         
def yaka(price):
 units = price//560
 print(f"The number of units earned is: {units}")   
 return units
price = int(input("Enter the amount you want to pay"))
yaka(price)

def amount_paid(unit_cost):
 cost = unit_cost * units
 print(f"The ampont to be paid is: shs{cost}")
 return cost
units= int(input("Enter your units"))
unit_cost = 4100
amount_paid(unit_cost)

num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
add = num1+num2
def answer(add):
    sum = num1+num2
    print(f"The answer is: {sum}")
    return sum
answer(add)
    
string = 'programming'

def string_slicing(string):
    str = string[1:8:2]
    print(f"The sliced string is: {str}")
    return str
string_slicing(string)'''


fruits =["banana","apple","mango"]

fruits.append('pineapple')
print(f"The fruits are: {fruits}")

numbers = [76,95,78,90,100,67]
numbers.pop()
print(f"The new numbers are: {numbers}")
