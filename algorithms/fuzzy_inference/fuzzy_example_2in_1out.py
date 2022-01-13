from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_system.fuzzy_variable import FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem

temp = FuzzyInputVariable('Temperature', 10, 40, 100)
temp.add_triangular('Cold', 10, 10, 25)
temp.add_triangular('Medium', 15, 25, 35)
temp.add_triangular('Hot', 25, 40, 40)

humidity = FuzzyInputVariable('Humidity', 20, 100, 100)
humidity.add_triangular('Wet', 20, 20, 60)
humidity.add_trapezoidal('Normal', 30, 50, 70, 90)
humidity.add_triangular('Dry', 60, 100, 100)

motor_speed = FuzzyOutputVariable('Speed', 0, 100, 100)
motor_speed.add_triangular('Slow', 0, 0, 50)
motor_speed.add_triangular('Moderate', 10, 50, 90)
motor_speed.add_triangular('Fast', 50, 100, 100)

system = FuzzySystem()
system.add_input_variable(temp)
system.add_input_variable(humidity)
system.add_output_variable(motor_speed)

system.add_rule(
		{ 'Temperature':'Cold',
			'Humidity':'Wet' },
		{ 'Speed':'Slow'})

system.add_rule(
		{ 'Temperature':'Cold',
			'Humidity':'Normal' },
		{ 'Speed':'Slow'})

system.add_rule(
		{ 'Temperature':'Medium',
			'Humidity':'Wet' },
		{ 'Speed':'Slow'})

system.add_rule(
		{ 'Temperature':'Medium',
			'Humidity':'Normal' },
		{ 'Speed':'Moderate'})

system.add_rule(
		{ 'Temperature':'Cold',
			'Humidity':'Dry' },
		{ 'Speed':'Moderate'})

system.add_rule(
		{ 'Temperature':'Hot',
			'Humidity':'Wet' },
		{ 'Speed':'Moderate'})

system.add_rule(
		{ 'Temperature':'Hot',
			'Humidity':'Normal' },
		{ 'Speed':'Fast'})

system.add_rule(
		{ 'Temperature':'Hot',
			'Humidity':'Dry' },
		{ 'Speed':'Fast'})

system.add_rule(
		{ 'Temperature':'Medium',
			'Humidity':'Dry' },
		{ 'Speed':'Fast'})

output = system.evaluate_output({
				'Temperature':18,
				'Humidity':60
		})

print(output)
# print('fuzzification\n-------------\n', info['fuzzification'])
# print('rules\n-----\n', info['rules'])

system.plot_system()