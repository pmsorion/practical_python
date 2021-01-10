import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@gmail.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Platzi',
        'email': 'ricardo@platzi.com',
        'position': 'Academic Coach',
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company=client['company'],
            email= client['email'],
            position = client['position']
        ))


def update_client(client_id, updated_client_name):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client_name
    else:
        _print_message_client()

    # if client_name in clients:
    #     index = clients.index(client_name)
    #     clients[index] = updated_client_name
    # else:
    #     _print_message_client()


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def seach_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _get_client_field(field_name, message='What is the client {}? '):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _print_welcome():
    print('=' * 40)
    print('Welcome to Platzi ventas')
    print('=' * 40)
    print('What would you like to do today')
    print('-' * 40)
    print('[C]reate client')
    print('[L]ist   client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('*' * 40)


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_message_client():
    print('Client is not in clients list')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }

        create_client(client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))

        updated_client_name = _get_client_from_user()
        update_client(client_id, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = seach_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        a = 1
        b = 2
        print(a)
        print(b)
        #a, b = b, a + b
        a = b
        b = a + b
        print(a)
        print(b)
        print('Invalid command')