my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

# Create dict with strings as keys and string length as values. Only odd lens.
strlen_dict = { name: len(name) 
                for name in my_set
                if len(name) % 2 != 0 }
print(strlen_dict)