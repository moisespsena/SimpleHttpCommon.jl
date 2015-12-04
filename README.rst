SimpleHttpCommon.jl
===================

Provides pure Julia API for parser, request, response and utilities for implements your HTTP Server.

.. image:: https://travis-ci.org/moisespsena/SimpleHttpCommon.jl.svg?branch=master
    :target: https://travis-ci.org/moisespsena/SimpleHttpCommon.jl

.. image:: https://coveralls.io/repos/moisespsena/SimpleHttpCommon.jl/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/moisespsena/SimpleHttpCommon.jl?branch=master

.. image:: http://codecov.io/github/moisespsena/SimpleHttpCommon.jl/coverage.svg?branch=master
    :target: http://codecov.io/github/moisespsena/SimpleHttpCommon.jl?branch=master


Install
-------


.. code-block:: julia

    Pkg.clone("https://github.com/moisespsena/SimpleHttpCommon.jl")

    
Usage Example
-------------

.. code-block:: julia

	req_io = IOBuffer()

    write(req_io, "POST /page?getvar=gvalue HTTP/1.1\r\n" *
        "Host: 0.0.0.0:7000\r\n" *
        "Content-Type: application/x-www-form-urlencoded\r\n" *
        "Content-Length: $(sizeof(data))\r\n" *
        "\r\n" *
        "postvar=pvalue&postvar2=pvalue2")

    seekstart(req_io)

    req = Request(IOSocket(req_io))
    init(req, PROTOCOLS)
    data_parsed = parse_data(req)
    


For more and complex examples, See the tests files.