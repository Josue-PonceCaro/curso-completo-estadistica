import pandas as pd
location = '1. Estadistica descriptiva/5.+Ejercicio+-+pesos+de+80+personas.xlsx'
fl = pd.read_excel(location)
val = list(fl.columns)
val2 = fl.values
for i in val2:
    val.append(i[0])
val.sort()

init = val[0]-val[0]%5
end = val[-1]+5-val[-1]%5

print(init)
print(end)

count = []
for i in range(init,end,5):
    count.append(0)
    for y in range(i,i+5):
        count[-1] += sum([1 for yy in val if y == yy])
print(val)
print(count)