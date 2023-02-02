def create_file_from_string(my_filename, my_string):
    my_filename = open(my_filename,"x")
    my_filename.write(my_string)

def print_file_on_screen(my_filename):
    my_filename = open(my_filename)
    print(my_filename.read())

create_file_from_string("fil.txt","hej")
print_file_on_screen("fil.txt")
    