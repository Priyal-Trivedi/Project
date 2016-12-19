Front-end - Methods Business Logic
==================================

This component contains all the details on business logic of all the methods.

Design
------

This is the main page and renders the :py:class:`frontend.forms.DesignChoiceForm` for user to choose following.

 * Problem Type
 * Domain
 * TBL Scope

.. figure:: resources/design_choice.png
   :align: center

Once user selects it, every click on the arrow button takes user to the next step. For each click following function is called
on the backend which saves user data and takes user to the appropriate next step.

.. function:: next_step(request)
   :module: frontend.views

Contribute
----------


Data
----

Terminology
-----------

.. function:: terminology(request)
   :module: frontend.views

Renders terminology html page.


Reset User Progress
-------------------

.. function:: reset(request)
   :module: frontend.views

Resets user progress.
 * Sets step_reached to 0
 * Sets tbl scope, domain and problem type to None and saves the user object.

