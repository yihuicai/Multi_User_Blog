1.How to use the file:
  a:Download Google App Engine SDK.
  b:open the command line, direct to the folder where main.py is.
  c:Execute " dev_appserver.py . "in command line.

2.Structure:

  a: In the Handler folder, there are many classes. Each of them except Handler deals with a request.
  b: The Handler class stores functions that include jinja template methods to render a page. Also it includes different helper functions including authentication functions.
  c: In the Model folder, there are classes that deals with data structures including Account, Comment and Message. Each of them refers to a spcecific database that can let the user update information.