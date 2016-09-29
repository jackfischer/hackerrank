

s = input().strip()

def buckets(s):
    buckets = []
    temp = None
    for c in s:
        if c != temp:
            buckets.append([c])
            temp = c
        else:
            buckets[-1].append(c)
    return buckets

def bucketToString(bucket):
    result = []
    for b in bucket:
        if (len(b) % 2) == 1:
            result.append(b[0])
    return ''.join(result)



while True:
    bucket = buckets(s)
    temp = bucketToString(bucket)
    if temp == s:
        if temp:
            print(temp)
        else:
            print("Empty String")
        break
    else:
        s = temp
