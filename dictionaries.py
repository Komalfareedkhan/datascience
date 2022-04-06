from turtle import update


food={"rice":200,"apples":250,"milk":70}
print(food)
print(type(food))
print(food.keys())
#print(food)
print(food.values())
update1={"dates":200}
#print(food)
food.update(update1)
print(food)
#print(food)
change_in_price={"apples":150}
food.update(change_in_price)
print(food)
#when tuple is passed in update
food.update(orange=120,banana=150)
print(food)