room_temperature_c = 20;
cooking_temperature_f = 350;
oven_heating_rate_c = 20;
oven_heating_time = (
    ((cooking_temperature_f - 32) * 5 / 9)
    - room_temperature_c)/ \
    oven_heating_rate_c
print(oven_heating_time)
# note the open parentheses and \ characters allow continuation
# also note the indentation
# could this be simpler? yes!!!
room_temperature_c = 20;
cooking_temperature_f = 350;
cooking_temperature_c = (cooking_temperature_f - 32)\
                        * 5 / 9
oven_heating_rate_c = 20
oven_heating_time = (cooking_temperature_c - room_temperature_c)/ \
                     oven_heating_rate_c
print(oven_heating_time)
# This is much clearer!
