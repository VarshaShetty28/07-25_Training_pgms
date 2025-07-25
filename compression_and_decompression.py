def compression_decompression(nums):
    dictionary={}
    for i in nums:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    print(f"Compressed output\n",dictionary)
    print("Decompressed Output:")
    for key, count in dictionary.items():
        for i in range(count):
            print(key, end=' ')

nums = [2,2,2,1,1,1,5,5,6,9]
compression_decompression(nums)
