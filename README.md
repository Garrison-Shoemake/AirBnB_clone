# AirBnB Console
This is the console portion of the AirBnB Clone project and will be used in future AirBnB Clone projects. In this console, we are able to put in place a parent class named `BaseModel` which handles initialization, serialization, and deserialization of the classes inherited from it: `User`, `State`, `City`, `Amenity`, `Place`, and `Review`. Included in the console is our first storage engine for the project as well as unit tests for each class and for the console itself. 

***

## Command Interpreter
The command interpreter for the console takes varying arguments as input from the user and executes processing based on that input. The console is an executable `.py` file and can be started with the command `./console.py` in your local terminal. After starting the console, it should look like this:

    root@c05fbf18ea24:~/AirBnB_clone# ./console.py
    (hbnb)

From here you may call any of the following commands, including the information you want to :

| Command | Example | Result |
| --- | --- | --- |
|
|`quit`| `(hbnb) quit` | Exit's the program. This is the same as using `ctrl+d`
|`help` | `(hbnb) help <command>` | Displays help message for `<command>`
|`create`| `(hbnb) create <class name>` | Creates a new instance of class `class name` and prints its unique `id`
|`show`| `(hbnb) show <class name> <id>`| Prints a string representation of class `class name` and its unique `id`
|`destroy`| `(hbnb) show <class name> <id>`| Deletes class `class name` with `id` given
|`all`|`(hbnb) all` or `(hbnb) all <class name>`| Shows all classes of `class name`, otherwise, shows all classes in storage | 
|`update`| `(hbnb) update <class name> <id> <attribute name> <attribute value>`| Updates class `class name` with `id` to update that instance's `attribute name` to be `attribute value`. If that instance does not have `attribute name`, it will be created and initialized with `attribute value`

You are also able to format the following commands with similar input as above:

|Command|Example|
| --- | --- |
|`all`|`(hbnb) <class name>.all()`
|`count`|`(hbnb) <class name>.count()`, which returns the total number of `<class name>`
|`show`| `<class name>.show(<id>)`
|`destroy`| `<class name>.destroy(<id>)`
|`update`| `<class name>.update(<id>, <attribute name>, <attribute value>)`

In all examples shown above, if any information is missing or incorrect, the console will return a message noting the error encountered. Included in this project is our FileStorage, which is where the information created or updated is stored, via class inheritance and dictionaries. 