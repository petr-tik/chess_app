<aside class="warning">
This is under active development without a working version yet
</aside>

# A flask web-app to organise chess tournaments 


## Run in a Docker container

```bash
docker build -t chess-app .
docker run -p 5000:5000 -it chess-app /bin/sh
```

This runs the test suite and then the app locally under address below
http://127.0.0.1:5000/


## Description

Mockup [here](https://moqups.com/pe3v4/7xozNp9y). The app has 7 views: starting menu, old tournament loader, new tournament creator, round plan and results page, and final table.

Create a tournament with date and location info, choose a scheduling system, input all players and it will generate the rounds, record the results and output running results as well as the final results table, which you can send to all participants. 

In db schema each tournament is created with an INT round_num parameter, which is incremented at the end of every successfully completed round, which allows you to load the last uncompleted round. Any uncompleted round won't be submitted to the db, so you will have to restart again. 


### TO-DO

- [x] round robin schedule algorithm
- [x] tournament creator
- [x] tournament loader screen
- [ ] Update flask to 0.12
- [ ] Move to py3
- [ ] load tournament to latest round 
- [ ] add players to db
- [ ] basic final results template 
- [ ] add send email to final results
- [ ] custom decorator to check last round and render different page
- [ ] implementing swiss schedule algorithm

