const csv = require('csv-parser');
const fs = require('fs');

const filepath = "./disasters.csv"

fs.createReadStream(filepath)
    .on('error', () => {
        // handle error
    })
    
    .pipe(csv())
    
    .on('data', (row) => {
        let str = `${row["Description"]} bought ${row["People"]}.`;
        console.log(str);

    })

    .on('end', () => {
        // handle end of CSV
    })
