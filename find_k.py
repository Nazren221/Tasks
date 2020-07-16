def prime(x):
    count=0
    for i in range(2, x+1):
        if x % i ==0:
            count+=1
    if count==1:
        return x
    else:
        return 0
   
sum=2
n=1
x=3
k=int(input())
while sum % k != 0:
    a=prime(x)
    if a!=0:
        sum+=a 
        n+=1
    x+=1
   
print(n)


# sadəliyi yoxlamaq üçün ayrı bir funksiya yazdım. burda şərti elə yazdım ki ədədin təkcə özünə bölməsi hesablansın. və toplama üçün geri dəyər ötürsün.
# cemi 2 i götürdüm ki, ilk   sadə eded zatən 2 di və n say da 1 dən başlasın. if hissə bizim sadə ədədimizi yoxlayıb N i artırır və onu cəmə əlavə edəcək 