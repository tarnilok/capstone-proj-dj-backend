import uuid

def get_random_code():
    code = str(uuid.uuid4())
    code2= ''.join(code.split('-'))[0:10]
    return code2

print(get_random_code())