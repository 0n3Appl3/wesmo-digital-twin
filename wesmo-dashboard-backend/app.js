const dotenv = require('dotenv').config({
    path: __dirname + '/../.env',
})
const { Sequelize, DataTypes, } = require('sequelize')
const bodyParser = require('body-parser')
const mqtt = require('mqtt')
const socketIo = require('socket.io')
const http = require('http')
const cors = require('cors')
const express = require('express')
const app = express()
const server = http.createServer(app)
const io = socketIo(server, {
    cors: {
        origin: '*',
    },
    transports: ['websocket', 'polling', 'flashsocket']
})
const port = 3000

/*
 * Setting up MQTT
 */
const mqttClient = mqtt.connect('http://wesmo.co.nz:1883/');

mqttClient.on('connect', () => {
    console.log('Connected to MQTT Broker');
    mqttClient.subscribe('<check with Casper>');
});

/*
 * Setting up listening for message
 */
mqttClient.on('message', (topic, message) => {
    console.log(`Received message on ${ topic }: ${ message.toString() }`);
    // Emit message (socket.io)
    io.emit('event', message.toString());
});

/*
 * Setting up Socket.io
 */
io.on('connection', (socket) => {
    console.log('User connected!');
    emitTest();
    socket.on('disconnect', () => {
        console.log('User disconnected!');
    });
});

// Run the server.
server.listen(port, () => {
    console.log(`WESMO Backend running on port ${ port }`);
})

// TESTING PURPOSES (pretend this is data to be displayed on the dashboard)
const emitTest = () => {
    setTimeout(async () => {
        const num = Math.floor(Math.random() * 100);
        await io.emit('event', num);
        emitTest();
    }, 1 * 1000);
}

// REST API endpoint naming properties.
const appContext = 'api'
const appVersion = 'v1'
const prefix =  '/' + appContext + '/' + appVersion

let responseData = null

/*
 * Create new instance of Sequelize.
 */
const sequelize = new Sequelize(
    process.env.VITE_DB_NAME, 
    process.env.VITE_DB_USER, 
    process.env.VITE_DB_PASSWORD,
    {
        host: process.env.VITE_DB_HOST,
        dialect: 'mysql',
        define: {
            freezeTableName: true,
            timestamps: false,
        }
    }
)

/*
 * Ensure connection to the database was successful.
 */
const authDatabaseConnection = async () => {
    try {
        await sequelize.authenticate()
        console.log('Connection to database has been established successfully.')
    } catch(error) {
        console.error('Unable to connect to the database: ', error)
    }
}

/*
 * Category Model (test model)
 */
const Category = sequelize.define('category', {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        allowNull: false,
    },
    name: {
        type: DataTypes.STRING,
        allowNull: false,
    },
})

Category.afterCreate(async (category, options) => {
    console.log('--------\n\n')
    console.log(category.dataValues)
    console.log('\n\n--------\n')
    responseData = category.dataValues
})

/* 
 * Enable Cross-Origin Resource Sharing.
 */
app.use(cors())

/*
 * Listen Express.js instance on a specified port.
 */
app.listen((port + 1), () => {
    console.log(`WESMO Dashboard Backend listening on port ${ (port + 1) }`)
    authDatabaseConnection()
})

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false,
}))

//////////////////////////////
//                          //
//    REST API Endpoints    //
//                          //
//////////////////////////////

app.get(prefix + '/test', (req, res) => {
    if (!responseData) {
        return res.status(204).send()
    }
    res.status(200).json(responseData)
    responseData = null
})

app.get(prefix + '/battery-data', async (req, res) => {
    const result = await Category.findAll()

    if (!result) {
        return res.status(404).json({
            status: 'Fail',
            message: 'No results found'
        })
    }
    res.status(200).json(result)
})

app.get(prefix + '/battery-data/latest', async (req, res) => {
    const result = await Category.findOne({
        order: [
            ['id', 'DESC'],
        ],
    })
    res.status(200).json(result)
})

// DEVELOPMENT ENDPOINTS (NOT FINAL)
app.get(prefix + '/rest-test', async (req, res) => {
    const result = await Category.findAll()

    if (!result) {
        return res.status(404).json({
            status: 'Fail',
            message: 'No results found'
        })
    }
    res.status(200).json(result)
})

app.get(prefix + '/rest-test-2', async (req, res) => {
    const result = await Category.findOne({
        order: [
            ['id', 'DESC'],
        ],
    })
    res.status(200).json(result)
})

app.post(prefix + '/rest-test-3', async (req, res) => {
    try {
        const result = await Category.create({
            id: req.body.id,
            name: req.body.name,
        })
        res.status(200).json(result)
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
})

app.all('*', (req, res) => {
    res.status(404).json({
        status: 'Fail',
        message: `The endpoint ${ req.originalUrl } does not exist`,
    })
})