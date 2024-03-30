def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 98765\n")
            print("File created successfully.")
    except PermissionError:
        print("Permission error occurred. Unable to create the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation process completed.\n")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please create the file first.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading process completed.\n")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
            print("Content appended successfully.")
    except PermissionError:
        print("Permission error occurred. Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending process completed.\n")


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
