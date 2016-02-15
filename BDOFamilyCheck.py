import re
from twill.commands import *

fileName = raw_input('Enter file name: ');
try:
	with open(fileName) as f:
		names = f.readlines();
except:
	print("File not found");
	exit(0);

for i in range(len(names)):
	names[i] = names[i].strip('\n');

go('https://www.blackdesertonline.com/account/login')
email = raw_input('Enter Email: ');
pw = raw_input('Enter Password: ')
fv("1", "email", email);
fv("1", "password", pw);

submit();
result = []

z = open("result.txt", 'w');

go("https://www.blackdesertonline.com/shop/preorder/namereservation/AJAXIsExistFamilyName.json?serverName=na&familyName=Test");
n = show();
a = re.search("USER__NOT_LOGIN", n);
if(a != None):
	z.write("Failed to login");
	exit();

z.write("Available Family Names:\n");

for i in range(len(names)):
	go('https://www.blackdesertonline.com/shop/preorder/namereservation/AJAXIsExistFamilyName.json?serverName=na&familyName=' + names[i])
	s = show();
	m = re.search('true', s);
	if(m == None):
		result.insert(i, names[i]);

for k in result:
	z.write("%s\n" % k);

