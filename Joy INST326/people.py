import re

class Address:
    """
    A class to represent an address.

    Attributes:
    -----------
    street : str
        The street address.
    city : str
        The city part of the address.
    state : str
        The state part of the address.

    Methods:
    --------
    __init__(self, street, city, state):
        Initializes the Address with street, city, and state.
    """
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def __repr__(self):
        return f"{self.street}, {self.city}, {self.state}"

class Employee:
    """
    A class to represent an employee.

    Attributes:
    -----------
    first_name : str
        Employee's first name.
    last_name : str
        Employee's last name.
    address : Address
        Employee's address, an instance of the Address class.
    email : str
        Employee's email address.

    Methods:
    --------
    __init__(self, text):
        Constructs all the necessary attributes for the employee object.
    """
    def __init__(self, text):
        self.first_name, self.last_name = parse_name(text)
        self.address = parse_address(text)
        self.email = parse_email(text)

    def __repr__(self):
        return f"Employee(Name: {self.first_name} {self.last_name}, Address: {self.address}, Email: {self.email})"

def parse_name(text):
    """
    Parses the first name and last name from a string.

    Parameters:
    ----------
    text : str
        A string containing a person's full name.

    Returns:
    -------
    tuple
        A tuple containing the first name and last name.
    """
    name_regex = r"^\w+\s\w+"
    match = re.match(name_regex, text)
    if match:
        first_name, last_name = match.group().split()
        return first_name, last_name
    return None, None

def parse_address(text):
    """
    Parses the street, city, and state from a string and returns an Address object.

    Parameters:
    ----------
    text : str
        A string containing a person's address.

    Returns:
    -------
    Address
        An Address object with street, city, and state attributes filled.
    """
    address_regex = r"(\d+\s[\w\s]+)\s([\w\s]+)\s([A-Z]{2})"
    match = re.search(address_regex, text)
    if match:
        street, city, state = match.groups()
        return Address(street, city, state)
    return Address(None, None, None)

def parse_email(text):
    """
    Parses the email address from a string.

    Parameters:
    ----------
    text : str
        A string containing a person's email address.

    Returns:
    -------
    str
        The email address found in the string.
    """
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    match = re.search(email_regex, text)
    if match:
        return match.group()
    return None

def main(path):
    """
    Reads a text file from the given path, parses each line, and creates a list of Employee objects.

    Parameters:
    ----------
    path : str
        The path to the text file containing employee data.

    Returns:
    -------
    list
        A list of Employee objects.
    """
    employee_list = []
    with open(path, 'r') as file:
        for line in file:
            employee = Employee(line.strip())
            employee_list.append(employee)
    return employee_list

# Check if the script is the main program and execute
if __name__ == "__main__":
    employees = main("people.txt")
    for emp in employees:
        print(emp)
