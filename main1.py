#list comprhension example
fruitbowl=['banana','apple','oranges','grapes','watermelon']
formula=[x for x in fruitbowl if 'r'in x]
print(formula)
brand=[x for x in fruitbowl if x!='apple']
print(brand)