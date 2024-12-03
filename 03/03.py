import re

with open("./03_input.txt", "r") as file:
    content = file.read()

#there's probably some regex to do this in one go but i can't figure it out

#first process removes content where there is opening and closing dont/do
processed_content = re.sub(r"don't\(\).*?do\(\)", "", content, flags=re.DOTALL)
#second process removes content where there isnt a 'closing' do
processed_content = re.sub(r"don't\(.*", "", processed_content, flags=re.DOTALL)

#match all mul(int, int)
pattern = r"mul\((-?\d+),(-?\d+)\)"
matches = re.findall(pattern, processed_content)

total = 0
for x, y in matches:
    total += (int(x)*int(y))

print(total)