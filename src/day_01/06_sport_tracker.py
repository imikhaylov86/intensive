ccal = 5000
step = 340
step_count = 0

while ccal > 3600:
    ccal = ccal - step
    step_count = step_count + 1
    print(f'Шаг {step_count}, каллории {ccal}')
#print('Цель достигнута! Тренировка окончена.')
else:
    print(f'Шагов сделано: {step_count}')