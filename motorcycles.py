motorcycles = ['honda', 'suzuki', 'yamaha']
motorcycles[0]= 'ducati'
print(motorcycles)

#adding item to end of a list
motorcycles = ['honda', 'suzuki', 'yamaha']
motorcycles.append('ducati')
print(motorcycles)

#building lists dyamically
super_cars = []
super_cars.append('porsche')
super_cars.append('ferrari')
super_cars.append('lamborghini')
#adds item at a certain positon
super_cars.insert(0,'amg')
print(super_cars)
#delete from list
del super_cars[0]
print(super_cars)

cats = ['haku', 'maru', 'garfield']
pop_cat = cats.pop()
print(cats)
print(pop_cat)