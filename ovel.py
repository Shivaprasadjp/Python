chr=['a','b','e','i','o','u','z']
result=list(filter(lambda x:x in "aeiou",chr))
print(result)

startswith_h=lambda s:s.startswith('h')
print(startswith_h('hello'))


num=[15,30,10,45,60,22]
res=list(filter(lambda x : x%3==0 and 5==0,num))
print(res)

filter out all string longer then 5 charecter in a list
input['apple','banana','cat','dog','elephant',dainosor]

lst=['apple','banana','cat','dog','elephant','dainosor']
res=list(filter(lambda x : len(x)<=5,lst))
print(res)