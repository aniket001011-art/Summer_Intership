password=input("\n ENter your password-- ")

def is_secure(password):
    if (len(password)>=8 and "!" in password):
        return True
    else:
        return False
@is_secure
def other_fun():
    return "hello "
h=is_secure(password)
print("\nyour password is--",h)
