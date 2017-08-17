with open("family-test-file.txt") as f:
  file = open("Tommy.csv","w")
  a = 0
  a1 = 0
  a2 = 0
  a3 = 0
  a4 = 0

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
      #Saves document to Document
      c = f.read(1)
      Document.extend([c])
      if not c:
        
        a1 += 1
        print("Document imported")
        #print(Document)
        
    while a2 < 1:
      #searches for person
      if Document[DocumentCount] == "0" and Document[DocumentCount + 2] == "@" and Document[DocumentCount + 3] == "I":
      
        while a3 < 1:
          #writes document to PersonProfile
          PersonProfile.extend(Document[DocumentCount])
          DocumentCount += 1
          if DocumentCount >= len(Document):
            #terminates the all loops
            print("end of document")
            #a += 1
            #a2 += 1
            a3 += 1
            a4 = 0
            print("PersonProfile")
            print(PersonProfile)
            #PersonProfile = []

          elif Document[DocumentCount] == "0" and Document[DocumentCount + 2] == "@" and Document[DocumentCount + 3] == "I":
            #prints and resets person profile
            a3 += 1
            a4 = 0
            print("PersonProfile")
            print(PersonProfile)
            #PersonProfile = []
            
          elif Document[DocumentCount] == "0" and Document[DocumentCount + 2] == "@" and Document[DocumentCount + 3] == "F":
            #terminates the all loops
            print("end of person profiles")
            #a += 1
            #a2 += 1
            a3 += 1
            a4 = 0
            print("PersonProfile")
            print(PersonProfile)
            #PersonProfile = []
          
          


        #person identified 

        print("wow")
        #print(Document[DocumentCount])
        PersonCount += 1
        
        DocumentCount += 1
        

        while a4 < 1:
          print("loop A4")
          PersonProfileCount += 1
          if PersonProfileCount >= len(PersonProfile):
            print("length done")
            a1 += 1
            a2 += 1
            a4 += 1
            PersonProfile = []
            PersonProfileCount = 0
          
          if PersonProfile[PersonProfileCount] == "1" and PersonProfile[PersonProfileCount + 2] == "N" and PersonProfile[PersonProfileCount + 3] == "A" and PersonProfile[PersonProfileCount + 4] == "M" and PersonProfile[PersonProfileCount + 5] == "E":
            print("name Found")
            #a += 1
            #a1 += 1
            #a2 += 1
            a4 += 1
            PersonProfile = []
            PersonProfileCount = 0
            a3 = 0
          elif PersonProfileCount >= len(PersonProfile):
            print("name Found else")
            #a += 1
            #a1 += 1
            #a2 += 1
            a4 += 1
            PersonProfile = []
            PersonProfileCount = 0
            a3 = 0

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
