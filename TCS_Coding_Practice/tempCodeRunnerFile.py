def count_distinct_optimal(arr, k):
    n = len(arr)
    freq = {}
    result = []

    # first window
    for i in range(k):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    result.append(len(freq))

    # sliding window
    for i in range(k, n):
        incoming = arr[i]
        outgoing = arr[i-k]

        freq[incoming] = freq.get(incoming, 0) + 1

        freq[outgoing] -= 1
        if freq[outgoing] == 0:
            del freq[outgoing]

        result.append(len(freq))

    return result


arr = [1,2,1,3,4,2,3]
k = 4
print(count_distinct_optimal(arr,k))