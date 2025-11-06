# Key Concepts You Learned Here
# Concept	Meaning
# MRO	The order Python searches classes for methods.
# super()	Goes to the next class in the MRO, not just “the parent.”
# **kwargs	Passes unused parameters through the inheritance chain safely.
# Cooperative Inheritance	Each class calls super().__init__(**kwargs) so every parent runs once.

class A:    
    def __init__(self,name,**kwargs):
        
        self.name=name
    
    def detail(self):
        print(f"Name:{self.name}")
    def findme(self):
        print(f"find Me :{self.name}")

class B:
    def __init__(self,age,**kwargs):
        super().__init__(**kwargs) # pass unused args forward


        self.age=age
        
    def detail(self):
       print(f"this is age:{self.age}")


class C(B,A):
    def __init__(self,name,age):
        super().__init__(name=name,age=age)
                          
    
c=C("aman","22")
c.detail()
c.findme()

# Step 2: Creating the Object

# When you write:

# c = C("aman", "22")


# Python begins by calling:

# C.__init__(self, name="aman", age="22")


# Inside that method, you have:

# super().__init__(name=name, age=age)

# ⚙️ Step 3: super() in C

# super() always means:

# “Go to the next class in the MRO after the current one.”

# In the MRO:

# C → B → A → object


# The next after C is B, so this line:

# super().__init__(name=name, age=age)


# calls:

# B.__init__(self, age="22", name="aman")

# ⚙️ Step 4: Inside B.__init__()

# Definition:

# def __init__(self, age, **kwargs):
#     super().__init__(**kwargs)
#     self.age = age


# Now, the values coming in are:

# age="22"

# **kwargs={"name": "aman"}

# So inside B.__init__:

# super().__init__(**kwargs)
# becomes → super().__init__(name="aman")

# Then it calls the next class in MRO after B, which is A.

# ⚙️ Step 5: Inside A.__init__()

# Definition:

# def __init__(self, name, **kwargs):
#     super().__init__(**kwargs)
#     self.name = name


# Now, the values passed are:

# name="aman"

# **kwargs={} (nothing left)

# So inside A.__init__:

# It calls super().__init__(**kwargs) → super().__init__()
# → goes to next class in MRO after A, which is object
# → object.__init__() does nothing, returns.

# Then self.name = name runs.

# 🧩 Step 6: Backtracking (Return Path)

# The call stack unwinds:

# object.__init__() finishes

# Returns to A.__init__() → sets self.name

# Returns to B.__init__() → sets self.age

# Returns to C.__init__() → done.

# ✅ Object is fully created with:

# c.name = "aman"
# c.age = "22"