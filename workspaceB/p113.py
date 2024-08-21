def p(space,space_num,*args): #arguments ,인수
    str=""
    for i in range(len(args)):#(0,1,2,3,4,5)
        str=str+args[i]
        print(str)
  

 
p(',',3,'💕','👌','❤️','😒','🤣','😍')
p('t',3,'x','y','z')