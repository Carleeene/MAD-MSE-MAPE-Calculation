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
        actual = int(input(f'Input the Actual Value for Period {1+i}: '))
        av.append(actual)

    for x in range(per):
        forecast = int(input(f'Input the Forecast Value for Period {1+x}: '))
        fv.append(forecast)

    for a, f in zip(av, fv):
        error += abs(a - f)
    return error

er = e()

#MAD calculation
#mad as Mean Absolute Deviation
mad = int(er/per)
print(f'Mean Absolute Deviation: {mad}')
