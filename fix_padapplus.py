import re

with open('padapplus.html', 'r') as f:
    content = f.read()

# Fix toggleSearchState - replace everything from first function toggleSearchState to the last closing brace before cedulaInput.addEventListener
pattern = r'function toggleSearchState\(isMinimized\) \{.*?cedulaInput\.addEventListener'
replacement = """function toggleSearchState(isMinimized) {
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
        }

        cedulaInput.addEventListener"""

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Clean up unused CSS
content = re.sub(r'\.candidate-info \{.*?\}', '', content, flags=re.DOTALL)

with open('padapplus.html', 'w') as f:
    f.write(content)
