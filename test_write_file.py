from functions.write_file import write_file

def test():
    result = write_file("calculator", "lorem.txt", "This is another test content.")
    print("Result of write_file:", result)
    print("")
    
    result = write_file("calculator", "pkg/test.txt", "Trying to write outside working directory.")
    print("Result of write_file:", result)
    
if __name__ == "__main__":
    test()
