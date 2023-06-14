const dotenv = require('dotenv').config({
    path: __dirname + '/../.env',
})
const { Sequelize, DataTypes, } = require('sequelize')
const cors = require('cors')
const express = require('express')
const app = express()
const port = 3000

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
app.listen(port, () => {
    console.log(`WESMO Dashboard Backend listening on port ${ port }`)
    authDatabaseConnection()
})

//////////////////////////////
//                          //
//    REST API Endpoints    //
//                          //
//////////////////////////////

app.get(prefix + '/test', (req, res) => {
    if (!responseData) {
        return res.status(204).json({
            status: 'Fail',
            message: 'No new data found',
        })
    }
    res.status(200).json(responseData)
    responseData = null
})

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

app.get(prefix + '/rest-test-3', async (req, res) => {
    // req.body will be used later.
    // let data = req.body
    try {
        const result = await Category.create({
            id: 13,
            name: 'Test',
        })
        res.status(200).json(result)
    } catch (error) {
        res.status(500).json({
            status: 'Error',
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