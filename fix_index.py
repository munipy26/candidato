import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix the broken JS at the end of renderResult
broken_js_pattern = r'}\s*:\s*</td>\s*<td>\s*\${record\[keys\[i\]\]\s*\|\|\s*\'\'}\s*</td>`;\s*tableBody\.appendChild\(tr\);\s*}\s*}'
fixed_js = '}'
content = re.sub(broken_js_pattern, fixed_js, content, flags=re.DOTALL)

# Also fix the cleanup in the script (remove unused tableBody stuff and fix the rest of the file)
# The broken part looks like:
#         }
# :</td><td>${record[keys[i]] || ''}</td>`;
#                 tableBody.appendChild(tr);
#             }
#         }

pattern2 = r'}\n:</td><td>\${record\[keys\[i\]\] \|\| \'\'}</td>`;\n                tableBody\.appendChild\(tr\);\n            }\n        }'
content = re.sub(pattern2, '}', content)

# Remove the unused divider style definition and other leftover CSS if any
# Actually, the divider class is used in HTML but I removed its style. Let's add it back.
if '.divider {' not in content:
    content = content.replace('.red-banner {', '.divider { width: 100%; height: 2px; background-color: #eee; margin: 10px 0 20px 0; }\n        .red-banner {')

# Ensure cleanup of the script - the 'limpiar' button should also clear the result-container
content = content.replace("document.getElementById('cedula').value = '';", "document.getElementById('cedula').value = '';\n            document.getElementById('result-container').innerHTML = '';")

with open('index.html', 'w') as f:
    f.write(content)
