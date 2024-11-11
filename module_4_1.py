# Задача "А как делить?":
# В школе нам говорили, что на 0 делить нельзя. Высшая же математика опровергает это и говорит,
# что результат при делении на 0 будет стремиться к бесконечности.
# Давайте реализуем оба способа, чтобы у вас всегда был выбор!
from fake_math import divide as fake_divide
from true_math import divide as true_divide
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1, type(result1))
print(result2, type(result2))
print(result3, type(result3))
print(result4, type(result4))