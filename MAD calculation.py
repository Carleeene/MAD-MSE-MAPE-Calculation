#Mean Absolute Deviation calculation 

#per variable as Periods
per = int(input('Total Period of Operations: '))

#Calculate the Sum of Errors
#av as Actual Values
#fv as Forecast Values
#er as Error
def e():
    error = 0
    av = []
    fv = []
    for i in range(per):
        av.append(int(input(f'Input the Actual Value for Period {1+i}: ')))
        fv.append(int(input(f'Input the Forecast Value for Period {1+i}: ')))

    for a, f in zip(av, fv):
        error += abs(a - f)
    return error

er = e()

#MAD calculation
#mad as Mean Absolute Deviation
mad = round(er/per, 2)
print(f'Mean Absolute Deviation: {mad}')
