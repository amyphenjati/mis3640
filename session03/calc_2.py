# exercis02

# 2.1
pi = 3.1415926535897932
r = 5.0
v = 4.0 / 3.0 * pi * r ** 3
print(f'Volume of a sphere with radius=5 is{v:.2f}')

# 2.2
wholesale_cost = (24.95*0.60)*60+3+0.75*(60-1)
print(f'Total wholesale cost of 60 books is $ {wholesale_cost:.2f}')

# 2.3
start_time_hour = 6 + (52 / 60)
easy_pace_hour = (8 + (15 / 60)) / 60
tempo_pace_hour = (7 + (12 / 60)) / 60
total_run_time_hour = 2 * easy_pace_hour + 3 * tempo_pace_hour

breakfast_hour = start_time_hour + total_run_time_hour
breakfast_min = (breakfast_hour - int(breakfast_hour)) * 60

print(f'breakfast at {int(breakfast_hour)}:{int(breakfast_min)}')

# 2.4
perc_change = ((89 - 82) / 82) * 100
print(f'{perc_change:.1f}%')
