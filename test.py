def state_water(temperature):
    if 0 < temperature < 100:
        return 'Liquid'
    elif temperature <= 0:
        return 'Solid'
    else:
        return 'Gas'


current_temperature = int(input('Enter water temperature: '))
state = state_water(current_temperature)
print(state)
