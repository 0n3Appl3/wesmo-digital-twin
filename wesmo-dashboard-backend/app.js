const dotenv = require('dotenv').config({
    path: __dirname + '/../.env',
})
const cors = require('cors')
const express = require('express')
const app = express()
const port = 3000

// Enable Cross-Origin Resource Sharing
app.use(cors())

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/test', (req, res) => {
    console.log('Incoming request...')
    res.send({
        test: process.env.VITE_TEST
    })
})

app.listen(port, () => {
    console.log(`WESMO Dashboard Backend listening on port ${ port }`)
})