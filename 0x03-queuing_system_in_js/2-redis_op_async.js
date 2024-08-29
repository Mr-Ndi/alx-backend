// 2-redis_op_async.js
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

// Handle successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (error) => {
    console.log('Redis client not connected to the server: ' + error);
});

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

// Function to set a new school value
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error('Error setting value:', err);
        } else {
            console.log(`Reply: ${reply}`); // Confirmation message using redis.print
        }
    });
}

// Function to display the value of a school using async/await
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value); // Log the value to the console
    } catch (error) {
        console.error('Error retrieving value:', error);
    }
}

// Connect to the Redis server and perform operations
client.connect().then(async () => {
    await displaySchoolValue('Holberton'); // Attempt to display value for a key that may not exist
    setNewSchool('HolbertonSanFrancisco', '100'); // Set new school value
    await displaySchoolValue('HolbertonSanFrancisco'); // Display the newly set value

    // Close the connection after operations
    client.quit();
}).catch((error) => {
    console.error('Error connecting to Redis:', error);
});