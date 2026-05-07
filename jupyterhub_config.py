import os

# ── Spawner ────────────────────────────────────────────────────────────────────
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# The notebook image built from notebook.Dockerfile
c.DockerSpawner.image = "ml-notebook:latest"

# Put every spawned container on the same network as ray-head
c.DockerSpawner.network_name = os.environ.get("DOCKER_NETWORK_NAME", "ml-net")
c.DockerSpawner.use_internal_ip = True

# Clean up the container when the user's server stops.
# It will be re-created (from the same image) on next login.
c.DockerSpawner.remove = True

# Persistent work directory per user — Docker named volume, auto-created on first login.
# Adding a new user requires zero manual volume setup.
c.DockerSpawner.volumes = {
    "jupyterhub-user-{username}": "/home/jovyan/work"
}

# Every notebook container knows how to talk to Ray
c.DockerSpawner.environment = {
    "RAY_ADDRESS": os.environ.get("RAY_ADDRESS", "ray://ray-head:10001")
}

# ── Hub networking (so spawned containers can phone home) ──────────────────────
# Spawned containers reach the Hub API via the service name on ml-net
c.JupyterHub.hub_connect_ip = "jupyterhub"

# ── Authentication ─────────────────────────────────────────────────────────────
c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# Users cannot self-register — an admin must create their account
c.NativeAuthenticator.open_signup = False

# Bootstrap: the first admin. Add yourself here. You can promote others in the UI.
c.Authenticator.admin_users = {"john"}

# Admins can open any user's notebook for debugging
c.JupyterHub.admin_access = True

# ── Database (persisted in the jupyterhub-data volume) ────────────────────────
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
