import math

p1 = math.radians(float(input("Enter latitude 1: ")))
m1 = math.radians(float(input("Enter longtitude 1: ")))
p2 = math.radians(float(input("Enter latitude 2: ")))
m2 = math.radians(float(input("Enter longtitude 2: ")))

R = 6372.8

dp = p2 - p1
dm = m2 - m1

a = (math.sin(dp/2))**2 + math.cos(p1) * math.cos(p2) * (math.sin(dm/2))**2
c = 2 * math.asin(math.sqrt(a))

d = R * c

print('The distance between those two point is about {:.0f} km'.format(d))
