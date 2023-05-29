const dotenv = require('dotenv').config({
    path: __dirname + '/../.env',
})
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/test', (req, res) => {
    res.send('Test: ' + process.env.TEST)
})

app.listen(port, () => {
    console.log(`WESMO Dashboard Backend listening on port ${ port }`)
})