<<<<<<< Updated upstream
num = int(input('Количество процентов'))

str_perc = "процент"

if num == 1:
    end = ""
elif num in [2, 3, 4]:
    end = "a"
else:
    end = "ов"

=======
num = int(input('Количество процентов'))

str_perc = "процент"

if num == 1:
    end = ""
elif num in [2, 3, 4]:
    end = "a"
else:
    end = "ов"

>>>>>>> Stashed changes
print(str(num) + " " + str_perc + end)