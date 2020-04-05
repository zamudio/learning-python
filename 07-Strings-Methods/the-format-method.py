# mad_libs = '{} laughed at the {} {}.'  # name, adj, noun

# print(mad_libs.format('Bobby', 'green', 'alien'))

mad_libs = '{name} laughed at the {adj} {noun}.'

name = input('Enter a name: ')
adj = input('Enter an adj: ')
noun = input('Enter a noun: ')

print(mad_libs.format(name=name, adj=adj, noun=noun))
