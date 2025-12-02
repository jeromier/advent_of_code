from scipy.linalg import solve

A = [ [26, 66], [67, 21]]
b = [12748, 12176]

x = solve(A,b)

print(x)