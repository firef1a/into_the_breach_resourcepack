import json 
import math
import os

# this is for up shifting the first person model data to be higher so you can set the player's attack speed to 0 to remove item swap animations 
# er if u want to use this for ur own rp go ahead idk why u would want to use this shitty script tho..

def upshift(directory):
	working_directory = directory + "/base"
	 
	for filename in os.listdir(working_directory):
		path = os.path.join(working_directory, filename)

		print ("  " + path)
		with open(os.path.join(working_directory,filename), 'r') as load_file:
			data = json.load(load_file)

			display = data['display']

			if display.get('firstperson_righthand'):
				righthand = display['firstperson_righthand']
			else:
				righthand = {'rotation': [0,0,0], 'translation': [0,0,0], 'scale': [1,1,1]}


			if display.get('firstperson_lefthand'):
				lefthand = display['firstperson_lefthand']
			else:
				lefthand = {'rotation': [0,0,0], 'translation': [0,0,0], 'scale': [1,1,1]}


			if not righthand.get('translation'):	righthand['translation'] = [0,0,0]
			if not lefthand.get('translation'):	lefthand['translation'] = [0,0,0]
			righthand['translation'] = [righthand['translation'][0],righthand['translation'][1]+9.75,righthand['translation'][2]]
			lefthand['translation'] = [lefthand['translation'][0],lefthand['translation'][1]+9.75,lefthand['translation'][2]]

			display['firstperson_righthand'] = righthand
			display['firstperson_lefthand'] = lefthand

			data['display'] = display

			with open(os.path.join(directory,filename), 'w+') as write_file:
				json.dump(data, write_file, indent=4)

upshift_list = [
	'assets/minecraft/models/item/weapons/special/microhid',
	'assets/minecraft/models/item/weapons/special/phase_blade',
	'assets/minecraft/models/item/weapons/special/plasma_rifle',

	'assets/minecraft/models/item/weapons/kriss_vector',
	'assets/minecraft/models/item/weapons/lmg',
	'assets/minecraft/models/item/weapons/p90',
	'assets/minecraft/models/item/weapons/awp',
	'assets/minecraft/models/item/weapons/ak',
	'assets/minecraft/models/item/weapons/revolver',
	'assets/minecraft/models/item/weapons/dbsg',
	'assets/minecraft/models/item/weapons/pistol',
	'assets/minecraft/models/item/weapons/cooler_pistol',
	'assets/minecraft/models/item/weapons/frmg',
	'assets/minecraft/models/item/weapons/epsilon11',
	'assets/minecraft/models/item/weapons/glockinator',

	'assets/minecraft/models/item/use/radio',
	'assets/minecraft/models/item/use/adrenaline',
	'assets/minecraft/models/item/use/painkillers',
	'assets/minecraft/models/item/use/grenade',
	'assets/minecraft/models/item/use/stun_grenade'
]

for folder in upshift_list:
	print ("ASSET: " + folder)
	upshift(folder)

