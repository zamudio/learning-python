empty_space = '            content       '

print(empty_space.rstrip())  # space still in front, but cut from the end

print(empty_space.lstrip())  # space still on the end, but cut in front

print(empty_space.strip())  # cuts all empty spaces

web = 'www.google.com'

print(web.strip('w.'))
