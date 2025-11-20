def args_prnt(func):
    print("decorator set wrapper create , return ")
    def wrapper(*args,**kwargs):
          print(f"position args:{args} And Kwargs c:{kwargs['c']}")
          return func(*args,**kwargs)
    
    return wrapper


@args_prnt             # check=args_prnt(check)
def check(a,b,c=12):
    print("org function")

print("now call wrapper()=check()")
check(1,2,c=34) # when call this right after that check = wrapper so wrapper called


# ✔ args_prnt(func) runs at definition time

# It only:

# receives func

# defines wrapper

# returns wrapper
# (NO PRINT INSIDE WRAPPER EXECUTES YET)

# ✔ wrapper runs at call time

# It:

# prints arguments

# calls original function


# When Python executes:

# test = args_prnt(test)


# It does NOT mean:

# wrapper() is executed


# It means:

# wrapper is CREATED
# wrapper is RETURNED
# test now POINTS to wrapper


# That’s it.