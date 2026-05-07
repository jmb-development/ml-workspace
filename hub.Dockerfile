FROM quay.io/jupyterhub/jupyterhub:5

# DockerSpawner creates per-user containers on the fly
# NativeAuthenticator gives us a simple username/password admin UI
RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-nativeauthenticator
