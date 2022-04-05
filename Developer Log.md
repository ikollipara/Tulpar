# Tulpar Developer Log

## 2022.04.04

I've decided to move the project to a different name, as the last one was taken. I've also decided that each piece of Tulpar - the cli, framework, and DSL - will be separate packages. This allows me to version differently and work on each independently. Given that, this is just the framework developer log now.

### Testing
I've been able to test most of the classes, but not the main one yet. This is due to the dependence on the config existing. 

### Pages
I've been thinking that pages would be well served by being just a render function. As in, pages should only implement a get, and take dependencies. As such, I can just write a decorator that creates a class that implements the get method. This approach would work well with the DSL as well.


## 2022.04.05
I've finished documenting what is currently in the framework. My next concern is where I should include service files, or should I have those at all. I think having a dedicated folder would be nice for services, as some things just don't belong in the view parts of the function. It also allows for some DRY principles as well. 