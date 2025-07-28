# CRUD Program - Animal Hospital Patient Data

# ========================
# Part 1: Initial Data & Menu Display
# ========================

patient_data = [
    {'Animal_ID': 'H001', 'Animal_Name': 'Birong', 'Age': 24, 'Animal_Type': 'Cat', 'Gender': 'Female', 'Diagnosis': 'Worms'},
    {'Animal_ID': 'H002', 'Animal_Name': 'Bagong', 'Age': 60, 'Animal_Type': 'Dog', 'Gender': 'Male', 'Diagnosis': 'Sore Throat'},
    {'Animal_ID': 'H003', 'Animal_Name': 'Cemong', 'Age': 12, 'Animal_Type': 'Cat', 'Gender': 'Male', 'Diagnosis': 'Worms'},
    {'Animal_ID': 'H004', 'Animal_Name': 'Dodo', 'Age': 36, 'Animal_Type': 'Cat', 'Gender': 'Male', 'Diagnosis': 'Open Wound'},
    {'Animal_ID': 'H005', 'Animal_Name': 'Euis', 'Age': 18, 'Animal_Type': 'Dog', 'Gender': 'Female', 'Diagnosis': 'Sore Throat'},
    {'Animal_ID': 'H006', 'Animal_Name': 'Fufu', 'Age': 6, 'Animal_Type': 'Rabbit', 'Gender': 'Female', 'Diagnosis': 'Digestive Issues'},
    {'Animal_ID': 'H007', 'Animal_Name': 'Gogo', 'Age': 8, 'Animal_Type': 'Rabbit', 'Gender': 'Male', 'Diagnosis': 'Digestive Issues'},
    {'Animal_ID': 'H008', 'Animal_Name': 'Hera', 'Age': 20, 'Animal_Type': 'Cat', 'Gender': 'Female', 'Diagnosis': 'Worms'},
    {'Animal_ID': 'H009', 'Animal_Name': 'Iro', 'Age': 30, 'Animal_Type': 'Dog', 'Gender': 'Male', 'Diagnosis': 'Itchy Skin'},
    {'Animal_ID': 'H010', 'Animal_Name': 'Juju', 'Age': 16, 'Animal_Type': 'Hamster', 'Gender': 'Female', 'Diagnosis': 'Worms'},
    {'Animal_ID': 'H011', 'Animal_Name': 'Kiko', 'Age': 10, 'Animal_Type': 'Hamster', 'Gender': 'Male', 'Diagnosis': 'Itchy Skin'},
    {'Animal_ID': 'H012', 'Animal_Name': 'Lulu', 'Age': 5, 'Animal_Type': 'Rabbit', 'Gender': 'Female', 'Diagnosis': 'Worms'}
]

def display_menu():
    '''
    Displays the main CRUD menu options.
    Allows the user to easily choose Report, Add, Update, Delete, or Exit features.
    '''
    print('\n============= Animal Hospital Patient Data =============')
    print('1. Report Animal Data')
    print('2. Add Animal Data')
    print('3. Update Animal Data')
    print('4. Delete Animal Data')
    print('5. Exit')

# ========================
# Part 2: Helper Functions
# ========================

def format_age_display(total_months):
    '''
      Converts total months of age into a text format like:
    - 8 months -> '8 months'
    - 24 months -> '2 years'
    - 27 months -> '2 years 3 months'
    '''
    if total_months < 0:
        return 'Invalid age'
    if total_months < 12:
        return f'{total_months} months'
    else:
        years = total_months // 12
        months = total_months % 12
        if months == 0:
            return f'{years} years'
        else:
            return f'{years} years {months} months'

def display_table(data_list):
    '''
    Displays animal data in a table format with dynamic diagnosis column width.
    '''
    if not data_list:
        print('\n**** No Data to Display ****')
        return False
    
    # Calculate the maximum width needed for the diagnosis column
    diagnosis_width = len('Diagnosis') # Minimum width is the header itself
    for animal in data_list:
        if len(animal['Diagnosis']) > diagnosis_width:
            diagnosis_width = len(animal['Diagnosis'])

    # Calculate total table width dynamically
    total_width = 10 + 15 + 15 + 15 + 13 + diagnosis_width + 15 # Additional separator spaces
    
    print('\n' + '=' * total_width)
    # Use the diagnosis_width variable to format the header
    print(f'{"Animal ID":<10} | {"Animal Name":<15} | {"Age":<15} | {"Animal Type":<15} | {"Gender":<13} | {"Diagnosis":<{diagnosis_width}}')
    print('=' * total_width)
    for animal in data_list:
        display_age = format_age_display(animal['Age'])
        # Use the diagnosis_width variable so data and header are aligned
        print(f"{animal['Animal_ID']:<10} | {animal['Animal_Name']:<15} | {display_age:<15} | {animal['Animal_Type']:<15} | {animal['Gender']:<13} | {animal['Diagnosis']:<{diagnosis_width}}")
    print('=' * total_width)
    return True

def find_animal_by_id(id_to_find):
    '''
    Returns the animal dictionary data corresponding to the ID.
    If not found, returns None.
    '''
    for animal in patient_data:
        if animal['Animal_ID'] == id_to_find:
            return animal
    return None

def get_confirmation(message):
    '''
    Asks the user to confirm an action (y/n) with input validation.
    '''
    while True:
        choice = input(f'{message} (y/n): ').lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def input_age():
    '''
      Asks for age input from the user in the format:
    - 'X years Y months'
    - 'X years'
    - 'Y months'
    - or just a number, which is considered as months
    Returns the total age in months (int).
    '''
    while True:
        input_str = input("Enter Age (e.g., '3 years 2 months', '5 years', or '8 months'): ").lower()
        years = 0
        months = 0

        try:
            if 'year' in input_str and 'month' in input_str:
                # Example: '2 years 3 months'
                year_part = input_str.split('year')[0].strip()
                month_part = input_str.split('year')[1].split('month')[0].strip()
                years = int(year_part)
                months = int(month_part)

            elif 'year' in input_str:
                # Example: '4 years'
                year_part = input_str.split('year')[0].strip()
                years = int(year_part)

            elif 'month' in input_str:
                # Example: '7 months'
                month_part = input_str.split('month')[0].strip()
                months = int(month_part)

            else:
                # If input is just a number, assume it's months
                months = int(input_str.strip())
                print(f"(Input '{input_str}' is considered as {months} months)")

            # Validate the final values
            if years < 0:
                print('Year cannot be negative.')
                continue
            if months < 0 or months >= 12:
                print('Month must be between 0 and 11.')
                continue

            return years * 12 + months

        except (ValueError, IndexError):
            print("Invalid Input Format. Correct examples: '2 years 6 months', '4 years', '9 months'")

def input_gender():
    '''
    Displays gender options for valid input (1 or 2).
    Returns the string 'Male' or 'Female'.
    '''
    while True:
        print('Select Gender:')
        print('1. Male')
        print('2. Female')
        choice = input('Enter choice (1/2): ')
        if choice == '1':
            return 'Male'
        elif choice == '2':
            return 'Female'
        else:
            print("Invalid input. Please enter '1' or '2'.")

def input_alpha_text(prompt):
    '''
    A 'specialist' function to request input that only contains letters and spaces.
    '''
    while True:
        text = input(prompt).title()
        # Ensure input is not empty and only contains letters/spaces
        if text.strip() and all(char.isalpha() or char.isspace() for char in text):
            return text
        else:
            print('Invalid Input. Please only enter letters and it cannot be empty.')

def input_diagnosis(prompt):
    '''
    Requests a non-empty diagnosis input,
    only allows letters, numbers, spaces, and the symbols -+/().,
    trims excess spaces without using regex,
    and returns the text in Title Case format.
    '''
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -+/()."

    while True:
        text = input(prompt).strip()
        
        if text == "":
            print("Diagnosis cannot be empty.")
            continue
        # Character validation
        is_invalid_char = False
        for char in text:
            if char not in allowed:
                is_invalid_char = True
                break
        if is_invalid_char:
            print("Diagnosis contains invalid characters.\nOnly letters, numbers, spaces, and symbols -+/(). are allowed.")
        else:
            # Remove double spaces
            clean_text = ' '.join(text.split()) 
            return clean_text.title()

def create_auto_id():
    '''
    Generates a new ID automatically (e.g., H003 after H002).
    Based on the last data in the patient_data list.
    '''
    if not patient_data:
        return 'H001'
    last_id = patient_data[-1]['Animal_ID']
    last_number = int(last_id[1:])
    new_number = last_number + 1
    if new_number < 10:
        number_string = '00' + str(new_number)
    elif new_number < 100:
        number_string = '0' + str(new_number)
    else:
        number_string = str(new_number)
    new_id = f'H{number_string}'
    return new_id

def display_statistics(data_list):
    '''
    Prints statistics from the animal patient list, such as total animals, counts by type,
    gender, average age per type, diagnosis, and most frequent diagnosis.
    '''
    print('\n===== Animal Data Statistics =====')

    # Total number of animals
    total_count = len(data_list)
    print(f"{'Total Animals':<30}: {total_count} animals")

    # Count by Animal Type
    count_by_animal_type = {}
    for animal in data_list:
        animal_type = animal['Animal_Type']
        if animal_type in count_by_animal_type:
            count_by_animal_type[animal_type] += 1
        else:
            count_by_animal_type[animal_type] = 1

    print(f"\n{'Count by Animal Type':<30}")
    for animal_type, count in count_by_animal_type.items():
        print(f"  - {animal_type:<25}: {count} animals")

    # Count by Gender
    count_by_gender = {}
    for animal in data_list:
        gender = animal['Gender']
        if gender in count_by_gender:
            count_by_gender[gender] += 1
        else:
            count_by_gender[gender] = 1

    print(f"\n{'Count by Gender':<30}")
    for gender, count in count_by_gender.items():
        print(f"  - {gender:<25}: {count} animals")

    # Average Age per Animal Type
    age_by_type = {}
    count_per_type = {}
    for animal in data_list:
        animal_type = animal['Animal_Type']
        age = animal['Age']
        if animal_type in age_by_type:
            age_by_type[animal_type] += age
            count_per_type[animal_type] += 1
        else:
            age_by_type[animal_type] = age
            count_per_type[animal_type] = 1

    print(f"\n{'Average Age per Animal Type':<30}")
    for animal_type in age_by_type:
        average = age_by_type[animal_type] / count_per_type[animal_type]
        print(f"  - {animal_type:<25}: {round(average, 1)} months")

    # Count by Diagnosis
    count_by_diagnosis = {}
    for animal in data_list:
        diagnosis = animal['Diagnosis']
        if diagnosis in count_by_diagnosis:
            count_by_diagnosis[diagnosis] += 1
        else:
            count_by_diagnosis[diagnosis] = 1

    print(f"\n{'Count by Diagnosis':<30}")
    for diagnosis, count in count_by_diagnosis.items():
        print(f"  - {diagnosis:<25}: {count} cases")

    # Most Frequent Diagnosis
    if count_by_diagnosis:
        most_frequent_diagnosis = ''
        highest_count = 0
        for diagnosis, count in count_by_diagnosis.items():
            if count > highest_count:
                most_frequent_diagnosis = diagnosis
                highest_count = count

        print(f"\n{'Most Frequent Diagnosis':<30}: {most_frequent_diagnosis} ({highest_count} cases)")

# ========================
# Part 3: Main Menu Functions
# ========================

def menu_view_data():
    '''
    Displays the menu for viewing animal patient data.
    Menu options:
    1. View all data
    2. Search by ID
    3. Search by name
    4. View statistics
    0. Return to main menu
    '''
    while True:
        print('\n+++++++ Report Animal Data +++++++')
        print('1. Report All Data')
        print('2. Report Specific Data (by ID)')
        print('3. Search by Animal Name')
        print('4. Animal Data Statistics')
        print('0. Return to Main Menu')
        choice = input('Please Select Sub Menu [1-4] or [0]: ')

        if choice == '1':
            # Display all data in a table
            display_table(patient_data)
        elif choice == '2':
            # Display data by Animal ID
            if not patient_data:
                print('\n**** No Animal Data ****'); 
                continue
            search_id = input('Enter Animal ID: ').upper()
            animal = find_animal_by_id(search_id)
            if animal:
                print(f'\nData for ID {search_id} found:')
                display_age = format_age_display(animal['Age'])
                print(f"  {'Animal ID':<15}: {animal['Animal_ID']}")
                print(f"  {'Animal Name':<15}: {animal['Animal_Name']}")
                print(f"  {'Age':<15}: {display_age}")
                print(f"  {'Animal Type':<15}: {animal['Animal_Type']}")
                print(f"  {'Gender':<15}: {animal['Gender']}")
                print(f"  {'Diagnosis':<15}: {animal['Diagnosis']}")
            else:
                print(f'\n**** Animal Data with ID {search_id} Not Found ****')
        
        elif choice == '3':
             # Display data by searching for Animal Name
            if not patient_data:
                print('\n**** No Animal Data ****'); 
                continue
            search_name = input('Enter Animal Name to search for: ').lower()
            search_results = []
            for animal in patient_data:
                if search_name in animal['Animal_Name'].lower():
                    search_results.append(animal)
            
            if search_results:
                print(f"\nDisplaying search results for '{search_name}':")
                display_table(search_results)
            else:
                print(f"\n**** No animal found with a name containing '{search_name}' ****")

        elif choice == '4':
            # Display simple statistics
            if not patient_data:
                print('\n**** No Animal Data ****'); 
                continue
            display_statistics(patient_data)

        elif choice == '0':
            break
        else:
            print('\n***** Your choice is incorrect *****')

def menu_add_data():
    '''
    Provides a feature to add new animal patient data.
    The Animal ID will be created automatically.
    The user is asked to fill in name, age, animal type, gender, and diagnosis.
    The program will ask for confirmation before saving.
    '''
    while True:
        print('\n+++++++ Adding Animal Data +++++++')
        print('1. Add New Animal Data')
        print('2. Add Multiple Data at Once')
        print('0. Return to Main Menu')
        choice = input('Please Select Sub Menu [1-2] or [0]: ')

        if choice == '1':
            new_id = create_auto_id()
            print(f'\nA new Animal ID will be automatically created: {new_id}')
            new_animal = {
                'Animal_ID': new_id,
                'Animal_Name': input_alpha_text('Enter Animal Name: '),
                'Age': input_age(),
                'Animal_Type': input_alpha_text('Enter Animal Type: '),
                'Gender': input_gender(),
                'Diagnosis': input_diagnosis('Enter Animal Diagnosis: ')
            }
            if get_confirmation('Do you want to save this data?'):
                patient_data.append(new_animal)
                print('\n>> Animal Data Successfully Saved <<')
            else:
                print('\n>> Data was not saved <<')
        elif choice == '2':
            input_count = input('How much data do you want to add?: ')
            if input_count.isdigit():
                count = int(input_count)
                for i in range(count):
                    print(f'\n>> Data #{i+1}')
                    new_id = create_auto_id()
                    new_animal = {
                        'Animal_ID': new_id,
                        'Animal_Name': input_alpha_text('Enter Animal Name: '),
                        'Age': input_age(),
                        'Animal_Type': input_alpha_text('Enter Animal Type: '),
                        'Gender': input_gender(),
                        'Diagnosis': input_diagnosis('Enter Animal Diagnosis: ')
                    }
                    if get_confirmation('Do you want to save this data?'):
                        patient_data.append(new_animal)
                        print('>> Data Successfully Added <<')
                    else:
                        print('>> Data Was Not Added <<')
                print('\n>> Data Addition Process Finished <<')
            else:
                print('Invalid quantity input. Please enter a valid number.')
        elif choice == '0':
            break
        else:
            print('\n***** Your choice is incorrect *****')

def menu_update_data():
    '''
    Provides a feature to change a column of animal data based on ID
    or in bulk (diagnosis).
    '''
    while True:
        print('\n--------- Updating Animal Data ---------')
        print('1. Update Animal Data')
        print('2. Update Diagnosis in Bulk')
        print('0. Return to Main Menu')
        choice = input('Please Select Sub Menu [1-2] or [0]: ')

        if choice == '1':
            if not display_table(patient_data): continue
            search_id = input('Enter the Animal ID to be updated: ').upper()
            animal = find_animal_by_id(search_id)

            if not animal:
                print(f'\n**** Animal Data with ID {search_id} not found ****')
                continue

            print(f"\nData to be updated: Name: {animal['Animal_Name']}, Diagnosis: {animal['Diagnosis']}")
            if not get_confirmation('Continue updating this data?'):
                print('\n>> Update Canceled <<')
                continue

            # Map user-friendly English input to internal dictionary keys
            column_mapping = {
                'name': 'Animal_Name', 'age': 'Age', 'animal type': 'Animal_Type',
                'gender': 'Gender', 'diagnosis': 'Diagnosis'
            }
            while True:
                column_input = input('Enter the column name to change (Name/Age/Animal Type/Gender/Diagnosis): ').lower()
                if column_input in column_mapping:
                    break
                else:
                    print('\n**** Invalid Column Name. Try Again. ****')
            
            key_to_update = column_mapping[column_input]
            old_value = animal[key_to_update]

            print(f"Old value for '{key_to_update}': {format_age_display(old_value) if key_to_update == 'Age' else old_value}")

            if key_to_update == 'Age':
                new_value = input_age()
            elif key_to_update == 'Gender':
                new_value = input_gender()
            elif key_to_update in ['Animal_Name', 'Animal_Type']:
                new_value = input_alpha_text(f'Enter new {key_to_update.replace("_", " ")}: ')
            else: # For Diagnosis
                new_value = input_diagnosis(f'Enter new {key_to_update}: ')

            display_value = format_age_display(new_value) if key_to_update == 'Age' else new_value
            if get_confirmation(f"Are you sure you want to change {key_to_update} to '{display_value}'?"):
                animal[key_to_update] = new_value
                print('\n>> Data Successfully Updated <<')
                print('Data after update:')
                display_table([animal])
            else:
                print('\n>> Update Was Not Performed <<')

        elif choice == '2':
            if not patient_data: print('\n**** No Animal Data ****'); continue
            
            old_diagnosis = input('Enter the diagnosis to change (case-insensitive): ')
            
            # First, find the matching data
            matching_data = []
            for animal in patient_data:
                if animal['Diagnosis'].lower() == old_diagnosis.lower():
                    matching_data.append(animal)

            if not matching_data:
                print(f'>> No data found with diagnosis "{old_diagnosis}" <<')
                continue

            print(f'\nFound {len(matching_data)} matching records:')
            display_table(matching_data)

            new_diagnosis = input_diagnosis('Change to new diagnosis: ')
            
            if get_confirmation(f'Are you sure you want to change {len(matching_data)} records to "{new_diagnosis}"?'):
                count_updated = 0
                for animal in patient_data:
                    if animal['Diagnosis'].lower() == old_diagnosis.lower():
                        animal['Diagnosis'] = new_diagnosis
                        count_updated += 1
                print(f'>> {count_updated} records successfully updated <<')
            else:
                print('>> Change canceled <<')

        elif choice == '0':
            break
        else:
            print('\n***** Your choice is incorrect *****')

def menu_delete_data():
    '''
    Provides a feature to delete animal data by ID.
    The program will ask for confirmation before the data is actually deleted.
    '''
    while True:
        print('\n--------- Deleting Animal Data ---------')
        print('1. Delete Animal Data')
        print('2. Delete All Data (Reset)')
        print('0. Return to Main Menu')
        choice = input('Please Select Sub Menu [1-2] or [0]: ')

        if choice == '1':
            if not display_table(patient_data): continue
            id_to_delete = input('Enter the Animal ID to be Deleted: ').upper()
            animal = find_animal_by_id(id_to_delete)

            if not animal:
                print(f'\n**** Animal Data with ID {id_to_delete} Not Found ****')
                continue

            if get_confirmation(f"Are you sure you want to delete data for {animal['Animal_Name']} (ID: {animal['Animal_ID']})?"):
                patient_data.remove(animal)
                print('\n>> Data Successfully Deleted <<')
            else:
                print('\n>> Data Was Not Deleted <<')
        elif choice == '2':
            if get_confirmation('Are you sure you want to delete all data?'):
                patient_data.clear()
                print('>> All data successfully deleted <<')
        elif choice == '0':
            break
        else:
            print('\n***** Your choice is incorrect *****')

# ========================
# Part 4: Main Program
# ========================

def main():
    '''
    The main function that is the 'heart' of the program.
    Displays the menu and handles the main flow.
    Will keep running until the user chooses to exit.
    '''
    while True:
        display_menu()
        choice = input('Please Select Main Menu [1-5]: ')

        if choice == '1':
            menu_view_data()
        elif choice == '2':
            menu_add_data()
        elif choice == '3':
            menu_update_data()
        elif choice == '4':
            menu_delete_data()
        elif choice == '5':
            print('\nThank You for Using the ANABUL Program!!!')
            break
        else:
            print('\n***** Your choice is incorrect *************')

# This line is the standard 'entry point' for a Python program.
# It means: 'Only run the main() function if this file is executed directly'.
if __name__ == '__main__':
    main()