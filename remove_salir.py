import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove Salir button
content = re.sub(r'\s*<button class="btn-orange" id="salir">Salir</button>', '', content)

# Remove Salir button event listener
content = re.sub(r'\s*document\.getElementById\(\'salir\'\)\.addEventListener\(\'click\', \(.*?\}\);\s*', '', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
