cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
    'Larry':  'orange',
    'Lenny':  'orange',
}

orange_cats = [name.replace('L', 'K') for name in cats_colors
               if 'L' in name]
print(orange_cats)

non_orange_cats = [name for name in cats_colors
                   if cats_colors[name] != 'orange'
                   if cats_colors[name] != 'black']
print(non_orange_cats)

l_orange_cats = [name for name in cats_colors
                 if cats_colors[name] == 'orange'
                 if name[:2] == 'Le']
print(l_orange_cats)