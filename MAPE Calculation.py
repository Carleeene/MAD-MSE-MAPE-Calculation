#Mean Absolute Percentage Error Calculation

#per variable as Period
per = int(input('Total Period of Operations: '))

#Calculate for the Percentage Error
#av as Actual Value
#e as Error
#percentage_e as Percentage Error
def percentage_sum():
    e_percentage = 0
    av = []
    e = []
    for i in range(per):
        av.append(int(input(f'What is the Actual Value of period {1+i}: ')))
        e.append(int(input(f'What is the Error of period {1+i}: ')))
    
    for a, er in zip(av, e):
        e_percentage += abs(er/a)*100
        e_percentage = round(e_percentage, 2)
    return e_percentage

percentage_e = percentage_sum()

#Calculate the Mean Absolute Percentage Error 
#mape as Mean Absolute Percentage Error
mape = round(percentage_e/per, 2)
print(mape)