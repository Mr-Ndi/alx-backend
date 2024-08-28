import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Connected to the redis server!')
});

client.on('error', (error) => {
    console.log('Redis client not connected to the server: '+error)
});

(async () => {
    await client.connect();

})();