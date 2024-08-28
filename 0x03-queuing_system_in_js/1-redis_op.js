import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('error', (error) => {
    console.log('Redis client not connected to the server: '+error)
});

(async () => {
    await client.connect();
    function setNewSchool(schoolName, value) {
        client.set(schoolName, value, redis.print);
    }
        
    function displaySchoolValue(schoolName) {
        const value = client.get(schoolName, (error, value) => {
            if (error) {
                console.error('Error retrieving value:', error);
            }else {
                console.log(`Value for ${schoolName}: ${value}`);
            }
        });
    }

        await client.quit();

})();
