#Made by @dyphen12

import pymysql.cursors

# Connect to the database.

mothercon = pymysql.connect(host='yourhost',
                            user='youruser',
                            password='password1234',
                            db='dbname')

####USER VALIDATION####

def user_validation(user, password):
    try:

        connection = mothercon

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `users` WHERE `username` LIKE %s"
            cursor.execute(sql, (user,))
            result = cursor.fetchone()
            print(result, '///////this is the result')
            if result is not None:
                print('validating process...')
                print(result[0],'//////// this is result[0]')
                if result[0]==user:
                    print('user validated!')
                    if result[1]==password:
                        print('password validated!')
                        msg = ('password validated!')
                        return True, result[4]
                    else:
                        print('wrong password :(')
                        err = ('wrong password :(')
                        return False, err
                else:
                    print('user not valid')
                    err = ('user not valid')
                    return False, err
            else:
                print('Credentials Error')
                err = ('Credentials Error')
                return False, err


    finally:
        connection.close()
