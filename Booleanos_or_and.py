#sub-expression1 or sub-expression2

#rules

#subexpression1	Operador	subexpression2	Resultado
#True	        and	            True	        True
#True	        and	            False	        False
#False	        and	            True	        False
#False	        and	            False	        False

#subexpression1	Operador	subexpression2	Resultado
#True	           or	        True	        True
#True	           or	        False	        True
#False	           or	        True	        True
#False	           or	        False	        False

a = 23
b = 34
if a == 23 and b == 34:
    print (a + b)