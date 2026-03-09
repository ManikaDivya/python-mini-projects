import pyperclip as p

print("Enter multiple lines (type 'stop' to finish):")

lines = []

while True:
    line = input()

    if line.lower() == "stop":
        break

    lines.append(line)

text = "\n".join(lines)

p.copy(text)

print("Text copied to clipboard!")
print("Pasted Text:")
print(p.paste())
