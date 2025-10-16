# learning_kestra
## Kestra and Docker test using python
This project uses basic functionalites of python to test Kestra and Docker. The main propose is to 
learn automation with python

 **Prerequisites:**
- Docker e Docker Desktop instalados
- WSL 2 configurado no Windows

## How to use the project
1. Clone the project
```Bash
git clone https://github.com/Albuquerque07/learning_kestra.git
cd learning_kestra
```

2. Initialize Docker compose:
```Bash
docker-compose up -d
```

3. Acess Kestra interface with `http://localhost:8080`

4. Execute Workflow
- Go to the "Flows" section
- Search "firstContact" project
- Click on "New execution" to execute it