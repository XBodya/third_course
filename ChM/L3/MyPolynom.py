import numpy as np

class MyPolynom():
    def __init__(self, degrees):
        """
        self.degree_array - array of polynom degrees
        self.degree_array[i] <=> coefficient of (i sequal of polynom)
        """
        self.degree_array = degrees if isinstance(type(degrees), type(np.array([]))) else np.array(degrees )

    @property
    def degree(self):
        return self.degree_array.size - 1

    def __add__(self, other):
        if self.degree_array.size < other.degree_array.size:
            return MyPolynom(other.degree_array + np.pad(self.degree_array, (0, max(self.degree_array.size, other.degree_array.size) - min(self.degree_array.size, other.degree_array.size)), 'constant', constant_values=(0)))
        else:
            return MyPolynom(self.degree_array + np.pad(other.degree_array, (0, max(self.degree_array.size, other.degree_array.size) - min(self.degree_array.size, other.degree_array.size)), 'constant', constant_values=(0)))
        # return MyPolynom(self.degree_array + other.degree_array)

    def __sub__(self, other):
        if self.degree_array.size < other.degree_array.size:
            return MyPolynom(np.pad(self.degree_array, (0, max(self.degree_array.size, other.degree_array.size) - min(self.degree_array.size, other.degree_array.size)), 'constant', constant_values=(0)) - other.degree_array)
        else:
            return MyPolynom(self.degree_array - np.pad(other.degree_array, (0, max(self.degree_array.size, other.degree_array.size) - min(self.degree_array.size, other.degree_array.size)), 'constant', constant_values=(0)))
        # return MyPolynom(self.degree_array + other.degree_array)


    def __mul__(self, other):
        result = np.zeros((self.degree_array.size + other.degree_array.size) - 1)
        for i in range(self.degree_array.size):
            for j in range(other.degree_array.size):
                result[i + j] += self.degree_array[i] * other.degree_array[j]
        return MyPolynom(result)

    def __str__(self):
        return str(self.degree_array)

    def get_value(self, x):
        return sum([np.pow(x, i) * self.degree_array[i] for i in range(self.degree + 1)])

    @property
    def get_lambda(self):
        return lambda x: sum([np.pow(x, i) * self.degree_array[i] for i in range(self.degree + 1)])

if __name__ == '__main__':
    # MyPolynom(1, 2, 3) + MyPolynom(2, 3, 4)
    n = MyPolynom([1, 2])
    q = MyPolynom([1, 0, 2] * 1000)
    print(q)
    q = q * n
    lq = q.get_lambda
    print(q.get_value(0))
    print(lq(1))