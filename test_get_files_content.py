from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "lorem.txt")
    print("Result", len(result))

if __name__ == "__main__":
    test()