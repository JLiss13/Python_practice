class hash_tables:

    def __init__(self, name):
        self.name = name
        self.hash_table = dict()

    def set(self, key, value):
        if isinstance(key,str) and len(key) > 1:
            if isinstance(value,(int,float)):
                self.hash_table[key] = value
                return print(self.hash_table)
            else:
                return print("Value must be a number")
        else:
            return print("Key must be a string")
      

    def get(self, key):
        if isinstance(key,str) and len(key) > 1:
            return self.hash_table[key]
        else:
            print("Key must be a string")
    
if __name__ == '__main__':
    # Create the hash table example
    shopping_list_inst = hash_tables("20231030_shopping_list")

    # case 1
    key_1 = "grapes"
    price_1 = 1
    shopping_list_inst.set(key_1,price_1)

    # case 2
    key_2 = "apples"
    price_2 = 0.5
    shopping_list_inst.set(key_2,price_2)

    # case 3 (should return a error print statement)
    key_3=""
    price_3=100
    shopping_list_inst.set(key_3,price_3)


    # case 4 (should return a error print statement)
    key_4 = "stuff"
    price_4 = "asdf"
    shopping_list_inst.set(key_4,price_4)

    # case 5 (should check for the existance of the apples in the shopping list)
    print(shopping_list_inst.get("apples"))
