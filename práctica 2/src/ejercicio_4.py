import re

def validar_email (email):
    patron = r'^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    if re.match(patron,email):
        if (not email.startswith('.')) and (not email.endswith('.')):
            return True
    return False
