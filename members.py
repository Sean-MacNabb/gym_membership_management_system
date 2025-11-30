from db import get_connection

# Creates a new member
def create_member(
    first_name: str,
    last_name: str,
    phone_number: str,
    membership_id: int,
    address: str | None = None,
    email: str | None = None,
    date_of_birth: str | None = None,
):
    
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        INSERT INTO members (
            first_name,
            last_name,
            phone_number,
            membership_id,
            address,
            email,
            date_of_birth
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    
    cursor.execute(query, (first_name, last_name, phone_number, membership_id, address, email, date_of_birth))
    connection.commit()

    new_member_id = cursor.lastrowid

    cursor.close()
    connection.close()

    if new_member_id == 0:
        return f'New member was not added.'
    else:
        return f'New member was added with id: {new_member_id}'
    
#Looks up member by phone_number, returns a dictionary or None if no member is found
def get_member(phone_number: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        SELECT
            m.member_id,
            m.first_name,
            m.last_name,
            m.email,
            m.address,
            m.phone_number,
            m.date_of_birth,
            m.date_joined,
            m.status,
            ms.plan,
            ms.price
        FROM members m
        JOIN memberships ms
            ON m.membership_id = ms.membership_id
        WHERE m.phone_number = %s
    '''

    cursor.execute(query, (phone_number,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

# Updates member based on phone number
def update_member(
        current_phone_number: str,
        phone_number: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        address: str | None = None,
        email: str | None = None,
        status: str | None = None,
        membership_id: int | None = None,
        date_of_birth: str | None = None,    
    ):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    fields_to_update = []
    update_values = []

    if phone_number is not None:
        fields_to_update.append('phone_number = %s')
        update_values.append(phone_number)

    if first_name is not None:
        fields_to_update.append('first_name = %s')
        update_values.append(first_name)

    if last_name is not None:
        fields_to_update.append('last_name = %s')
        update_values.append(last_name)

    if address is not None:
        fields_to_update.append('address = %s')
        update_values.append(address)

    if email is not None:
        fields_to_update.append('email = %s')
        update_values.append(email)

    if status is not None:
        fields_to_update.append('status = %s')
        update_values.append(status)

    if membership_id is not None:
        fields_to_update.append('membership_id = %s')
        update_values.append(membership_id)

    if date_of_birth is not None:
        fields_to_update.append('date_of_birth = %s')
        update_values.append(date_of_birth)

    if not fields_to_update:
        cursor.close()
        connection.close()
        return 'No fields were updated.'
        
    query = f'''
        UPDATE members
        SET {', '.join(fields_to_update)}
        WHERE phone_number = %s
    '''
    
    update_values.append(current_phone_number)

    cursor.execute(query, update_values)
    connection.commit()

    update_count = cursor.rowcount

    cursor.close()
    connection.close()

    if update_count == 0:
        return 'No members were updated.'
    elif update_count == 1:
        return f'{update_count} member was updated.'
    else:
        return f'{update_count} members were updated.'

# Deletes member based on phone number
def delete_member(phone_number:str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        DELETE FROM members
        WHERE phone_number = %s    
    '''

    cursor.execute(query, (phone_number,))
    connection.commit()

    rows_deleted = cursor.rowcount

    cursor.close()
    connection.close()

    if rows_deleted == 0:
        return f'No member found with that phone number.'
    elif rows_deleted == 1:
        return f'{rows_deleted} member was deleted.'
    else:
        return f'{rows_deleted} members were deleted.' 

# Returns all pertinent information on members in a dictionary
def list_members():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        SELECT
            m.member_id,
            m.first_name,
            m.last_name,
            m.email,
            m.address,
            m.phone_number,
            m.date_of_birth,
            m.date_joined,
            m.status,
            ms.plan,
            ms.price
        FROM members m
        JOIN memberships ms
            ON m.membership_id = ms.membership_id
    '''

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result
