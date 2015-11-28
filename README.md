# bindslash

## About

Bindslash (think binding `/` to some port) exists to help you make your system configuration public in a frictionless and non-custom way. On a single system, there is no viable way to make the system configuration public and version-controlled without using some configuration management framework. If you use one of those, you have to write all your stuff for their system. You don't write $service configs, you write configs for $framework's $service plugin. Why all the abstraction for a single server? It doesn't make sense.

So bindslash is not configuration management. It doesn't handle multiple machines. It doesn't have a DSL. It doesn't have a variable store, or a master, or a status dashboard. Instead, you run it once, and it will build a collection of directories that can be used to recreate your setup. If you run it again, it will look at what changed, and sync up. The resulting data can be put anywhere - a tarball, a Git repository, a backup system, or nowhere special at all. Bindslash doesn't care.
