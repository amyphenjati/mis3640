import time

epoch = time.time()
print(f"Epoch time:{epoch}")

days = epoch / (60 * 60 * 24)
hours = days % int(days) * 24
minutes = hours % int(hours) * 60
seconds = minutes % int(minutes) * 60

print(
    f"The current time is {int(hours)} hours {int(minutes)} minutes and {int(seconds)} seconds. \n {int(days)} days since epoch."
)
