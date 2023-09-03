admins={'Justin','David'}
users={'Mary','Nicole','Justin'}

#intersect = admins & users
intersect = admins.intersection(users)
print("交集:", intersect)

#union = admins | users
union = admins.union(users)
print("聯集:", union)

#difference1 = admins - users
difference1 = admins.difference(users)
print("差集:", difference1)
#difference2 = users - admins
difference2 = users.difference(admins)
print("差集:", difference2)

#sym_difference = admins ^ users
sym_difference = admins.symmetric_difference(users)
print("對稱差集:", sym_difference)
