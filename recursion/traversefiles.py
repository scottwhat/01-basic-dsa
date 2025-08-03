import os
import argparse

def print_subdirectories(directory_name):
    for filename in os.listdir(directory_name):
        if os.path.isdir(os.path.join(directory_name, filename)):
            path = os.path.join(directory_name, filename)
            print(path)
            
            # Do the action then make another call 
            print_subdirectories(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traverse directories and print subdirectories.")
    parser.add_argument("directory", type=str, help="The directory to traverse")
    args = parser.parse_args()

    print_subdirectories(args.directory)