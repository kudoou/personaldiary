from datetime import datetime

first_name ='randy'
last_name = 'ardiansyah'
full_name = f'{first_name} {last_name}'
print(full_name)

today = datetime.now()

date_time = today.strftime('%Y-%M-%d-%H-%M-%S')

print(date_time)