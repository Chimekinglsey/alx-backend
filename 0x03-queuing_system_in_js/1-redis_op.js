import Redis from 'ioredis';
const utils = require('util')

const redisClient = new Redis();

redisClient.on('connect', ()=>{
    console.log('Redis client connected to the server')
})
redisClient.on('error', (error)=>{
    console.log(`Redis client not connected to the server: ${error}`)
})
redisClient.set = utils.promisify(redisClient.set)
redisClient.get = utils.promisify(redisClient.get)
async function setNewSchool(schoolName, value) {
    try {
        await redisClient.set(schoolName, value);
            console.log(`value ${value} set for schoool ${schoolName}`)
    }
    catch(error)  {
        console.log(`Error occurred: ${err}`)
    }
}
async function displaySchoolValue(schoolName){
    try {
        const val = await redisClient.get(schoolName);
        console.log(val)

    }
   catch (error) {
       console.log(error)
}
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
