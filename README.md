# Anakonda Project
This is a container-based task runner to run user tasks in Docker and Kubernetes.
Simple API with Flask web framework

```bash
docker-compose -f docker-compose.base.yaml -f docker-compose.test.yaml up --build --abort-on-container-exit --exit-code-from anakonda
```