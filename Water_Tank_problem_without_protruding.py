def Water_Tank_Protruding(heights):
    left_ptr = 0
    right_ptr = len(heights)-1
    max_area = 0
    while left_ptr < right_ptr:
        width_tank = right_ptr - left_ptr
        min_side = min(heights[right_ptr],heights[left_ptr])
        
        procrude = False
        
        for i in range(left_ptr+1,right_ptr):
            if heights[i] > min_side:
                procrude = True        
        if not procrude:
            area = width_tank * min_side
            max_area = max(max_area,area)
        
        if heights[left_ptr]<heights[right_ptr]:
            left_ptr+=1
        else:
            right_ptr-=1
    return max_area
heights = [1,8,6,2,5,4,9,3,7] 
heights1 = [1,1] 
print(Water_Tank_Protruding(heights))
print(Water_Tank_Protruding(heights1))
