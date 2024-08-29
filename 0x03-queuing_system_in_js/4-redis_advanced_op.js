// 4-redis_advanced_op.js
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

// Function to create a hash with school values
function createHash() {
    const hashKey = 'HolbertonSchools';
    const schools = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };

    // Use hset to store each value in the hash
    for (const [city, value] of Object.entries(schools)) {
        client.hSet(hashKey, city, value, redis.print);
    }
}

// Function to display the hash
function displayHash() {
    const hashKey = 'HolbertonSchools';
    client.hGetAll(hashKey, (error, result) => {
        if (error) {
            console.error('Error retrieving hash:', error);
        } else {
            console.log(result); // Log the entire hash object
        }
    });
}

// Connect to the Redis server and perform operations
client.connect().then(() => {
    createHash(); // Create the hash
    displayHash(); // Display the hash
    client.quit(); // Close the connection
}).catch((error) => {
    console.error('Error connecting to Redis:', error);
});