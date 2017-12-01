#1-1-2 vectors - algebra refresh
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        #return round(new_coordinates, 3)#<======================CZEMU NIE MOGE UZYC ROUND ??????????????????
        return Vector(new_coordinates)
    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    def multiply(self, a):
        new_coordinates = [a * x for x in self.coordinates]
        return Vector(new_coordinates)

# plus
vector_1 = Vector([8.218, -9.341])
vector_2 = Vector([-1.129, 2.111])
print (vector_1.plus(vector_2))
# minus
vector_3 = Vector([7.119, 8.215])
vector_4 = Vector([-8.223, 0.878])
print (vector_3.minus(vector_4))

# scalar multiply
vector_5 = Vector([1.671, -1.012, -0.318])
print (vector_5.multiply(3))
