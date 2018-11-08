# Все задачи текущего блока решите с помощью генераторов списков!
import random
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
lst_g = [random.randint(-10, 10) for _ in range(10)]
print("Задание 1\n",lst_g)
only_org = [el*el for el in lst_g]
print(only_org)



# Задание-2:
# Даны два списка фруктов.
fruits1 = [random.randint(-10, 10) for _ in range(2)]
fruits2 = [random.randint(-10, 10) for _ in range(3)]
fruits1.append(2)
fruits2.append(2)
#fruits1 = ["клубника","груша","грейпфрут","банан"]
#fruits2 = ["яблого","банан","киви","апельсин"]
print("\n Задание 2\n",fruits1)
print(fruits2)
# Получить список фруктов, присутствующих в обоих исходных списках.
allfruits = []
allfruits = list(set(fruits1 + fruits2))
print(allfruits)


# Задание-3:
# Дан список, заполненный произвольными числами.
lst_g = [random.randint(-10, 10) for _ in range(10)]
print("Задание 3\n",lst_g)
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
only_org = [el for el in lst_g if el%3 == 0 and el >= 0 and el%4 != 0]
print(only_org)