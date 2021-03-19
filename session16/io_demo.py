import os

#  print(os.getcwd())

# fout = open('data/output.txt', 'w')
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# context manager
with open('data/output.txt', 'w') as fout:
    line1 = "How many roads must a man walk down\n"
    fout.write(line1)
    line2 = "Before you call him a man?\n"
    fout.write(line2)


f = open
