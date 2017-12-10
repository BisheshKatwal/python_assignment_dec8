def acceleration(v,u,t):
    """Function to calculate value of a"""
    return ((v-u)/t)


v=20
u=0
t=10
a= acceleration(v,u,t)
print("The acceleration is {0:.3f} m/s^2 when v={1:.3f} m/s,u={2:.3f} m/s and t={3:.3f} sec".format(a,v,u,t))

