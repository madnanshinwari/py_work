# num1 = 20
# num2 = 30


def cal(num1, num2):
    # if (product > 1000):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2


mul_result = cal(20, 30)
print("the multiplication is :", mul_result)
sum_result = cal(40, 30)
print("the addition is : ", sum_result)
