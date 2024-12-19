### Как запустить:
1. install `pydantic`, `uvicorn` and `FastAPI`: `pip install pydantic uvicorn fastapi`<br>
2. run command `uvicorn main:app --reload`<br>


### Handlers usage 
#### Create
POST request for /create 
```
fetch('http://127.0.0.1:8000/create', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify({
        Concept: 'CodeSplitting', 
        Definition: 'A technique used to optimize the performance of UI libraries by loading components or their dependencies only when needed, reducing the initial load time and improving user experience.' 
    })
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error)); 
```

#### Update
PUT request for /update/{definition}
Replace {definition} with definition name
```
fetch('http://127.0.0.1:8000/update/CodeSplitting', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify({
        NewDefinition: '[CHANGE] A technique to load parts of an application or UI library on demand, improving performance by reducing initial load time.' 
    })
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error));
```

#### Remove
DELETE request for /remove/{definition
Replace {definition} with definition name
```
fetch('http://127.0.0.1:8000/remove/CodeSplitting', {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json', 
    }
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error));
```
