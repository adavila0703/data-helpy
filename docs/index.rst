DBHELPY
=======

dbhelpy is an easy to use Python library that allows you to interact with your sqlite database using dbhelpy methods

Getting Started
***************


Installing::

   pip install dbhelpy

Importing::

    from dbhelpy.dbhelpy import Helpy

Construct Object::

     db = Helpy('database.db')

Basic Concept
*************

*table='cardata'*
.................


+-------+---------------+------------+-----------+
|   id  |  Model        | Color      | Price     |
+=======+===============+============+===========+
|   1   | Mercedes-Benz | White      | $53,950   |
+-------+---------------+------------+-----------+
|   2   | Corvette      | Black      | $58,900   |
+-------+---------------+------------+-----------+

Here is an example of how to use dbhelpy to quickly pull all data from the cardata table above::

    from dbhelpy.dbhelpy import Helpy

    db = Helpy('database.db')

    db.get_all_data('cardata')

Returns::

    [(1, 'Mercedes-Benz', 'White', 53950), (2, 'Corvette', 'Black' , 58900)]

.. toctree::
    :maxdepth: 1

    code