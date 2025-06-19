import docker
client = docker.from_env() # Create a Docker client instance

# List Docker containers :
containers = client.containers.list()
for container in containers :
    print(container.name)
    
# Pull a Docker image :
client.images.pull('nginx:latest')

# Create and run a Docker container :
container = client.containers.run('nginx:latest', detach=True, ports={"80/tcp":8080})