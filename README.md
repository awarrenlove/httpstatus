# httpstatus - Simple HTTP Status Codes

`httpstatus` was initially created as a pull request for the avinassh/status project to allow pairing a human-readable string with the status codes, but the owner of that project didn't want to move away from literal ints as constants. Since I didn't want this code to die, I decided to create my own project.

This project is simply a module with helper constants to represent HTTP status codes. For now, I only included standardized ones, but I am considering including other well-known codes used in popular libraries as well. The class included in the module is not meant to be used directly, but instead is simply to provide an object that can be coerced to an int when a literal is needed or a string when a prettier, human-readable string is preferred.
