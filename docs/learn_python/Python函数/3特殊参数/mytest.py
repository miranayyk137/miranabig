def mytest(aaa, *bbb, **ccc):
    print("-- Do you have any", aaa, "?")
    print("-- I'm sorry, we're all out of", aaa)
    for b in bbb:
        print(b)
    print("-" * 40)
    for c in ccc:
        print(c, ":", ccc[c])


mytest("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           a="Michael Palin",
           b="John Cleese",
           c="Cheese Shop Sketch")
