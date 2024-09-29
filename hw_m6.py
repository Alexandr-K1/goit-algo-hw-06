from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, value):
        if len(value) < 10:
            raise ValueError('Number less than 10 digits!')
        elif len(value) > 10:
            raise ValueError('Number more than 10 digits!')
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone_value):
        phone_to_remove = self.find_phone(phone_value)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone_val, new_phone_val):
        phone_to_edit = self.find_phone(old_phone_val)
        if phone_to_edit:
            self.remove_phone(old_phone_val)
            self.add_phone(new_phone_val)
        else:
            raise ValueError('Old number not found!')

    def find_phone(self, phone_value):
        result = list(filter(lambda phone: phone.value == phone_value, self.phones))
        return result[0] if len(result) > 0 else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
