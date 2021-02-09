# Django ElasticSearch Demo
--- 

Populate .env with ElasticSearch credentials and secret key
   
### Run
 > docker-compose up

### Other useful commands
 > Index elasticsearch from all database models
 
 `python manage.py search_index --rebuild`