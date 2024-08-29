import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Loop through the jobs array and create jobs in the queue
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Handle job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Handle job failure
    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    // Handle job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    // Enter test mode
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).toThrow('Jobs is not an array');
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate that the jobs are in the queue
    const jobIds = queue.testMode.jobs;
    expect(jobIds.length).toBe(2);
    expect(jobIds[0].data).toEqual(jobs[0]);
    expect(jobIds[1].data).toEqual(jobs[1]);
  });

  it('should log the correct messages for job events', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account'
      }
    ];

    // Spy on console.log to capture log messages
    const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

    createPushNotificationsJobs(jobs, queue);

    // Wait for the job to be processed
    queue.process('push_notification_code_3', (job, done) => {
      done(); // Mark job as complete
    });

    setImmediate(() => {
      expect(consoleSpy).toHaveBeenCalledWith(expect.stringMatching(/Notification job created:/));
      expect(consoleSpy).toHaveBeenCalledWith(expect.stringMatching(/Notification job/));
      consoleSpy.mockRestore(); // Restore the original console.log
      done();
    });
  });
});

export default createPushNotificationsJobs;