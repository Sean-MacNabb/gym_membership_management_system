from db import get_connection

# Create a new membership
def create_membership(
        plan: str,
        sign_up_fee: float,
        price: float,
        duration_months: int,
        status: str,
        description: str | None = None
    ):
    
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        INSERT INTO memberships(
            plan,
            sign_up_fee,
            price,
            duration_months,
            status,
            description
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''

    cursor.execute(query, (plan, sign_up_fee, price, duration_months, status, description))
    connection.commit()

    new_membership_id = cursor.lastrowid

    cursor.close()
    connection.close()

    if new_membership_id == 0:
        return 'Membership was not added.'
    else:
        return f'Membership was added with id: {new_membership_id}.'

# Get membership information given plan name, returns dictionary
def get_membership(plan: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        SELECT *
        FROM memberships
        WHERE plan = %s
    '''

    cursor.execute(query, (plan,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

# Update a membership given plan name
def update_membership(
        current_plan: str,
        plan: str | None = None,
        sign_up_fee: float | None = None,
        price: float | None = None,
        duration_months: int | None = None,
        status: str | None = None,
        description: str | None = None
    ):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    fields_to_update = []
    update_values = []

    if plan is not None:
        fields_to_update.append('plan = %s')
        update_values.append(plan)

    if sign_up_fee is not None:
        fields_to_update.append('sign_up_fee = %s')
        update_values.append(sign_up_fee)

    if price is not None:
        fields_to_update.append('price = %s')
        update_values.append(price)

    if duration_months is not None:
        fields_to_update.append('duration_months = %s')
        update_values.append(duration_months)

    if status is not None:
        fields_to_update.append('status = %s')
        update_values.append(status)

    if description is not None:
        fields_to_update.append('description = %s')
        update_values.append(description)

    if not fields_to_update:
        cursor.close()
        connection.close()
        return 'No memberships were updated.'

    query = f'''
        UPDATE memberships
        SET {', '.join(fields_to_update)}
        WHERE plan = %s
    '''

    update_values.append(current_plan)

    cursor.execute(query, update_values)
    connection.commit()

    update_count = cursor.rowcount

    cursor.close()
    connection.close()

    if update_count == 0:
        return 'No memberships were updated.'
    elif update_count == 1:
        return f'{update_count} membership was updated.'
    else:
        return f'{update_count} memberships were updated.'

# Delete a memberships given a plan
def delete_membership(plan: str):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        DELETE FROM memberships
        WHERE plan = %s
    '''

    cursor.execute(query, (plan,))
    connection.commit()

    rows_deleted = cursor.rowcount

    cursor.close()
    connection.close()

    if rows_deleted == 0:
        return 'No memberships were deleted.'
    elif rows_deleted == 1:
        return f'{rows_deleted} membership was deleted.'
    else:
        return f'{rows_deleted} memberships were deleted.'

# List all memberships and their information
def list_memberships():
    
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        SELECT *
        FROM memberships
        ORDER BY membership_id ASC
    '''

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result
