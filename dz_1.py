# Первая задача - опредление суммы трехзначного числа
n = int (input ("Введите трехзнаное число "))
a = n//100
b = (n%100)//10
c = (n%100)%10
print (int(a + b + c))

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

s = int (input ("Введите количесто журавликов "))
print ("Катя сделала" , int (s/2), "Петя и Сережа сделали по ", int((s/2)/2))
