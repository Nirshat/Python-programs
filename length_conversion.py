import colorama
from colorama import Fore, Style
colorama.init(autoreset= True)


# LENGTH CONVERSION


# Formula:  
# smaller length ÷ higher length
# higher length × smaller length
# Note: If you are converting a length with higher length ( length1 ÷ length2 )


# Meter/s
# Foot/Feet
# Inch/es
# Centimeter/s
# Millimeter/s

print('''________________________________
				|
   LENGTH CONVERSION		|
 1 meter = 3.28 Feet		|
 1 meter = 39.37 Inches		|
 1 meter = 100 Centimeters	|
 1 meter = 1,000 Millimeters	|
 1 Foot = 12 Inches		|
 1 Foot = 30.48 Centimeters     |
 1 Foot = 304.8 Millimeters     |
 1 Inch = 2.54 Centimeters	|
 1 Inch = 25.4 Millimeters      |
 1 cm = 10 Millimeters		|
________________________________|''')

con = ""
while con == "":
	print('\n Length Keyword Options: [ m | ft | in | cm | mm ] ')
	
	# this function is when you're converting any type of length that is probably lower/smaller than meter/s.
	def finding_highest_meter (x,y):
		higher = x / y
		if higher > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' meters')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' meter')
	#----------------------------------------------- 
	def finding_lower_feet (x,y): # higher length convert to foot / foot convert to lower length
		lower = x * y
		# proper statement (singular/plural)
		if lower > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' feet')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' foot')
			
	def finding_higher_feet (x,y): # foot convert to higher length
		higher = x / y
		if higher > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' feet')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' foot')
#-----------------------------------------------		
	def finding_lower_inch (x,y):
		lower = x * y
		if lower > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' inches')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' inch')

	def finding_higher_inch (x,y):
		higher = x / y
		if higher > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' inches')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' inch')
#-----------------------------------------------
	def finding_lower_cm (x,y):
		lower = x * y
		if lower > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' centimeters')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' centimeter')

	def finding_higher_cm (x,y):
		higher = x / y
		if higher > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' centimeters')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' centimeter')
#-----------------------------------------------
	def finding_lower_mm (x,y):
		lower = x * y
		if lower > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' millimeters')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(lower)+' mill1imeter')

	def finding_higher_mm (x,y):
		higher = x / y
		if higher > 1:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' millimeters')
		else:
			print(Fore.GREEN+' TOTAL LENGTH: '+str(higher)+' millimeter')




 # Proper statement of singular and plural for length
	def display_meter ():
		if lth >= 0 and lth <= 1:
			print(Fore.GREEN+' '+str(lth)+' meter')
		else:
			print(Fore.GREEN+' '+str(lth)+' meters')
 	
	def display_feet ():
		if lth >= 0 and lth <= 1:
			print(Fore.GREEN+' '+str(lth)+' foot')
		else:
			print(Fore.GREEN+' '+str(lth)+' feet')
 	
	def display_inch ():
		if lth >= 0 and lth <= 1:
			print(Fore.GREEN+' '+str(lth)+' inch')
		else:
			print(Fore.GREEN+' '+str(lth)+' inches')
			
	def display_cm ():
		if lth >= 0 and lth <= 1:
			print(Fore.GREEN+' '+str(lth)+' centimeter')
		else:
			print(Fore.GREEN+' '+str(lth)+' centimeters')
 	
	def display_mm ():
		if lth >= 0 and lth <= 1:
			print(Fore.GREEN+' '+str(lth)+' millimeter')
		else:
			print(Fore.GREEN+' '+str(lth)+' millimeters')
			
			
			
 
 
	# Keyword List
	meter_option = ['m','M','meter','Meter','METER']
	ft_option = ['ft','Ft','FT','feet','Feet','FEET','foot','Foot','FOOT']
	inch_option = ['in','In','IN','inch','Inch','INCH','inches','Inches','INCHES']
	cm_option = ['cm','Cm','CM','centimeter','Centimeter','CENTIMETER']
	mm_option = ['mm','Mm','MM','millemeter','Millimeter','MILLIMETER']
 

	len = input(' Insert Length: ')

	
	# METER
	if len in meter_option:
		lth = float(input(' Length Value: '))
		if lth >= 0:
			display_meter()
			convert = input(' Convert to: ')
			if convert in ft_option:
				finding_lower_feet(3.28,lth)
				# meter to ft || 1 meter is equivalent to 3.28 feet
				# 3.28 × meter value
			elif convert in inch_option:
				finding_lower_inch(39.37,lth)
				# meter to inch || 1 meter is equivalent to 39.37 inches
				# 39.37 × meter value
			elif convert in cm_option:
				finding_lower_cm(100,lth)
				# meter to cm || 1 meter is equivalent to 100 centimeters
				# 100 × meter value
			elif convert in mm_option:
				finding_lower_mm(1000,lth)
				# meter to mm || 1 meter is equivalent to 1000 millimeters
				# 1000 × meter value
			elif convert in meter_option:
				# if meter to meter...
				print(Fore.RED+' System denied...\n Invalid conversion for same length')
			else:
				print(Fore.RED+' You have input a invalid keyword')
			#	print(' ------------------------------------')
		else:
			print(Fore.RED+' Invalid input for negative length')
		

	# FEET
	elif len in ft_option:
		lth = float(input(' Length Value: '))
		if lth >= 0:
			display_feet()
			convert = input(' Convert to: ')
			if convert in meter_option:
				finding_highest_meter(lth,3.28)
				# foot/feet to meter ||  3.28 feet is equivalent to 1 meter
				# foot/feet divided by 3.28
			elif convert in inch_option:
				finding_lower_inch(12,lth)
				# foot/feet to inch/es ||  1 foot is equivalent to 12 inches
				# foot/feet × inch/es value
			elif convert in cm_option :
				finding_lower_cm(30.48,lth)
				# foot/feet to cm ||  1 foot is equivalent to 30.48 inches
				# foot/feet × inch/es value
			elif convert in mm_option:
				finding_lower_mm(304.8,lth)
				# foot/feet to mm ||  1 foot is equivalent to 304.8 inches
				# foot/feet × inch/es value
			elif convert in ft_option:
				# if feet/foot to feet/foot...
				print(Fore.RED+' System denied...\n Invalid conversion for same length')
			else:
				print(Fore.RED+' You have input a invalid keyword')
			#	print(' ------------------------------------')
		else:
			print(Fore.RED+' Invalid for negative length')
		
		
	# INCH
	elif len in inch_option:
		lth = float(input(' Length Value: '))
		if lth >= 0:
			display_inch()
			convert = input(' Convert to: ')
			if convert in meter_option:
				finding_highest_meter(lth,39.37)
				# inch/es to meter ||  39.37 inch/es is equivalent to 1 meter
				# inch/es value divided by 39.37
			elif convert in ft_option:
				finding_higher_feet(lth,12.0)
				# inch/es to ft ||  12.0 inches is equivalent to 1 foot
				# inch/es value divided by 12.0
			elif convert in cm_option:
				finding_lower_cm(2.54,lth)
				# inch/es to cm ||  2.54 cm is equivalent to 1 inch
				# 2.54 × inch/es value 
			elif convert in mm_option:
				finding_lower_mm(25.4,lth)
				# inch/es to mm ||  25.54 mm is equivalent to 1 inch
				# 25.4 × inch/es value
			elif convert in inch_option:
				# if inch/es to inch/es...
				print(Fore.RED+' System denied...\n Invalid conversion for same length')
			else:
				print(Fore.RED+' You have input a invalid keyword')
			#	print(' ------------------------------------')
		else:
			print(Fore.RED+' Invalid for negative length')
		
	
	# CENTIMETER
	elif len in cm_option:
		lth = float(input(' Length Value: '))
		if lth >= 0:
			display_cm()
			convert = input(' Convert to: ')
			if convert in meter_option:
				finding_highest_meter(lth,100)
				# cm to meter ||  100 cm is equivalent to 1 meter
				# cm value divided by 100
			elif convert in ft_option:
				finding_higher_feet(lth,30.48)
				# cm to ft ||  30.48 cm is equivalent to 1 foot
				# cm value divided by 30.48
			elif convert in inch_option:
				finding_higher_inch(lth,2.54)
				# cm to inch ||  2.54 cm is equivalent to 1 inch
				# cm value divided by 2.54
			elif convert in mm_option:
				finding_lower_mm(10,lth)
				# cm to mm ||  10 mm is equivalent to 1 cm
				# 10 × cm value
			elif convert in cm_option:
				# if cm to cm...
				print(Fore.RED+' System denied...\n Invalid conversion for same length')
			else:
				print(Fore.RED+' You have input a invalid keyword')
		#		print(' ------------------------------------')
		else:
			print(Fore.RED+' Invalid for negative length')
					
		
	# MILLIMETER
	elif len in mm_option:
		lth = float(input(' Length Value: '))
		if lth >= 0:
			display_mm()
			convert = input(' Convert to: ')
			if convert in meter_option:
				finding_highest_meter(lth,1000)
				# mm to meter ||  1000 mm is equivalent to 1 meter
				# mm value divided by 1000
			elif convert in ft_option:
				finding_higher_feet(lth,304.8)
				# mm to ft ||  304.8 mm is equivalent to 1 foot
				# mm value divided by 304.8
			elif convert in inch_option:
				finding_higher_inch(lth,25.4)
				# mm to inch/es ||  25.4 mm is equivalent to 1 inch
				# mm value divided by 25.4
			elif convert in cm_option:
				finding_higher_cm(lth,10)
				# mm to cm ||   10 mm is equivalent to 1 cm
				# mm value divided by 10
			elif convert in mm_option:
				# if mm to mm...
				print(Fore.RED+' System denied...\n Invalid conversion for same length')
			else:
				print(Fore.RED+' You have input a invalid keyword')
			#	print(' ------------------------------------')
		else:
			print(Fore.RED+' Invalid for negative length')
				
				
	else:
		print(Fore.RED+' You have input a invalid keyword')

		
	print(' Enter to continue...or')
	con = input(' Type any key to close: ')
	print(' ------------------------------------')
	if con != "":
		print('\n - Program Ended - \n')
		break






	# Note: if your IDE has not colorama module installed...
	# 👇️ for python 3 (could also be pip3.10 depending on your version)
  # type 'pip3 install colorama' in your terminal




	# Program Written by: Aron Paul Gonzales