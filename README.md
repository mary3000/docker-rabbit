# docker-rabbit
Example of using rabbitmq with docker-compose. There are 3 services: consumer, producer, and rabbitmq. Producer sends `n` random integers with random delay to the queue, and consumer receives and prints it to the console.

Requirements: docker, docker-compose.

You can simply run `sudo ./run.sh --build` for the 1st time, and `sudo ./run.sh` for the next time.

I'd prefer using python3, but this stupid thing cannot run correctly with it! If you know why, and even know the solution, please tell me!


