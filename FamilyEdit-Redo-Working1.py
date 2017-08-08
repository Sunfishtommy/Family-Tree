with open("family-test-file2.txt") as f:
  file = open("Tommy.csv","w")
  a = 0
  a1 = 0
  a2 = 0
  a3 = 0

  Document = []
  DocumentCount = 0
  PersonCount = 0
  PersonProfile = []
  PersonProfileCount = 0
  NameLetter = []
  NameCount = 0


  while a < 1:


    print("loop1")

    while a1 < 1:
      c = f.read(1)
      Document.extend([c])
      if not c:
        
        a1 += 1
        print(Document)
        
    while a2 < 1:
      #searches for person
      if Document[DocumentCount] == "0" and Document[DocumentCount + 2] == "@" and Document[DocumentCount + 3] == "I":

        #person identified 

        print("wow")
        print(Document[DocumentCount])
        PersonCount += 1
        
        DocumentCount += 1
        

      else:
        DocumentCount += 1
        #print("loop a2")

        if DocumentCount >= len(Document):
        #terminates the document count loop progressing through Document List.
          a += 1
          a2 += 1
          
          print(PersonCount)
          print(NameCount)


          
            
  f.close()
  print("f Close")
  file.close()
  print("file Close")
