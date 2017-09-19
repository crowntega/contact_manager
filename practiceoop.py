# class Contact_Manager:
# 	def __init__(self, name='', number='', age='',address='', gender='', email='', contacts=[]):
# 		self.name = name
# 		self.number = number
# 		self.address = address
# 		self.gender = gender 
# 		self.email = email
# 		self.age = age
# 		self.contacts = contacts

# 		answer = int(input('Welcome, to add contact Press 1 to search contact Press 2: '))

# 		if answer == 1:
# 			self.add_user()

# 	def add_user(self):
# 		self.name = input('Enter your name: ')
# 		self.age = input('Enter your age: ')
# 		self.number = input('Enter your number: ')
# 		self.address = input('Your address: ')
# 		self.gender =  input('Male or Female?: ')
# 		self.email =  input('Your email here: ')

# 		print('Contacts Saved Successfully', self.contacts)


# First Class takes the ContactBox
# Second Class dd contacts

class ContactBox:
	def __init__(self, contacts=[]):
		self.contacts = contacts

	def add_contact(self, contact):
		print('Contact Saved Successfully')
		return self.contacts.append(contact)

class Contacts:
	def __init__(self, name='', age='', number='', email='', gender=''):
		self.name = input('Enter name: ')
		self.age = input('Enter age: ')
		self.number = input('Enter number: ')
		self.email = input('Enter email: ')
		self.gender = input('Enter gender (m/f): ')


def main():

	while True:
		ans = int(input('Please enter 1 to add contact or 2 to get contact: '))

		if ans == 1:
			contact = Contacts()

			new_contact = ContactBox()

			new_contact.add_contact(contact)
		
		elif ans == 2:
			name =  input('Enter name to search: ')

			new_contact = ContactBox()

			for contact in new_contact.contacts:
				if contact.name == name:
					print(contact.name, contact.email, contact.age, contact.number, contact.gender)



main()
