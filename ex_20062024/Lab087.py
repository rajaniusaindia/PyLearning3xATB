# tuple - multi-Dimension - Matrix
# Array kind of rarely used but just know them

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Spiderman", "Peter Parker")
l = len(hero1)
print(l)

new_tuple = hero1 + hero2
print(new_tuple) # ('Batman', 'Bruce Wayne', 'Spiderman', 'Peter Parker')
new_tuple = (hero1, hero2)
print(new_tuple) # (('Batman', 'Bruce Wayne'), ('Spiderman', 'Peter Parker'))

print(new_tuple[0]) # ('Batman', 'Bruce Wayne')
print(new_tuple[1]) # ('Spiderman', 'Peter Parker')

# From the 0 => 0
print(new_tuple[0][0]) # Batman

# 0,0
# 0,1
# 1,0
# 1,1

print(new_tuple[1][1]) # Peter Parker
