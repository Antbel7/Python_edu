# Первая задача - опредление суммы трехзначного числа
n = int (input ("Введите трехзнаное число "))
a = n//100
b = (n%100)//10
c = (n%100)%10
print (int(a + b + c))