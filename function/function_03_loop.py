# def myname(f_name,l_name):
#     return f"Firstanme: {f_name} and Lastname: {l_name}"

# while True:
#     """wirte firstname amd last"""
#     fname= input("enter firdtname:")
#     lname= input("enter lastname:")

#     if fname == 'q':
#         break
#     if lname == 'q':
#         break

#     a=myname(fname,lname)
#     print(a)

# print("you exit the loop")

def make_album(singer,al_title,no_of_song=None):
    dic={'singer':singer,'al_title':al_title}

    if no_of_song:
        dic['song_of_song']=no_of_song
    return dic


while True:
  """q for quit the loop"""
  artist=  input('Enter singer:')
  album=  input('Enter album:')
  song= input('Enter songs:')

  if artist =='q':
     break
  s= make_album(artist,album,song)
  print(s)




