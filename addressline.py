import json
import re


def address_converter(address):
    """This function gets an string as address and returns
    string of street and string of street-number as JSON object

    Args:
        address (str): concatenated address

    Returns:
        JSON: string of street and string of street-number as JSON object if address string is valid
            otherwise returns "Invalid address"

    Examples:
        >>> address_converter("Winterallee 3")
            {"street": "Winterallee", "housenumber": "3"}
        >>> address_converter("4, rue de la revolution")
            {"street": "rue de la revolution", "housenumber": "4"}
        >>> address_converter("Calle 39 No 1540")
            {"street": "Calle 39", "housenumber": "No 1540"})
        >>> address_converter( "Calle Aduana, 29")
            {"street": "Calle Aduana", "housenumber": "29"})
    """
    house_number = ""
    street = ""

    # converts multi spaces to one space if user enter extra space in address
    address = re.sub(" +", " ", address)

    # eliminate "," of addresses like  "Calle Aduana, 29"
    address = re.sub(",", "", address)

    patterns = [
        r"(?P<street>^\D+) (?P<house_number>\d+.*)",  # for adresses like "Winterallee 3"
        r"(?P<house_number>^\d+) (?P<street>.*)",  # for addresses like "4, rue de la revolution"
        r"(?P<street>^.*) (?P<house_number>No.*)",  # for addresses like "Calle 39 No 1540"
    ]

    for pattern in patterns:
        match = re.match(pattern, address)
        if match is None:
            continue
        street = match.group("street")
        house_number = match.group("house_number")

    if len(street) != 0 and len(house_number) != 0:
        return json.dumps({"street": street, "housenumber": house_number})
    else:
        # Just in case if any invalid address entered
        return json.dumps("Invalid address")
