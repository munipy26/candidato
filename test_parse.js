const Papa = require('papaparse');
const fs = require('fs');
const csv = fs.readFileSync('padronapp.csv', 'utf8').split('\n').slice(0, 5).join('\n');

Papa.parse(csv, {
    header: true,
    skipEmptyLines: true,
    complete: function(results) {
        console.log('Keys:', Object.keys(results.data[0]));
        console.log('First record:', results.data[0]);
    }
});
