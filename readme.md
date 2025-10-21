# How to run this project
1. Clone this repository
```console
git clone https://github.com/werayco/LLM-Evaluation.git
```
2. Navigate to the wd
```console
cd LLM-Evaluation
```

3. Create a docker netowork
```console
docker network create chatai
```

4. Start the Order Docker Service (Make sure you have Docker Installed)
```console

docker-compose -f app.docker-compose.yml up -d
```

5. Scale the service if you need
```console
docker-compose -f app.docker-compose.yml up --scale gentlepanther=3
```
6. Check the logs of the service
```console
docker logs orderservice --since=10m
```

7. Create an hash value to serve as your UUID (for tracking your conversation)

```console
GET http://localhost:8000/get-uuid?username=xxxx
```

8. Chat with with Agent
```console
POST http://localhost:/api/chat
```
```json
{
  "username": "xxxx",
  "query": "zzzz",
  "hashed_data": "yyyy"
}

```



