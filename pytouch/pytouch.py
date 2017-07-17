import sys

def main():
    # sys.argv[0] is the path to the python interpreter
    # sys.argv[1] should contain the name of the file we want to create
    if len(sys.argv) != 2:
        raise ValueError("Please provide the name of the file to create.")

    filename = sys.argv[1]

    # 'w+' erases the file if it exists and creates it if the file doesn't exist
    with open(filename, 'w+'):
        pass
