ydkyb: you don't know your backlog
==================================
a julython 2014 weekend exercise

BACKGROUND:
episode 165 of the idlethumbs podcast jokingly suggested the idea of a "you don't know jack"-style quiz game that presented a random game from a person's Steam game list alongside some games they don't own, and challenged the player to pick which game they owned. the idea being that years of Steam sales and indie bundles have led to everyone's game backlog with hundreds of unplayed games they have no memory of buying.

So I had a sunday afternoon free and three 'Planet of the Apes' movies to watch, and hence decided to exercise my terrible python programming in the form of a flask app to try and do the above.

PRE-REQUISITES
 - This program makes use of the Steam web API. You'll need an API key, which should be placed in the "apikey.txt" file in the base Flask directory. API keys can be easily registered at http://steamcommunity.com/dev/apikey 

TODO
 - Tidy everything up, put it in a proper structure, better cache the all-game-list, make a picture of angry Gabe zoom in closer with each wrong answer.
 - The Steam API is not really very good at supporting their store or catalog. So just using their API, it seems rather hard (if not impossible) to delineate between demos, videos, etc in the all-game-list that gets returned. Need to sort that out!
 - 



