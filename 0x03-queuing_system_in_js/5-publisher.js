// 5-publisher.js
import { createClient } from 'redis';

const publisher = createClient();

// Handle successful connection
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle connection errors
publisher.on('error', (error) => {
    console.log('Redis client not connected to the server: ' + error);
});

// Function to publish messages
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school channel', message);
    }, time);
}

// Connect to the Redis server and publish messages
publisher.connect().then(() => {
    publishMessage("Holberton Student #1 starts course", 100);
    publishMessage("Holberton Student #2 starts course", 200);
    publishMessage("KILL_SERVER", 300);
    publishMessage("Holberton Student #3 starts course", 400);
}).catch((error) => {
    console.error('Error connecting to Redis:', error);
});