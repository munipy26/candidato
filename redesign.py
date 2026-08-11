import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace <style> section
new_style = """
    <style>
        :root {
            --primary-red: #ED1C24;
            --bg-white: #ffffff;
            --light-gray: #f5f5f5;
            --border-color: #e0e0e0;
            --text-dark: #333;
            --text-gray: #666;
        }

        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            padding: 20px; 
            background-color: var(--bg-white); 
            color: var(--text-dark); 
            margin: 0;
            min-height: 100vh;
        }

        .container { 
            width: 100%; 
            max-width: 500px; 
            text-align: center; 
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .logo { width: 180px; margin-bottom: 20px; }
        .header-title { font-size: 28px; font-weight: bold; margin: 0; color: var(--primary-red); }
        .header-subtitle { font-size: 16px; color: var(--text-gray); margin: 5px 0 30px 0; }
        
        .form-group { text-align: left; margin-bottom: 25px; width: 100%; }
        label { font-weight: bold; font-size: 14px; margin-bottom: 8px; display: block; color: var(--text-gray); }
        input#cedula { 
            width: 100%; 
            height: 48px; 
            padding: 0 15px; 
            border: 2px solid var(--border-color); 
            border-radius: 8px; 
            box-sizing: border-box; 
            font-size: 18px; 
            outline: none;
            transition: border-color 0.3s;
        }
        input#cedula:focus { border-color: var(--primary-red); }
        
        .btn-main { 
            background-color: var(--primary-red); 
            color: white; 
            border: none; 
            height: 52px; 
            width: 100%; 
            border-radius: 26px; 
            font-size: 18px; 
            font-weight: bold; 
            cursor: pointer; 
            box-shadow: 0 4px 6px rgba(237, 28, 36, 0.2);
            transition: transform 0.1s, box-shadow 0.1s;
        }
        .btn-main:active { transform: translateY(2px); box-shadow: 0 2px 3px rgba(237, 28, 36, 0.2); }

        #loading-overlay { display: none; color: var(--primary-red); font-weight: bold; margin: 15px 0; }

        /* Modal Styles */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background-color: white;
            width: 90%;
            max-width: 400px;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            animation: modalIn 0.3s ease-out;
        }
        @keyframes modalIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .modal-header {
            padding: 20px;
            border-bottom: 1px solid var(--border-color);
            text-align: left;
        }
        .modal-header h3 { margin: 0; color: var(--primary-red); font-size: 20px; }

        .modal-body { padding: 20px; text-align: left; }
        .data-row { margin-bottom: 12px; }
        .data-label { font-size: 12px; color: var(--text-gray); text-transform: uppercase; font-weight: bold; }
        .data-value { font-size: 16px; color: var(--text-dark); font-weight: 500; }

        .modal-footer-candidate {
            background-color: var(--light-gray);
            padding: 15px 20px;
            display: flex;
            align-items: center;
            border-top: 1px solid var(--border-color);
        }
        .candidate-photo {
            width: 50px;
            height: 50px;
            border-radius: 25px;
            background-color: var(--border-color);
            margin-right: 15px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        .candidate-photo img { width: 100%; height: 100%; object-fit: cover; }
        .candidate-info-text { text-align: left; }
        .candidate-name { color: var(--primary-red); font-weight: bold; font-size: 16px; margin: 0; }
        .candidate-list { color: var(--text-gray); font-size: 13px; margin: 2px 0 0 0; }

        .btn-close {
            width: 100%;
            padding: 15px;
            border: none;
            background-color: white;
            color: var(--text-gray);
            font-weight: bold;
            cursor: pointer;
            border-top: 1px solid var(--border-color);
        }

        .footer-fixed {
            margin-top: auto;
            padding: 20px 0;
            font-size: 10px;
            color: var(--text-gray);
            text-align: center;
            width: 100%;
            max-width: 500px;
        }
    </style>
"""
content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

# Update Body structure
new_body = """
<body>
    <div class="container">
        <img src="padronapp.png" alt="logo" class="logo">
        <h1 class="header-title">PADRONAPP</h1>
        <h2 class="header-subtitle">APP DE CONSULTAS AL PADRON ANR 2026</h2>
        
        <div class="form-group">
            <label for="cedula">Cédula de Identidad:</label>
            <input type="text" id="cedula" placeholder="Ingrese su número">
        </div>

        <button class="btn-main" id="aceptar">CONSULTAR</button>

        <div id="loading-overlay">Cargando base de datos...</div>
        
        <div class="footer-fixed">
            -------<br>
            Padron Actualizado de Afiliados a la ANR para las Internas del 07-Junio-2026.<br>
            -------
        </div>
    </div>

    <!-- Results Modal -->
    <div id="result-modal" class="modal-overlay">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Datos del Elector</h3>
            </div>
            <div class="modal-body" id="modal-data">
                <!-- Data will be injected here -->
            </div>
            <div class="modal-footer-candidate">
                <div class="candidate-photo">
                    <img src="padronapp.png" alt="Candidato">
                </div>
                <div class="candidate-info-text">
                    <p class="candidate-name">NOMBRE DEL CANDIDATO</p>
                    <p class="candidate-list">Lista: ___ | Opción: ___</p>
                </div>
            </div>
            <button class="btn-close" id="cerrar-modal">CERRAR</button>
        </div>
    </div>
"""
content = re.sub(r'<body>.*?<script>', new_body + '\n    <script>', content, flags=re.DOTALL)

# Update Script Logic
new_script_logic = """
        window.csvData = [];
        let isLoaded = false;

        // Load CSV
        const loader = document.getElementById('loading-overlay');
        loader.style.display = 'block';
        
        Papa.parse('padronapp.csv', {
            download: true,
            header: true,
            delimiter: ";",
            encoding: "ISO-8859-1",
            skipEmptyLines: true,
            complete: function(results) {
                window.csvData = results.data;
                isLoaded = true;
                loader.style.display = 'none';
                console.log('CSV Loaded');
            },
            error: function(err) {
                loader.textContent = 'Error al cargar datos.';
            }
        });

        const modal = document.getElementById('result-modal');
        const modalData = document.getElementById('modal-data');

        function showResult(record) {
            if (!record) return;
            
            modalData.innerHTML = `
                <div class="data-row">
                    <div class="data-label">Nombre Completo</div>
                    <div class="data-value">${record.nombre} ${record.apellido}</div>
                </div>
                <div class="data-row">
                    <div class="data-label">Local de Votación</div>
                    <div class="data-value">${record.local_votacion}</div>
                </div>
                <div class="data-row" style="display: flex; gap: 30px;">
                    <div>
                        <div class="data-label">Mesa</div>
                        <div class="data-value">${record.mesa}</div>
                    </div>
                    <div>
                        <div class="data-label">Orden</div>
                        <div class="data-value">${record.orden}</div>
                    </div>
                </div>
                <div class="data-row">
                    <div class="data-label">Dirección</div>
                    <div class="data-value">${record.direccion}</div>
                </div>
            `;
            modal.style.display = 'flex';
        }

        document.getElementById('aceptar').addEventListener('click', () => {
            if (!isLoaded) {
                alert('La base de datos aún se está cargando.');
                return;
            }
            const val = document.getElementById('cedula').value.trim();
            if (!val) {
                alert('Por favor, ingrese un número de cédula.');
                return;
            }
            const currentRecord = window.csvData.find(r => r.cedula === val);
            if (currentRecord) {
                showResult(currentRecord);
            } else {
                alert('El número de cédula no se encuentra en el padrón.');
            }
        });

        document.getElementById('cerrar-modal').addEventListener('click', () => {
            modal.style.display = 'none';
        });

        // Close on overlay click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.style.display = 'none';
        });
"""
content = re.sub(r'<script>\s*window\.csvData = \[\];.*?<\/script>', '<script>\n' + new_script_logic + '\n    </script>', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
