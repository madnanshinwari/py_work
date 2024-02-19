# break
# for i in range(12):
#     if i == 10:  # loop is end  on 10 iteration
#         break
#     print("5 X", i+1, "=", 5 * (i+1))


# continue
for i in range(12):
    if (i == 10):
        # continue keyword skip the iteration and continue other statements
        print("iteration skip!")
        continue
print("5 X", i, "=", 5 * (i))
