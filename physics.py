# Ryan Frazier 
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1



# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  force = mass * acceleration
  return str(force)

train_force = get_force(train_mass, train_acceleration)

print(train_force)

print("The GE train supplies " + train_force + " Newtons of force.")

def get_energy(mass, c):
  total_energy = mass * c ** 2
  return total_energy

bomb_energy = get_energy(bomb_mass, c = 3 * 10**8)
print(str(bomb_energy))

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print(train_work)

print("The GE train does " + train_work + "joules of work over " + str(train_distance) + " meters.")