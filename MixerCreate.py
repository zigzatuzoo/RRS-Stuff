from requests import get

print("What is the name of the parent room? EX: RecCenter or GoldenTrophy DONT ADD THE CARROT(Casing does matter)\n")
parent = input()
print("What is the name of the sub room? EX: Act-1 or Main (Casing does matter)\n")
sub = input()

yaml = get('https://raw.githubusercontent.com/zigzatuzoo/RRS-Stuff/main/mixerconfig.txt').text

yaml = yaml.replace('ROOMNAME',f'{parent}-{sub}')

file = open(f'{parent}-{sub}.mixer','x')

file.write(yaml)

file.close()
