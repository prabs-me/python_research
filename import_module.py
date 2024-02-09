from my_module.my_math_module import add_numbers, sub_numbers

if __name__ == "__main__":
    num1 = 10
    num2 = 6
    add_result = add_numbers(num1,num2)
    print("added result\n",add_result)

    sub_result = sub_numbers(num1,num2)
    print("subtracted result\n", sub_result)
