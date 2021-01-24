# Description
This project contains:

    .
    ├── tests                        # Unit tests for address converter function
    │   ├── __init__.py              
    │   ├── test_address_converter.py 
    ├── addressline.py               # Contains address coverter function
    ├── __main__.py                  # Contains main function to handel input args
    ├── requirements.txt             # All packages need to be installed
    └── README.md                    
          

# How to install

1. Clone project:
```
git clone https://github.com/ZEstaji/address-line.git
```

1. Install Python 3.8 or higher
2. Execute following line in CMD in the project folder:
```
pip install -r requirements.txt
```

# How to run 
Execute following line in CMD in the project folder:
```
python . --addr "string to convert"
```

# How to run tests
Execute following line in CMD in the project folder:
```
python -m pytest
```

# Addresses provided for Tests

1  "Winterallee 3" </br>  
2  "Musterstrasse 45" </br>  
3  "Blaufeldweg 123B" </br>  
4  "Am Bأ¤chle 23" </br>  
5  "Auf der Vogelwiese 23 b" </br>  
6  "4, rue de la revolution" </br>  
7  "200 Broadway Av" </br>  
8  "Calle Aduana, 29" </br>  
9  "Calle 39 No 1540" </br>  
10 " " </br>  
11 "invalid address" </br>  
