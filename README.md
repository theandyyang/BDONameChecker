# Black Desert Online Name Checker
Checks if a family/character name is taken using the python module "Twill" for Black Desert Online

This was written in Python 2.7 and requires Twill to be installed. Twill can be found here http://twill.idyll.org/

It checks for names in the North American server, to change it to check in European servers, change the serverName=na to serverName=eu.

It does not check if the name follows DAUM's "Name Validity" rules. Unfortunately, DAUM requires you to login to check if a name is taken or not, which is why your username and password is needed to be entered. 

If you have any idea on how to change this so the user does not have to enter their username and password, throw me a pull request, or message me.






How to use:

1) Make a .txt file of names you would like to check for

2) Have the python script in the same directory as your file of names

3) Run the script

4) Enter filename with the .txt extension

5) Enter username and password

A file, result.txt, will be created containing the results of the test.

