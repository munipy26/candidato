import re

with open('index.html', 'r') as f:
    content = f.read()

# The previous sed/re-sub might have cut too much or messed up the closing tags.
# Let's clean up the script part to be robust.

script_start = """
    <script>
        window.csvData = [];
        let currentRecord = null;
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
                loader.textContent = 'Error al cargar datos. Asegúrese de que el archivo padronapp.csv existe.';
            }
        });

        const tableBody = document.getElementById('data-table');

        
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
            currentRecord = window.csvData.find(r => r.cedula === val);
            if (currentRecord) {
                renderResult(currentRecord);
            } else {
                alert('El número de cédula no se encuentra en el padrón.');
                renderResult(null);
            }
        });

        document.getElementById('limpiar').addEventListener('click', () => {
            document.getElementById('cedula').value = '';
            document.getElementById('result-container').innerHTML = '';
            currentRecord = null;
        });
    </script>
"""

content = re.sub(r'<script>.*?</script>', script_start, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
