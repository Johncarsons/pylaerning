# list datastructures
# list are mutable(changeable)
# lists are ordered
# lists have indexes
# lists are declared be box bracket[]
fruits=['apple','banana','mangoes','pineapple','orange','strawberry', 'pear']
print(fruits)
fruits[2]= "Pawpaw"
print (fruits)
print(f"I love eating {fruits[5]}")
print(f"I hate eating {fruits[4]}")
print(f"I like eating {fruits[2]}")
print(f"I dislike eating {fruits[6]}")
numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(10)

print(numbers[2:7])
print(numbers[9])

# tuple data structures
# tuple are immutable(unchangeable)
# tuple are ordered
# tuple have indexes
# tuple are declared by normal bracket()
cars = ('BMW','Audi','Bently','Mercedes','Subaru','Toyota','Aston Martin','Ford','Suzuki','Ferari','Nissan','Dodge')
print(cars[2])
print(cars[2:10])
print(cars[3])
nambari = (1,2,3,4,5,6, 7, 8, 9)
print(len(cars))
# set datastructures
# sets are unorderd
# sets do not have indexes
# sets are immutable (unchangeable)
# sets aredeclared using calibraces {}
# bikes = {'Kawasaki', 'Ducati', 'Yamaha', 'Aprilia','Taro'}
# print(bikes)
days = {"Monday", 'Teusday','Wednesday','Thursday','Friday','Saturday','Sunday'}
print(days)

# dictionaries data structures
students = {"Name": "Carson", "Age":18, "Gender":"Male", "School":"eMobilis"}
print(students)
print (students["Name"])
print (students["Age"])
print (students["Gender"])
print (students["School"])