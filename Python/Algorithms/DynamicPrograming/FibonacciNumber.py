def fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib


if __name__ == "__main__":
    ans = fibonacci(15)
    print(ans)
