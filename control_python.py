
def age_determination(age):
    if age > 18:
        print("The person is an adult")
    else:
        print("The person is not an adult")


def print_item_in_list(item_list):
    for item in item_list:
        print(item)

def print_numbers_0_to_20():
    for i in range(20):
        print(i)

if __name__== "__main__":
    #age=input("Input your age\n")
    #print("your age is",age)
    #age_determination(int(age))
    #item_list = ["Apple","Orange", "Strawberry", "Banana"]
    #print_item_in_list(item_list)
    #print("First Item in list is:\n",item_list[0])
    #print("Second Item in list is:\n",item_list[1])
    #print("Third Item in list is:\n",item_list[2])
    #print("Fourth Item in list is:\n",item_list[3])

    #print_numbers_0_to_20()

    color_matrix = [["red","orange","blue"],["yellow","pink"],["green"]]

    for color_list in color_matrix:
        for color in color_list:
            print(color)