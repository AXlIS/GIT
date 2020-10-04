from statistics import median

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]"""

numbers = [2, 8, 5, 1, 4, 9, 0, 7, 1, 7, 9, 8, 10]


def medians(nums):
    half = len(nums) // 2
    for i in range(len(nums)):
        index = i
        for j in range(i, len(nums)):
            if nums[index] > nums[j]:
                index = j
        nums[index], nums[i] = nums[i], nums[index]
    if len(nums) % 2 == 0:
        return (nums[half - 1] + nums[half]) / 2
    return nums[half]


print('Исходный массив:', numbers)
print('Медиана:', medians(numbers[:]))
print('Медиана statistics:', median(numbers[:]))
