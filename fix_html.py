with open('index.html', 'r') as f:
    content = f.read()

# Fix the double </div> at the end of the body
content = content.replace('    </div>\n    </div>', '    </div>')

with open('index.html', 'w') as f:
    f.write(content)
