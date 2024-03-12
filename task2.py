from queue import deque

def is_palindrome(test_str):
    test_str = test_str.lower()
    chars_queue = deque()

    for char in test_str:
        if char.isalnum():
            chars_queue.append(char)

    while len(chars_queue) > 1:
        if chars_queue.popleft() != chars_queue.pop():
            return False

    return True


if __name__ == "__main__":
    print("Enter a string to test if that is palindrom, or press Ctrl+C to exit")

    while True:
        try:
            str = input("Enter a string to test: ")
    
            if str == '':
                raise EOFError
    
            result = is_palindrome(str)
            verb = "is" if result else "isn't"
            print(f"That {verb} palindrom")
        except (KeyboardInterrupt, EOFError):
            print("\n")
            break