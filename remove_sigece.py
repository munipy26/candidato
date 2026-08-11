import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove SIGECE button
content = re.sub(r'\s*<button class="btn-gray" id="sigece-btn">SIGECE</button>', '', content)

# Remove Password Modal
content = re.sub(r'\s*<!-- Password Modal -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Remove Password Modal Logic from script
content = re.sub(r'\s*// Password Modal Logic.*?// Allow Enter key in password field.*?}\);', '', content, flags=re.DOTALL)

# Remove CSS for .btn-gray and modal
content = re.sub(r'\.btn-gray\s*{[^}]*}', '', content)
content = re.sub(r'/\* Password Modal \*/.*?\.btn-modal-cancel\s*{[^}]*}', '', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
