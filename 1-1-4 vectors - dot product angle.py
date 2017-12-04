"""Use a set of functions for vectors."""
from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    """Use that class for playing with vectors."""

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        """Use it to initiate vectors."""
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        """Use that function for printing vector."""
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        """Use this function to compare two vectors."""
        return self.coordinates == v.coordinates

    def plus(self, v):
        """Use if for adding two vectors."""
        new_coordinates = \
            [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        """Use if for distracting two vectors."""
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def multiply(self, a):
        """Use if for multiplying two vectors."""
        new_coordinates = [Decimal(a) * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        """Use if for magnitude calculation."""
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))
        '''
        calculated_mag = 0
        for x in range(len(self.coordinates)):
            calculated_mag += self.coordinates[x] * self.coordinates[x]
        calculated_mag = sqrt(calculated_mag)
        return calculated_mag
        '''

    def normalized(self):
        """Use if to calculate a normalization of a vector."""
        try:
            calculated_mag = self.magnitude()
            return self.multiply(Decimal('1.0')/calculated_mag)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
        '''
        calculated_dir = 1/self.magnitude()
        calculated_dir = self.multiply(calculated_dir)
        '''
    def product(self, v):
        """Use if for calculation a dot product of two vectors."""
        calculated_product = 0
        for x, y in zip(self.coordinates, v.coordinates):
            calculated_product += x * y
            print (calculated_product)
        return calculated_product

    def angle(self, v, in_degrees=False):
        """Use if to calculate angle between two vectors."""
        calculated_angle = 0
        try:
            v_1 = self.normalized()
            v_2 = v.normalized()
            angle_in_radians = acos(v_1.product(v_2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians / degrees_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute \
                    an angle with the zero vector ')
            else:
                raise e
        pass

# plus
# vector_1 = Vector([8.218, -9.341])
# vector_2 = Vector([-1.129, 2.111])
# print (vector_1.plus(vector_2))

# minus
# vector_3 = Vector([7.119, 8.215])
# vector_4 = Vector([-8.223, 0.878])
# print (vector_3.minus(vector_4))

# scalar multiply
# vector_5 = Vector([1.671, -1.012, -0.318])
# print (vector_5.multiply(3))

# magnitude
# vector_6 = Vector([-0.221, 7.437])
# vector_7 = Vector([8.813, -1.331, -6.247])
#
# print (vector_6.magnitude())
# print (vector_7.magnitude())

# direction / normalization
# vector_8 = Vector([5.581, -2.136])
# vector_9 = Vector([1.996, 3.108, -4.554])
# vector_10 = Vector([0, 0, 0])
#
# print (vector_8.normalized())
# print (vector_9.normalized())
# print (vector_10.normalized())

# dot product & angle
vector_11 = Vector([7.887, 4.138])
vector_12 = Vector([-8.802, 6.776])
vector_13 = Vector([-5.955, -4.904, -1.874])
vector_14 = Vector([-4.496, -8.755, 7.103])

vector_15 = Vector([3.183, -7.627])
vector_16 = Vector([-2.668, 5.319])
vector_17 = Vector([7.35, 0.221, 5.188])
vector_18 = Vector([2.751, 8.259, 3.985])

print (vector_11.product(vector_12))
print (vector_13.product(vector_14))

print (vector_15.angle(vector_16))
