from aiohttp import web
import docker
import json

async def send_docker_ps(request):
    try:
        client = docker.from_env()
        containers = client.containers.list(True)
        containers_dct = {
            containers[i].attrs['Id']: {
                'Name': containers[i].attrs['Name'], 
                'Image': containers[i].attrs['Image'], 
                'Status': containers[i].attrs['State']['Status']
            } for i in range(0, len(containers))}

        return web.json_response(containers_dct, text=None, body=None, status=200, reason=None,
              headers=None, content_type='application/json', dumps=json.dumps)

    except Exception as e:
        print(f'Internal Error: {e}')
        return web.Response(
            text="Internal Error in status-state-api\n",
            status=500
        )

app = web.Application()
app.add_routes([
    web.get('/docker-ps', send_docker_ps)
])

ip = 'status-state-api'
port = 8080

web.run_app(app, host=ip, port=port)

"""
This server is listening for requests on port 8080 (/docker-ps):
http://localhost:8080/docker-ps
"""
