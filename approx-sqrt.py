def sqrt(x):
    #   Initial guess
    z = 1.0
    #   Keep getting a better estiate for the sqrt of x
    #   until you are within 2 decimal places
    while abs(z*z - x) >= 0.01:
        #   Get a better approximation for sqrt
        z -= (z*z - x) / (2*z)

    return z


#   Calculate the sqrt of 8
z = sqrt(16.0)
#   Print z
print(z)
#   Print the sqrt of z
print(z*z)