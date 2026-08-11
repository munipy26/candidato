import sys

with open('padapplus.html', 'r') as f:
    lines = f.readlines()

new_lines = []
skip_toggle = False

for line in lines:
    # Remove candidate-info div and replace with AGREGAR button
    if '<div class="candidate-info">' in line:
        new_lines.append('        <div id="add-container" style="margin: 20px 0;">\n')
        new_lines.append('            <button class="btn btn-orange" id="agregar" style="width: 100%;">AGREGAR</button>\n')
        new_lines.append('        </div>\n')
        skip_toggle = True
        continue
    if skip_toggle:
        if '</div>' in line and line.strip() == '</div>':
            skip_toggle = False
        continue

    # Modify toggleSearchState
    if 'function toggleSearchState(isMinimized) {' in line:
        new_lines.append(line)
        new_lines.append('            // Modified to keep search card at top\n')
        new_lines.append('            if (isMinimized) {\n')
        new_lines.append('                searchBtns.style.display = "none";\n')
        new_lines.append('                searchCard.style.padding = "16px";\n')
        new_lines.append('            } else {\n')
        new_lines.append('                searchBtns.style.display = "flex";\n')
        new_lines.append('                searchCard.style.padding = "24px";\n')
        new_lines.append('            }\n')
        new_lines.append('        }\n')
        # Skip the original function body
        skip_original_toggle = True
        continue
    
    # We need to skip until the closing brace of the original function
    # But since we added it manually above, we just skip the next few lines
    # This is a bit fragile, let's try a better way for the function replacement

    new_lines.append(line)

# Let's do a more robust replacement for the function and the HTML
content = "".join(new_lines)

import re

# Robustly replace toggleSearchState
old_function = r'function toggleSearchState\(isMinimized\) \{.*?\}'
new_function = """function toggleSearchState(isMinimized) {
            // Modified to keep search card at top
            if (isMinimized) {
                searchBtns.style.display = 'none';
                searchCard.style.padding = '16px';
                searchCard.style.marginBottom = '12px';
            } else {
                searchBtns.style.display = 'flex';
                searchCard.style.padding = '24px';
                searchCard.style.marginBottom = '24px';
            }
        }"""

content = re.sub(old_function, new_function, content, flags=re.DOTALL)

with open('padapplus.html', 'w') as f:
    f.write(content)
