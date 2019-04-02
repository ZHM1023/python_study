
var01 = ord("a")
print(var01)
print("#*#"*20)

var02 = ord("b")
print(var02, type(var02))

var03 = chr(97)
print(var03, type(var03))

var04 = "A BB CCC"
print(var04)
var04_new = var04.replace("A", "a")
print(var04_new)

var05 = var04_new.replace("C", "b")
print(var05)

var06 = var04 + " " + var05
print("var06: ", var06)

var07 = "ABB"
var08 = "ccc"

var09 = var07.replace(var08, "")
print(var09)


