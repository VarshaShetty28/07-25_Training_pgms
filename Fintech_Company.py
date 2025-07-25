feed_a = [ 
(1609459200, 150.25), # 2021-01-01 00:00:00 
(1609459260, 150.80), # 2021-01-01 00:01:00 
(1609459320, 151.15), # 2021-01-01 00:02:00 
(1609459380, 150.90), # 2021-01-01 00:03:00 
(1609459500, 151.40), # 2021-01-01 00:05:00 
(1609459620, 151.75), # 2021-01-01 00:07:00
] 
# Market Feed B (NASDAQ data) 
feed_b = [ 
(1609459220, 2500.30), # 2021-01-01 00:00:20 
(1609459280, 2501.15), # 2021-01-01 00:01:20 
(1609459400, 2499.80), # 2021-01-01 00:03:20 
(1609459460, 2502.45), # 2021-01-01 00:04:20 
(1609459580, 2503.10), # 2021-01-01 00:06:20 
(1609459640, 2504.25), # 2021-01-01 00:07:20
]

# def mergeInPlace(feed_a,feed_b):
#     i=0
#     j=0
#     merged=[]
#     while i<len(feed_a) and j<len(feed_b):
#         if feed_a[i][0]<=feed_b[j][0]:
#             merged.append(feed_a[i])
#             i+=1
#         else:
#             merged.append(feed_b[j])
#             j+=1
#     while i<len(feed_a):
#         merged.append(feed_a[i])
#         i+=1
#     while j<len(feed_b):
#         merged.append(feed_b[j])
#         j+=1
#     feed_a[:]=merged
        
#     return feed_a 
def merge_in_place_end(feed_a, feed_b):
    m = len(feed_a)
    n = len(feed_b)
    feed_a.extend([0] * n)
 
    
    i = m - 1  
    j = n - 1  
    k = m + n - 1  

    while i >= 0 and j >= 0:
        if feed_a[i][0] > feed_b[j][0]:
            feed_a[k] = feed_a[i]
            i -= 1
        else:
            feed_a[k] = feed_b[j]
            j -= 1
        k -= 1

    while j >= 0:
        feed_a[k] = feed_b[j]
        j -= 1
        k -= 1

    return feed_a   

def overlaps(feed_a,feed_b,window=30):
    overlap=[]
    i=0
    j=0
    while i<len(feed_a) and j<len(feed_b):
        diff=abs(feed_a[i][0]-feed_b[j][0])
        if diff<=window:
            overlap.append((feed_a[i],feed_b[j]))
            i+=1
            j+=1
        elif feed_a[i][0]<feed_b[j][0]:
            i+=1
        else:
            j+=1
    return overlap
        
                
merged = merge_in_place_end(feed_a, feed_b)
print("Merged feed:")
for item in merged:
    print(item)

overlap_pairs = overlaps(feed_a, feed_b)
print("\nOverlapping pairs:")
for pair in overlap_pairs:
    print(pair)
