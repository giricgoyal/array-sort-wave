import queue

arr = [1, 2, 3, 4, 7, 5]

def swapInArr(arr, x, y):
	arr[x] = arr[x] + arr[y]
	arr[y] = arr[x] - arr[y]
	arr[x] = arr[x] - arr[y]
	return arr

def main():
	global arr
	n = len(arr)
	for i in range(0, n, 2):
		if ((i > 0) and (arr[i - 1] > arr[i])):
			arr = swapInArr(arr, i - 1, i)
		if ((i < n - 1) and (arr[i] < arr[i + 1])):
			arr = swapInArr(arr, i + 1, i)
	print(arr)

if __name__ == "__main__":
	main()