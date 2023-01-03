nums = [9,6,7,8,1,2,5,4,3]

print("Было: ", nums)

for i in range(len(nums)): # O(N**2)
    lowest = i # первый элемент примем за наименьший
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j # нашли элемент меньше в правом срезе
    nums[i], nums[lowest] = nums[lowest], nums[i]

print("Стало: ", nums)

# Схожа с BubbleSort (пузырьковый метод)




        
    

 