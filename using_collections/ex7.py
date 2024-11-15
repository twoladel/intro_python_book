# First solution that came to mind
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
my_list = list(info)

for i in range(len(my_list)):
    if my_list[i] == ':':
        my_list[i] = '+'

print(''.join(my_list))

# Reread the problem and understood must use str methods
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info = info.split(':')
print('+'.join(info))

# Solution after searching str documentation
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info.replace(':', '+'))