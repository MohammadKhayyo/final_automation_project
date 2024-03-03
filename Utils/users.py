from operator import itemgetter

# we can store test data in this module like users
valid_users = [
    {"name": "mohammadkhayyo12account", "email": "mohammadkhayyo12@gmail.com", "password": "+j.q2B,TrA8+#pj"},

]

invalid_users = [
    {"name": "invalid", "email": "invalidUser@test.com", "password": "aG}+d6Ua9R7>"},
    {"name": "ALI", "email": "ali_drawy@test.com", "password": "MSU8u6W4Z7?p"},
    {"name": "Mohammad", "email": "Mohammad@test.com", "password": "oe4(Y7l3dELL"}

]


def get_valid_user(name):
    try:
        return next(user for user in valid_users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


def get_invalid_user(name):
    try:
        return next(user for user in invalid_users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


def get_all_valid_users():
    return valid_users


def get_all_invalid_users():
    return invalid_users
