# 🐳 Docker Cheat Sheet – DevNet Lab Edition

## ⚙️ Common Docker Commands
```bash
# Version and install check
docker --version

# Run a test container
docker run hello-world

# List all containers (running or not)
docker ps -a

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# Pull image from Docker Hub
docker pull python

# Run Python container interactively
docker run -it python

# Run a Flask app and map port
docker run -p 5000:5000 flask
```

---

## 🧱 Docker Concepts
- **Image**: Blueprint for containers
- **Container**: Running instance of an image
- **Volume**: Persistent storage between container runs
- **Port Mapping**: Expose app ports to your host machine

---

## 🧪 DevNet Use Cases
- Run test APIs in containers
- Build isolated Python scripts for network automation
- Emulate network environments for safe lab testing

---

## 🧠 Pro Tips
- Clean up unused containers/images:
```bash
docker system prune -a
```
- Use `docker-compose` for multi-container DevNet apps
- Mount project folders for live edits in containers

---

## 📝 Personal Notes
