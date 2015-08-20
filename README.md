# Random cool movie

Nothing serious here -- I handpicked a list of movies from various lists such as [RYM film charts](https://rateyourmusic.com/films/chart), [/r/TrueFilm 'Greatest Film' list](https://www.reddit.com/r/TrueFilm/comments/yy9mh/results_of_the_rtruefilm_greatest_film_poll/) and [Sight and Sound](http://explore.bfi.org.uk/sightandsoundpolls/2012/directors/), and compiled them in a text file to pick movies to watch next. However, I decided the thrill of suspense is not maximised this way, and made a quick shell script to pick a random movie... but is it enough? Long story short, I added a SQLite db and a web interface just to be sure.

# Usage

Shell version:

```
$ ./shell_v.py
1966 - "Persona" directed by Ingmar Bergman
```

Web version:
```
$ ./main.py # needs bottle python lib installed in the active environment and runs on localhost:8080
```

# Stuff

* Plaintext file with all the movies available [here](https://github.com/liviu-/random-cool-movie/blob/master/list)
* The code is slapped together super quickly so please don't look at it
* So is the rather terrible db design
* I took the liberty to remove random movies from the lists such as LoTR
* It lacks features such as ticking movies already watched, artworks, links, friendly writing API, etc.
