# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Wei Wang>,<08.30.2022>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Wei Wang>,<8.31.2022>,Modified code to complete assignment 8
    """

    #  -- Constructor --
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

    # -- properties --
    # Product Name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers!")

    # Product Price
    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise ("Price must be numbers! \n\t" + e.__str__().title())

    # -- Methods --
    def show(self):
        print("product name: " + self.product_name + ", " + "product price: " + self.product_price)


# Data ----------------------------------------------------------------------

# Processing ----------------------------------------------------------------

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Wei Wang>,<08.31.2022>,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        with open(file_name, "w") as file:
            for product in list_of_product_objects:
                file.write(product.product_name + "," + product.product_price + "\n")

    @staticmethod
    def read_data_from_file(file_name):
        list_of_product_objects = []
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                list_of_product_objects.append(Product(line.split(",")[0].strip(), line.split(",")[1].strip()))
        return list_of_product_objects


class IO:
    """ Handle input and output:

    methods:
        show_menu():
        get_menu_input(file_name): -> (file_name)
        show_current_data(file_name):
        show_current_data_from_file(file_name): -> (file_name)
        get_menu_input():
        bye():
    """

    # TODO: Add code to show menu to user
    def show_menu():
        print("""
        Menu of Options
        1) Add Data
        2) Show current data
        3) Load data from file
        4) Save data to file
        5) Exit Program
            """)

    @staticmethod
    def get_menu_input():
        return str(input("Which option would you like to perform? [1 to 5] -")).strip()

    @staticmethod
    def show_current_data_from_file(file_name):
        for product in FileProcessor.read_data_from_file(file_name):
            product.show()

    @staticmethod
    def show_current_data():
        for product in lstOfProductObjects:
            product.show()

    @staticmethod
    def input_product_data():
        product_name = input("Input product name: ")
        product_price = input("Input product price: ")
        return Product(product_name, product_price)

    @staticmethod
    def bye():
        print("bye")


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

# Show user a menu of options
while True:
    IO.show_menu()
    strChoice = IO.get_menu_input()
    match strChoice:
        case "1":
            lstOfProductObjects.append(IO.input_product_data())
            pass
        case "2":
            IO.show_current_data()
            pass
        case "3":
            IO.show_current_data_from_file(strFileName)
            pass
        case "4":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            pass
        case "5":
            IO.bye()
            break

# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
