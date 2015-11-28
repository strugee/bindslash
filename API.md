# API

## Note

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119 [1].

## Introduction

The bindslash plugin API is extremely simple. Each plugin is simply a Python module installed into a particular directory. Conventionally, plugins are named with the (capitalized) name of whatever they manage, followed by `Plugin`. For example, `FoobarPlugin`.

Each plugin MUST define two functions: `importConfiguration()` and `exportConfiguration()`.

## `importConfiguration(path)`

This function is responsible for importing configuration from the system into a bindslash project. It's passed the path where the plugin is supposed to write data to. Plugins MUST NOT write any data outside of this directory.

## `exportConfiguration(path)`

This function is responsible for exporting configuration stored in a bindslash project back out into the system. It's passed the path where the plugin is supposed to read data from. Plugins SHOULD NOT use as input data not read from this directory.

 [1]: https://tools.ietf.org/html/rfc2119
