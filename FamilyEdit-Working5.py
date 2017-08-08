with open("family-test-file2.txt") as f:
  file = open("Tommy.csv","w")
  a = 0
  a1 = 0
  a2 = 0
  a3 = 0
  a4 = 0
  N1 = []
  N2 = ""
  January = ["1","2","3","4","5"]

  b1 = 0
  b2 = 0

  while a < 1:
    a1 = 0
    a2 = 0
    a3 = 0
    N1 = []
    
    b = 0
    b1 = 0
    #resets variables


    print("loop1")

    while a1 < 1:
    #  print("loop a1")
      c = f.read(1)
    #  print(c)

      if not c:
        print("Done loop A1")
        a1 += 1
        a2 += 1
        a3 += 1
        a += 1  
      #Ends program here because it can't make it up the tree to the final break

      if c == "0":
        c = f.read(3)
      #  print("if1")
      #  print(c)
        if c == " @I":
    #Identifies "0 @I"

          while a2 < 1:
            print("loop a2")
            c = f.read(1)
            if c == "1":
              c = f.read(6)
              if c == " NAME ":  
            #Identifies position of name

                while a3 < 1:
                  print("loop a3")
                  c = f.read(1)
                  N1.extend([c])
                  print(c)
                  print(N1)
                #writes name to N1

                  if c == "/":
                    a4 += 1
                    if a4 >= 2:
                      print("rename")


                      while b < 1:
                        print(N1)
                        if N1[b1] == "/":
                          del N1[b1]
                        
                        b1 += 1
                        if b1 >= len(N1):
                          b += 1
                          N2 = "".join(N1)
                          N1 = []
                          print(N1)
                          print(N2)
                          file.write(N2+",")
                        #Converts name to readable format N2
                        


                      
                      a4 = 0
                      a3 += 1
                      a2 += 1
                      a1 += 1
                    #ends loops after end of name
                       
                  #restarts loops for next name after end of name
                  if not c:
                    print("Done Loop A3")
                    a1 += 1
                    a2 += 1
                    a3 += 1
                    a += 1  
#    while b < 1:
#      print(N1)
#      if N1[b1] == "/":
#        del N1[b2]
#      else:
#        b1 += 1
#      if b1 >= len(N1):
#        b += 1
#        N2 = "".join(N1)
#        N1 = []
#        print(N1)
#        print(N2)
                
            
  f.close()
  print("f Close")
  file.close()
  print("file Close")
