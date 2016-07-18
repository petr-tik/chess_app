## A flask web-app to organise chess tournaments 

Mockup [here](https://moqups.com/pe3v4/7xozNp9y). It will have 6-7 views, allow to load an old or create new chess tournament. 

When all players have been registered, a back end will schedule games according to input rules (round robin or swiss) and produce a live form with a list of games, where results will be entered. 
Calculate and show the table after every round and create an email to send to all attendees (they submit emails) with final results and per-round results.

In db schema each tournament is created with an INT round_num parameter, which is incremented at the end of every successfully completed round, which allows you to load the last uncompleted round. Any uncompleted round won't be submitted to the db, so you will have to restart again. 

## Run

```bash
./run.py
```
and go to address below in your browser
http://127.0.0.1:5000/



### TO-DO

- [ ] load tournament to latest round 
- [x] round robin schedule algorithm
- [ ] tournament loader screen
- [ ] swiss schedule algorithm
- [ ] implementing swiss schedule algorithm
- [ ] basic final results template 
- [ ] add send email to final results
- [ ] custom decorator to check last round and render different page

