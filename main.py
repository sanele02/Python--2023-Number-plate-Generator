import random
import string

print("Welcome to the South African 2023 new number plate generator! ")
print('')

provinces = ["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape", "Mpumalanga", "Limpopo", "North West", "Free State", "Northern Cape","CapeTown"]

print(provinces)

province_input = input("what provence are you from :")

# Checking if the user's input matches any province in the list
if province_input in provinces:
    chosen_province = province_input  # Capitalize input for consistency
    #print(f"You chose to promote" +chosen_province +".")
else:
    print("Wrong province. Please enter a valid province name.")
    quit()

#randomlly generate number plate numbers

random_plateset1 = random.randint(1, 100)


alphabet = string.ascii_uppercase

# Choosing two random letters
random_letters = random.choices(alphabet, k=2)

# Joining the two random letters into a string
random_letters_str = ''.join(random_letters)

random_plateset2 = random.randint(1, 100)

#the province abriviation
# Dictionary to store province abbreviations
province_abbreviations = {
    'Gauteng': 'GP',
    'Western Cape': 'WC',
    'KwaZulu-Natal': 'KZN',
    'Eastern Cape': 'EC',
    'Mpumalanga': 'MP',
    'Limpopo': 'LP',
    'North West': 'NW',
    'Free State': 'FS',
    'Northern Cape': 'NC',
    'CapeTown': 'CT'
}

# Simulating user input
chosen_province = province_input  # Replace this with actual user input

# Checking if the chosen province exists in the dictionary
if chosen_province in province_abbreviations:
    abbreviation = province_abbreviations[chosen_province]
    #print(f"The abbreviation for {chosen_province} is {abbreviation}.")


print('NUMBER PLATE : '+ ' '+str(random_plateset1)+' ' + random_letters_str +' '+ str(random_plateset2) + ' '+abbreviation)
print('')
print('Congratulations your new number plate has been successfully registered!  ')