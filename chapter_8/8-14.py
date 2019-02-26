# 8-14. Cars: Write a function that stores information about
# a car in a dictionary. The function should always receive a
# manufacturer and a model name. It should then accept an arbitrary
# number of keyword arguments. Call the function with the required
# information and two other name-value pairs, such as a color or
# an optional feature. Your function should work for a call like this
# one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def make_car(manufacturer, model, **others):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in others.items():
        car[key] = value
    return car

car_profile = make_car('volkswagen', 'golf 4 (3.2 r32)', color='black',
year='2004', engine='vr6 24v', displ='3189 cc', power='177 kW (241 PS;\
 237 hp) @ 6250 rpm', torque='320 N⋅m (240 lb⋅ft) @ 2800 rpm')

print(car_profile)
