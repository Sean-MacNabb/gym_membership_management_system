from members import create_member, get_member, update_member, delete_member, list_members
from memberships import create_membership, get_membership, update_membership, delete_membership, list_memberships

# Helper function for making sure inputs are valid ints, returns an int or None
def valid_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

# Helper function, empty strings are returned as None
def valid_str_input(prompt):
    string = input(prompt).strip()
    if string == '':
        return None
    else:
        return string

# Member flow methods for members table
def create_member_flow():
    print('Create New Member')
    print('Prompts with a * mean it cannot be blank.')
    first = input('Enter first name: *')
    last = input('Enter last name: *')
    phone = input('Enter phone number: *')
    membership = valid_int_input('Enter membership number: *')
    address = valid_str_input('Enter address: ')
    email = valid_str_input('Enter email address: ')
    dob = valid_str_input('Enter date of birth \'YYYY-MM-DD\': ')

    result = create_member(first, last, phone, membership, address, email, dob)
    print(result)

def get_member_flow():
    print('Get Member')
    phone = input('Enter the phone number for member you want to view: ')

    result = get_member(phone)
    print(result)

def update_member_flow():
    print('Update Member')
    current_phone = input('Enter the phone number of the member you want to update: ')
    phone = valid_str_input('Change phone number: ')
    first = valid_str_input('Change first name: ')
    last = valid_str_input('Change last name: ')
    address = valid_str_input('Change address: ')
    email = valid_str_input('Change email: ')
    status = valid_str_input('Change status: ')
    membership = valid_int_input('Change membership: ')
    dob = valid_str_input('Change date of birth \'YYYY-MM-DD\': ')

    result = update_member(current_phone, phone, first, last, address, email, status, membership, dob)
    print(result)

def delete_member_flow():
    print('Delete Member')
    phone = input('Enter the phone number of the member you want to delete: ')

    member = get_member(phone)
    print(member)

    confirm = input('Are you sure you want to delete this member? Y/N').strip().lower()

    if confirm == 'y':
        result = delete_member(phone)
        print(result)
    else:
        pass

def list_members_flow():
    print('All Members')

    result = list_members()
    print (result)

# Membership flow methods for memeberships table
def create_membership_flow():
    print('Create New Membership')
    print('Prompts with a * mean it cannot be blank.')
    plan = input('Enter plan name: *')
    sign_up_fee = input('Sign up fee cost: *')
    price = input('Membership price: *')
    duration_months = input('Length of membership (months): *')
    status = input('Status of membership: *')
    description = valid_str_input('Membership description: ')

    result = create_membership(plan, sign_up_fee, price, duration_months, status, description)
    print(result)

def get_membership_flow():
    print('Get Membership')
    plan = input('Which membership plan do you want to see: ')

    result = get_membership(plan)
    print(result)

def update_membership_flow():
    print('Update Membership')
    current_plan = input('Enter the membership plan you want to update: ')
    plan = valid_str_input('Change plan name: ')
    sign_up_fee = valid_int_input('Change sign up fee: ')
    price = valid_int_input('Change price: ')
    duration_months = valid_int_input('Change month duration: ')
    status = valid_str_input('Change status: ')
    description = valid_str_input('Change description: ')

    result = update_membership(current_plan, plan, sign_up_fee, price, duration_months, status, description)
    print(result)

def delete_membership_flow():
    print('Delete Membership')
    plan = input('Enter the membership plan you want to delete: ')

    membership = get_membership(plan)
    print(membership)

    confirm = input('Are you sure you want to delete this membership? Y/N').strip().lower()
    if confirm == 'y':
        result = delete_membership(plan)
        print(result)
    else:
        pass

def list_memberships_flow():
    print('All Memberships')

    result = list_memberships()
    print(result)

# Main program logic
def main():
    while True:
        print('Gym Management System')
        print('1. Member options')
        print('2. Membership options')
        print('3. Exit')

        selection = valid_int_input('Select an option: ')

        if selection == 1:
            print('Member Options:')
            print('1. Create member')
            print('2. Get member')
            print('3. Update member')
            print('4. Delete member')
            print('5. List members')
            print('6. Exit')

            member_selection = valid_int_input('Select a member option: ')

            if member_selection == 1:
                create_member_flow()
            elif member_selection == 2:
                get_member_flow()
            elif member_selection == 3:
                update_member_flow()
            elif member_selection == 4:
                delete_member_flow()
            elif member_selection == 5:
                list_members_flow()
            else:
                break            

        elif selection == 2:
            print('Membership Options')
            print('1. Create membership')
            print('2. Get membership')
            print('3. Update membership')
            print('4. Delete membership')
            print('5. List memberships')
            print('6. Exit')

            membership_selection = valid_int_input('Select a membership option: ')

            if membership_selection == 1:
                create_membership_flow()
            elif membership_selection == 2:
                get_membership_flow()
            elif membership_selection == 3:
                update_membership_flow()
            elif membership_selection == 4:
                delete_membership_flow()
            elif membership_selection == 5:
                list_memberships_flow()
            else:
                break     

        else:
            break

if __name__ == "__main__":
    main()