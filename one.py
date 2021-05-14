def fun():
    print("This is my function!")

print("Top level print statement!")

if __name__ == "__main__":
    print("This is my main function")
    fun()
else:
    print("This is imported part!")