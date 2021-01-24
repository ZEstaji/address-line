import json

from addressline import address_converter


def test_empty_address():
    result = address_converter("")
    assert result == '"Invalid address"'


def test_invalid_address():
    result = address_converter("invalid_address")
    assert result == '"Invalid address"'


def test_valid_addresses():
    sample_addresses = {
        "Winterallee 3": {"street": "Winterallee", "housenumber": "3"},
        "Musterstrasse 45": {"street": "Musterstrasse", "housenumber": "45"},
        "Blaufeldweg 123B": {"street": "Blaufeldweg", "housenumber": "123B"},
        "Am Bächle 23": {"street": "Am Bächle", "housenumber": "23"},
        "Auf der Vogelwiese 23 b": {
            "street": "Auf der Vogelwiese",
            "housenumber": "23 b",
        },
        "4, rue de la revolution": {
            "street": "rue de la revolution",
            "housenumber": "4",
        },
        "200 Broadway Av": {"street": "Broadway Av", "housenumber": "200"},
        "Calle Aduana, 29": {"street": "Calle Aduana", "housenumber": "29"},
        "Calle 39 No 1540": {"street": "Calle 39", "housenumber": "No 1540"},
    }

    for address in sample_addresses.keys():
        assert json.loads(address_converter(address)) == sample_addresses[address]
