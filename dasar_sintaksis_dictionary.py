users ={
    'id' : 1,
    'name' : 'leanne graham',
    'username' : 'bret',
    'email' : 'sincere@april.biz',
    'address' :{
        'street' : 'kulas light',
        'suite' : 'Apt.556',
        'city' : 'gwenborough',
        'zipcode' : '92998',
    }
}
print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address'])
print(users['address']['city'])

print(users)
print(type(users))
print('\nubah dict ke json')
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json','w') as file:
    json.dump(users, file)


