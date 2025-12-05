# Function returns a string
def fun(fname: str , lname:str) -> str:
    return fname,lname

print(fun("tony","stark"))

# Functions That Return Nothing (void)

def fun1(message: str ) -> None:
    print(f"Meaasge:{message}")

fun1("koinam")
# Function returns a float
def calculate_tax(tax:float) -> float:
    return tax * 2025

print(calculate_tax(100.23))