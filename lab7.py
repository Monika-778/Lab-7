# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:53:19 2026

@author: Monika
"""

#Ques1.
'''a=input("Entre the string:") 
rev=""
for i in a:
    rev = i + rev
print(rev)'''

#Ques2.
'''x = input("enter your string: ")
count = 0
for i in x:
    count+=1
    if i == " ":
        count=0
print(count)'''
    
#Ques3.
'''x = input("enter your string: ")
w = input("enter your word: ")
count =0
for i in x:
    if i == w:
        count= count + 1
print("count: ",count)
if count==0:
    print(f"there is no '{w}' in the string")'''
    
#Ques4. 
'''x  = input("enter your string: ")
x = x.lower()
a = "qwertyuiopasdfghjklzxcvbnm"
count = 0
for i in a:
    if a in x:
        count+=1
if count==26:
    print(f"{x} is a pangram")
else:
    print(f"{x} is not a pangram")'''
    
#Ques5.            



            
#Ques6.
'''count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
total = 0

while True:
    n = int(input("Enter a number (1-10) or -1 to stop: "))

    if n == -1:
        break

    if n < 1 or n > 10:
        print("Invalid input! Enter a number from 1 to 10.")
        continue

    total = total + 1

    if n <= 2:
        count1 = count1 + 1
    elif n <= 4:
        count2 = count2 + 1
    elif n <= 6:
        count3 = count3 + 1
    elif n <= 8:
        count4 = count4 + 1
    else:
        count5 = count5 + 1

if total > 0:
    print("1 - 2:", "# " * count1, format(count1 * 100 / total, ".2f"), "%")
    print("3 - 4:", "# " * count2, format(count2 * 100 / total, ".2f"), "%")
    print("5 - 6:", "# " * count3, format(count3 * 100 / total, ".2f"), "%")
    print("7 - 8:", "# " * count4, format(count4 * 100 / total, ".2f"), "%")
    print("9 - 10:", "# " * count5, format(count5 * 100 / total, ".2f"), "%")
else:
    print("No numbers were entered.")
   '''
    
#Ques7.
'''x = input("enter your string: ")
if x==x[::-1]:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")'''
    
#Ques8. 
'''x = list(map(int,input("enter your numbers with 1 space:").split(",")))
add = 0
pro=1
sd=9999999
l = 0
for i in x:
    add = add+i
    pro = pro*i
    if sd>i:
        sd=i        
print(f"\naddition of all numbers in this list: {add}\n")
print(f"product of all numbers in this list: {pro}\n")
print(f"the smallest number in this list: {sd}")'''

#Ques9.
'''numbers = input("Enter integers separated by spaces: ").split()
i = 0
while i < len(numbers):
    numbers[i] = int(numbers[i])
    i = i + 1
i = 0
while i < len(numbers) - 1:
    j = 0

    while j < len(numbers) - 1 - i:
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        j = j + 1
    i = i + 1

print("Descending order:", numbers)'''

#Ques10.
'''s = input("Enter hyphen-separated words: ")
words = s.split("-")
i = 0
while i < len(words) - 1:
    j = 0
    while j < len(words) - 1 - i:
        if words[j] > words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp
        j = j + 1
    i = i + 1
result = ""
i = 0
while i < len(words):
    if i > 0:
        result = result + "-"
    result = result + words[i]
    i = i + 1

print(result)
'''

#Ques11.
'''text = input("Enter a paragraph: ")
digits = 0
alphabets = 0
uppercase = 0
lowercase = 0
special = 0
for ch in text:
    if ch.isdigit():
        digits = digits + 1
    elif ch.isalpha():
        alphabets = alphabets + 1

        if ch.isupper():
            uppercase = uppercase + 1
        elif ch.islower():
            lowercase = lowercase + 1
    else:
        special = special + 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Uppercase alphabets:", uppercase)
print("Lowercase alphabets:", lowercase)
print("Special characters:", special)'''


            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            