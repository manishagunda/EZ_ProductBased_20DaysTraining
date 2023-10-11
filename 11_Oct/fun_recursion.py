def fun(n):
    if n<=2:return
    print(n)
    fun(n-2)
    fun(n-4)
    print(n)
fun(10)