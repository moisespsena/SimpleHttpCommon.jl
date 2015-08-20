# SimpleHttpCommon.jl

**Installation**: `julia> Pkg.add("SimpleHttpCommon")`

This package provides types and helper functions for dealing with the Simple HTTP protocol in Julia:

* types to represent `Request`s, `Response`s, and `Headers`
* a dictionary of `STATUS_CODES`
    (maps integer codes to string descriptions; covers all the codes from the RFCs)
* a bitmask representation of HTTP request methods
* a function to `escapeHTML` in a `String`
* a pair of functions to `encodeURI` and `decodeURI`
* a function to turn a query string from a url into a `Dict{String,String}`