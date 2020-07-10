class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user):
        if user in Library.user_records:
            return f'User with id = {user.user_id} already registered in the library!'

        Library.user_records.append(user)
        Library.rented_books[user.username] = {}

    def remove_user(self, user):
        if user not in Library.user_records:
            return f'We could not find such user to remove!'

        Library.user_records.remove(user)
        del Library.rented_books[user.username]

    def change_username(self, user_id, new_username):
        users_var = [i.user_id for i in Library.user_records]

        if user_id not in users_var:
            return f'There is no user with id = {user_id}!'

        person = [i for i in Library.user_records if i.user_id == user_id][0]

        if person.username == new_username:
            return f'Please check again the provided username - ' \
                   f'it should be different than the username used so far!'

        Library.rented_books[new_username] = Library.rented_books[person.username]
        del Library.rented_books[person.username]
        person.username = new_username

        return f'Username successfully changed to: {new_username} for userid: {user_id}'