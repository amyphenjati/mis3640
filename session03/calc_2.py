# exercis02

# 2.1
pi = 3.1415926535897932
r = 5.0
print(4.0 / 3.0 * pi * r ** 3)

# 2.2
cover_price = 24.95
discounted_price = cover_price * 0.6
number_of_books = int(input("How many books in the wholesale order? "))
shipping = 3 + (0.75 * (number_of_books - 1))
wholesale_cost = discounted_price * number_of_books + shipping
print(
    "Total wholesale cost of", number_of_books, "books is $", round(wholesale_cost, 2)
)

# 2.3
start_time_hour = 6 + (52 / 60)
easy_pace_hour = (8 + (15 / 60)) / 60
tempo_pace_hour = (7 + (12 / 60)) / 60
total_run_time_hour = 2 * easy_pace_hour + 3 * tempo_pace_hour

breakfast_hour = start_time_hour + total_run_time_hour
breakfast_min = (breakfast_hour - int(breakfast_hour)) * 60

print("breakfast at", int(breakfast_hour), ":", int(breakfast_min))

# 2.4
print(round(((89 - 82) / 82) * 100, 1), "%")
