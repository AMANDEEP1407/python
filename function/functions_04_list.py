# def show_message(shorts_mes):
#     for s in shorts_mes:
#         print(s)

# short_mes=['this is first','this is second','this is third','this is fourth']
# show_message(short_mes)
new_list=[]
def send_message(short_mes):
    while short_mes:
       newlist= short_mes.pop()
       new_list.append(newlist)

    
   


short_mes=['this is first','this is second','this is third','this is fourth']
send_message(short_mes[:])   # send a copy, so original list is unchanged
print(short_mes)
print(new_list)