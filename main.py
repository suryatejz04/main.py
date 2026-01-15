def power_sum(arr, ind):
    if ind == len(arr):
        return 0
    if arr[ind] <= 0:
        return arr[ind] ** 4 + power_sum(arr, ind + 1)
    return power_sum(arr, ind + 1)

def X(t):
    if t == 0:
        return
    n = int(input())
    arr = list(map(int, input().split()))
    print(power_sum(arr, 0))
    X(t - 1)  # call itself, not handle_tests

def main():
    t = int(input())
    X(t)

if __name__ == "__main__":
    main()
