// 5-subscriber.js
import { createClient } from 'redis';

const subscriber = createClient();

// Handle successful connection
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle connection errors
subscriber.on('error', (error) => {
    console.log('Redis client not connected to the server: ' + error);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Handle messages received on the subscribed channel
subscriber.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});
