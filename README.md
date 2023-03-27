### Description
This project is intended to help me interact with my local movies scattered on my hard drives
 , but structured somewhat correctly.  

The project presumes this directory structure:
- The main directories found inside each hard drive should be listed inside disks as a json dict[name:location].  
- These folder will be checked inside each main directory
  - `Movies`: Contains full-featured or short films
    - `Directors`: Contains a list of dirs named after film directors.
    - r`^(19[0-9]0|20[0-9]0)s$`: This is a directory named after a decade e.g. 1960s.
  - `Movie Series`: Contains a list of dirs, each of which represents a film series e.g. Kung fu Panda.
  - `TV Series`: Contains a list of dirs, each of which represent a TV Series.
  - `Stand-Up Comedy`: Contains a list of dirs representing stand-up comedians. Each dir contains a list of comedy specials.

Each film directory name syntax should follows this rule:  

- `[release year] - [film title] - [file quality and ripper]`
- e.g. `2008 - Kung Fu Panda 1 - 1080p BRrip 264fps YIFY`

There are two subcommands:

- `randfilm`: loads list of movies and prints one at random.
  - `python3 main.py randfilm`
- `findfilm`: loads list of movies and locates input text.
  - `python3 main.py findfilm --subtitle "Panda"`
  - `python3 main.py findfilm -t "Panda"`
  - argument search through movie title is case-***in***sensitive.

### TODOS
- write todos
