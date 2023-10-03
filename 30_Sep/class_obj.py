class MyClass:
    def __init__(self, str_val, int_val, int_val1):
        self.str_val = str_val
        self.int_val = int_val
        self.int_val1=int_val1

    def reverse_string_and_print_square(self, str_arg, int_arg):
        reversed_str = "".join(reversed(str_arg))
        squared_int = int_arg ** 2
        print("Reversed String:", reversed_str)
        print("Square of Integer:", squared_int)

    def display_results(self):
        str_length = len(self.str_val)
        modulo_result = self.int_val1 % self.int_val
        print("Length of String:", str_length)
        print("Modulo Division Result:", modulo_result)

# Example usage:
a=int(input())
b=int(input())
c=input()
my_instance = MyClass(c,a,b )
my_instance.reverse_string_and_print_square(c,a)
my_instance.display_results()