#!/usr/bin/python3

directory = {   "linux-stable" :
                    {"yes" , "yes_2", "yes_3"},
                "python_dict" : "yes" ,
                "ye_olde_skynet" : "no"
            }

def create_dir(directory):
    for filename in directory:
        if not isinstance(directory[filename],dict):
            print("Found file" , filename)
            print("Found file[file]" , directory[filename])
        else:
            create_dir(directory[filename])
def main():
    create_dir(directory)

if __name__ == "__main__":
    main()
