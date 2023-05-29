const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/test', (req, res) => {
    res.send('Test')
})

app.listen(port, () => {
    console.log(`WESMO Dashboard Backend listening on port ${ port }`)
})