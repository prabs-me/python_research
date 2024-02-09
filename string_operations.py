def substring_operation(in_str:str):
    sub_string = in_str[2:4]
    print(sub_string)

def split_operation(in_str:str):
    splitted_string = in_str.split(" ")
    part_split_str = in_str.split(" ",2)
    print(splitted_string)
    print(part_split_str)


if __name__ == "__main__":
    input_string = "prabhat"
    split_string = "My Name Is Prabhat"
    substring_operation(input_string)

    split_operation(split_string)
