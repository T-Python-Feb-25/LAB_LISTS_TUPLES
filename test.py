myList = ["one", "oi", 1100]
print(myList[1:2])

numbers = [30, 55, 3, 10, 2, 54]
average = sum(numbers)/len(numbers)
print("Average of list: " , average)
print("Average of list: ", round(average,3)) 


numberi = [ 
    ("raghaiid", 2002, [30, 55, 3, 10, 2, 54]),
    ("mohammeiid", 2004, [20, 5, 33, 10, 22, 4] )       
]

# استخدام حلقة for لتفكيك العناصر
for name, date, rate in numberi:
    average = sum(rate) / len(rate)  # حساب المتوسط
    print(f" {name} ({date}): Average rating for {round(average, 2)} ★")
      