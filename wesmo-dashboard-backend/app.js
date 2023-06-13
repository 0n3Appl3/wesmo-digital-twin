const dotenv = require('dotenv').config({
    path: __dirname + '/../.env',
})
const { Sequelize, DataTypes, } = require('sequelize')
const cors = require('cors')
const express = require('express')
const app = express()
const port = 3000

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
})

/* 
 * Enable Cross-Origin Resource Sharing.
 */
app.use(cors())

/*
 * Listen Express.js instance on a specified port.
 */
app.listen(port, () => {
    console.log(`WESMO Dashboard Backend listening on port ${ port }`)
    authDatabaseConnection()
})

//////////////////////////////
//                          //
//    REST API Endpoints    //
//                          //
//////////////////////////////

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/test', (req, res) => {
    console.log('Incoming request...')
    res.send({
        test: process.env.VITE_TEST
    })
})

app.get('/rest-test', async (req, res) => {
    // Raw database query using Sequelize.
    const result = await Category.findAll()
    res.send(result)
})

app.get('/rest-test-2', async (req, res) => {
    const result = await Category.findOne({
        order: [
            ['id', 'DESC'],
        ],
    })
    res.send(result)
})

app.get('/rest-test-3', async (req, res) => {
    // req.body will be used later.
    // let data = req.body
    const result = await Category.create({
        id: 13,
        name: 'Test',
    })
    res.send(result)
})