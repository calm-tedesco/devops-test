import asyncio
import requests
import time
import docker

status_api_url = 'http://status-state-api:8080/docker-ps'
r = requests.get(url = status_api_url)
status_state_list = r.json()

async def update_containers():
    client = docker.from_env()
    containers = client.containers.list(True)
    for list_item in containers:
        if list_item.attrs['Id'] in status_state_list:
            print("Container with Id " + list_item.attrs['Id'] + " is in status_state_list")
            if list_item.attrs['State']['Status'] == "exited":
                print("Restarting container with Id " + list_item.attrs['Id'])
                list_item.restart()
        else:
            print("Deleting container " + list_item.attrs['Id'])
            list_item.stop()
            list_item.remove()
            print("Container " + list_item.attrs['Id'] + " deleted")

async def do_stuff_periodically(interval, periodic_function):
    while True:
        await asyncio.gather(
            asyncio.sleep(interval),
            periodic_function(),
        )

asyncio.run(do_stuff_periodically(30, update_containers))
