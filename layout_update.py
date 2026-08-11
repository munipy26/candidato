import re

with open('index.html', 'r') as f:
    content = f.read()

# CSS adjustments
new_css = """
        .logo { width: 170px; margin-bottom: 20px; }
        .red-banner { background-color: #d10000; color: white; padding: 18px; font-size: 22px; font-weight: bold; margin-bottom: 10px; border-radius: 4px; text-align: center; }
        
        /* Layout Grid for Mesa/Orden and Info */
        .grid-row-2 { display: flex; gap: 20px; margin-bottom: 15px; }
        .grid-row-3 { display: flex; justify-content: space-between; gap: 10px; margin-top: 20px; text-align: center; }
        
        .result-item { flex: 1; text-align: left; }
        .result-label { font-size: 11px; font-weight: bold; color: #666; text-transform: uppercase; margin-bottom: 4px; }
        .result-value { font-size: 16px; font-weight: 500; color: #000; }
        
        .grid-col { flex: 1; padding: 10px 5px; background-color: #f8f9fa; border-radius: 4px; }
        .grid-label { font-size: 10px; font-weight: bold; color: #666; text-transform: uppercase; }
        .grid-value { font-size: 14px; font-weight: 500; color: #d10000; margin-top: 5px; }

        /* Full width result */
        .result-full { width: 100%; border-bottom: 1px solid #eee; padding: 12px 0; margin-bottom: 10px; }
"""
content = re.sub(r'\.logo\s*{[^}]*}\s*\.header-title\s*{[^}]*}\s*\.header-subtitle\s*{[^}]*}\s*\.divider\s*{[^}]*}\s*\.red-banner\s*{[^}]*}', 
                new_css, content, flags=re.DOTALL)

# Update Body structure
new_body = """
<body>
    <div class="container">
        <img src="padronapp.png" alt="logo" class="logo">
        <div class="red-banner">Padron ANR 2026 - Fernando de la Mora</div>
        <div class="divider"></div>
        
        <div class="form-group">
            <label for="cedula">Cédula de Identidad:</label>
            <input type="text" id="cedula" placeholder="0">
        </div>

        <div id="loading-overlay">Cargando base de datos...</div>

        <div id="result-container" style="width: 100%; text-align: left;">
            <!-- Custom rendered results -->
        </div>
"""
# Replace body content before candidate-info
content = re.sub(r'<body>.*?<div class="candidate-info">', new_body + '\n        <div class="candidate-info">', content, flags=re.DOTALL)

# Update JavaScript renderResult
new_js_render = """
        function renderResult(record) {
            const container = document.getElementById('result-container');
            container.innerHTML = '';
            if (!record) return;
            
            container.innerHTML = `
                <div class="result-full">
                    <div class="result-label">NOMBRE COMPLETO</div>
                    <div class="result-value">${record.nombre} ${record.apellido}</div>
                </div>
                <div class="result-full">
                    <div class="result-label">LOCAL DE VOTACIÓN</div>
                    <div class="result-value">${record.local_votacion}</div>
                </div>
                <div class="grid-row-2">
                    <div class="result-item">
                        <div class="result-label">MESA</div>
                        <div class="result-value">${record.mesa}</div>
                    </div>
                    <div class="result-item">
                        <div class="result-label">ORDEN</div>
                        <div class="result-value">${record.orden}</div>
                    </div>
                </div>
                <div class="result-full">
                    <div class="result-label">DIRECCIÓN</div>
                    <div class="result-value">${record.direccion}</div>
                </div>
                <div class="grid-row-3">
                    <div class="grid-col">
                        <div class="grid-label">NACIMIENTO</div>
                        <div class="grid-value">${record.fecha_nacimiento}</div>
                    </div>
                    <div class="grid-col">
                        <div class="grid-label">AFILIACIÓN</div>
                        <div class="grid-value">${record.fecha_afiliacion}</div>
                    </div>
                    <div class="grid-col">
                        <div class="grid-label">EDAD</div>
                        <div class="grid-value">${record.edad}</div>
                    </div>
                </div>
            `;
        }
"""
content = re.sub(r'function renderResult\(record\)\s*{.*?}', new_js_render, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
