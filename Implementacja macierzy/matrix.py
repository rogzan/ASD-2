class Array:
    def __init__(self, mat_, default_val=0):
        if isinstance(mat_, tuple):
            self.mat_ = [[default_val] * mat_[0]] * mat_[1]
        else:
            self.mat_ = mat_

    def __add__(self, other):
        if len(other.mat_) == len(self.mat_) and len(other.mat_[0]) == len(self.mat_[0]):
            result_matrix = Array(self)
            result_matrix.mat_ = []
            for i in range(len(self.mat_)):
                one_row = []
                for j in range(len(self.mat_[0])):
                    one_row.append(self.mat_[i][j] + other.mat_[i][j])
                result_matrix.mat_.append(one_row)
            return result_matrix

    def __mul__ (self, other):
        if len(other.mat_[0]) == len(self.mat_) and len(self.mat_[0]) == len(other.mat_):
            result_matrix = Array(self)
            result_matrix.mat_ = []
            for i in range(len(self.mat_)):
                one_row = []
                for j in range(len(other.mat_[0])):
                    sum = 0
                    for k in range(len(self.mat_[0])):
                        sum += self.mat_[i][k] * other.mat_[k][j]
                    one_row.append(sum)
                result_matrix.mat_.append(one_row)
            return result_matrix

    def __len__(self):
        rows = len(self.mat_)
        return rows

    def __getitem__(self, item):
        return self.mat_[item]

    def __str__(self):
        m = "["
        for i in range(len(self.mat_)):
            m += "["
            for j in range(len(self.mat_[0]) ):
                if j != len(self.mat_[0])-1:
                    m += str(self.mat_[i][j])
                    m += ", "
                else:
                    m += str(self.mat_[i][j])
            if i != len(self.mat_)-1:
                m += "]"
                m += ", "
            else:
                m += "]"
        m += "]"
        return m

def transpose(mat):
    result_matrix = []
    for i in range(len(mat[0])):
        one_row = []
        for j in range(len(mat)):
            one_row.append(mat[j][i])
        result_matrix.append(one_row)
    return result_matrix

if __name__ == "__main__":
    a1 = [[1, 0, 2],
        [-1, 3, 1]]
    b1 = [[1, 1, 1],
        [1, 1, 1]]
    c1 = [[3, 1], [2, 1], [1, 0]]

    a = Array(a1)
    b = Array((3,2), default_val=1)
    c = Array(c1)

    res1 = a + b
    res2 = a * c

    print(transpose(a))
    print(res1)
    print(res2)
