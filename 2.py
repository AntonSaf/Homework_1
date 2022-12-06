# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.


for X in [True, False]:
    for Y in [True, False]:
        for Z in [True, False]:
            res = not (X or Y or Z) == ((not X) and (not Y) and (not Z))
            print (f'x = {X}, y = {Y}, z = {Z}  =>  Result = {res}')