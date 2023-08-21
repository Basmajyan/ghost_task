For start the back run "docker compose up"
For start the front run "npm i;npm start" in "./front" folder
---
API routing:

    /todo
        methods:
            - get, post(fields: title,status,text)

    /todo/{id} 
        methods:
            - get, patch(fields: title,status,text), delete

    /status - 
        methods:
            - get, post
            
    /status/{id}
        methods:
            - get, patch(fields: status), delete
