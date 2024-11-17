cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

orange_cats = [name for name in cats_colors
                if cats_colors[name] == 'orange']
print(orange_cats)

non_orange_cats = [name for name in cats_colors
                   if cats_colors[name] != 'orange']
print(non_orange_cats)