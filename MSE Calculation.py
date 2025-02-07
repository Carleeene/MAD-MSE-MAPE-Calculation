#Mean Squared Error and Sample Variance calculation

#per as Period
per = int(input('Total Period of Operations: '))

#Error Squared calculation
#e as Error
#eSquared as Error Squared
def squared():
    squared = 0
    e = []
    for i in range(per):
        er = int(input(f'Enter the Error Value for Period {1+i}: '))
        e.append(er)
    
    for x in e:
        squared += abs(x**2)
    return squared

eSquared = squared()

#Calculate the MSE and Sample Variance
#mse_Sample as Mean Squared Error Sample Variance
#mse as Mean Squared Error
mse_Sample = eSquared/(per-1)
mse = eSquared/per
print(f'MSE: {mse}\nMSE Sample Variance: {mse_Sample}')
