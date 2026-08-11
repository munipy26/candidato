import re

with open('index.html', 'r') as f:
    content = f.read()

# Add CSS for the new texts
css_additions = """
        .candidate-info { margin: 20px 0; font-size: 16px; color: #000; font-weight: 500; }
        .footer-text { margin-top: 30px; font-size: 11px; color: #555; }
"""
content = content.replace('        #loading-overlay { display: none; color: #d10000; font-weight: bold; margin: 15px 0; font-size: 18px; }', 
                         '        #loading-overlay { display: none; color: #d10000; font-weight: bold; margin: 15px 0; font-size: 18px; }' + css_additions)

# Insert candidate text before buttons
candidate_html = """
        <div class="candidate-info">
            -------<br>
            ¡Gracias por tu consulta y tu confianza!<br>
            CANDIDATO/A - Intendente o Concejal 2026<br>
            Lista: ___ Opción: ___<br>
            --------
        </div>
"""
content = content.replace('<div class="btn-row">', candidate_html + '        <div class="btn-row">')

# Insert footer text at the bottom of the container
footer_html = """
        <div class="footer-text">
            -------<br>
            Padron Actualizado de Afiliados a la ANR para las Internas del 07-Junio-2026.<br>
            -------
        </div>
"""
# Find the end of the container (before </div>\n\n    <script>)
content = content.replace('        </div>\n    </div>\n\n    <script>', '        </div>\n' + footer_html + '    </div>\n\n    <script>')

with open('index.html', 'w') as f:
    f.write(content)
