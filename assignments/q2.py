with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.\nLine 2 here.")

with open("sample.txt", "r") as f:
    print("First read:")
    print(f.read(5))

    f.seek(0)
    print("\nAfter seek(0), read again:")
    print(f.read(5))

    f.seek(7)
    print("\nAfter seek(7), read next 9 characters:")
    print(f.read(9))
