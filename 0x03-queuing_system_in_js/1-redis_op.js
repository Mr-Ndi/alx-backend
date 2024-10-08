// 1-redis_op.js
import { createClient } from 'redis';

const client = createClient();

// Handle successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (error) => {
    console.log('Redis client not connected to the server: ' + error);
});

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

// Function to display the value of a school
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, value) => {
        if (error) {
            console.error('Error retrieving value:', error);
        } else {
            console.log(value); // Log the value to the console
        }
    });
}

// Connect to the Redis server
client.connect().then(() => {
    // Call the functions as specified
    displaySchoolValue('Holberton'); // Attempt to display value for a key that may not exist
    setNewSchool('HolbertonSanFrancisco', '100'); // Set new school value
    displaySchoolValue('HolbertonSanFrancisco'); // Display the newly set value

    // Close the connection after operations
    client.quit();
}).catch((error) => {
    console.error('Error connecting to Redis:', error);
});