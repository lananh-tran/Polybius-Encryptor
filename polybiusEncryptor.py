# extract the Polybius cube coordinate sequence out of the provided text
def textToCoord(text):
  coordSequnc = ""
  
  for char in text:
    # separate case where char is space ' '
    if char == ' ':
      xCoord = 3
      yCoord = 3
      zCoord = 3
    
    # evaluate char using 3 reference points 'a', 'j', 's' on the 3 square layers of the cube
    else:
      zCoord = int((ord(char) - ord('a')) / 9 + 1)
      
      if zCoord == 1:
        yCoord = int((ord(char) - ord('a')) / 3 + 1)
        xCoord = int((ord(char) - ord('a')) % 3 + 1)
      elif zCoord == 2:
        yCoord = int((ord(char) - ord('j')) / 3 + 1)
        xCoord = int((ord(char) - ord('j')) % 3 + 1)
      elif zCoord == 3:
        yCoord = int((ord(char) - ord('s')) / 3 + 1)
        xCoord = int((ord(char) - ord('s')) % 3 + 1)
      else:
        print("Can't encrypt the message. Please make sure you text is in lowercase and only contains normal characters or space.")
        break
    
    # comebine coordinate values into a sequence
    x = str(xCoord)
    y = str(yCoord)
    z = str(zCoord)
    coordSequnc = coordSequnc + x + y + z
    
  return coordSequnc

# process the new coordinate sequence by reading the x, y, z coordinates row-by-row
def coordEncrpt(sequnc):
  prcssdSequnc = ""
  coords = list(sequnc)
  charNum = int(len(sequnc) / 3) # applies for 3D coordinate system
  
  for i in range(0, 3): # Polybius cube -> each triple of digits is a triple of coordinate values of 1 character
    for j in range (0, len(sequnc) - 1, 3): # within sequence, extract coords, step = 3
      coord = int(coords[i + j]) # extract coordinate values "row-by-row"
      prcssdSequnc = prcssdSequnc + str(coord)
  
  return prcssdSequnc

# decipher encrypted sequence and revert them back to original
def coordDecrypt(encrptSequnc):
  prcssdSequnc = ""
  coords = list(encrptSequnc)
  charNum = int(len(encrptSequnc) / 3) # applies for 3D coordinate system

  # the original coordinate triple are positioned charNum away from each other in the encrypted sequnce
  for i in range(0, charNum):
    xNew = int(coords[i])
    yNew = int(coords[i + charNum])
    zNew = int(coords[i + charNum * 2])

    x = str(xNew)
    y = str(yNew)
    z = str(zNew)
    prcssdSequnc = prcssdSequnc + x + y + z

  return prcssdSequnc

# extract new coordinates and turn them into text
def coordToText(sequnc):
  text = ""
  coords = list(sequnc)
  
  # extract every triple and convert to text
  for i in range(0, len(sequnc) - 1, 3):
    xNew = int(coords[i])
    yNew = int(coords[i + 1])
    zNew = int(coords[i + 2])
    
    letterOrd = 3 * (yNew - 1) + xNew + 9 * (zNew - 1) + 96
    letter = chr(letterOrd)
    ch = str(letter)
    text = text + ch
  
  return text
  
message = input("Enter message:   ")
coordSequnc = textToCoord(message)
# print("Extracted sequence: ", coordSequnc)
newCoord = coordEncrpt(coordSequnc)
# print("Encrypted sequence: ", newCoord)
encrpt = coordToText(newCoord)
print("Encrypted text: ", encrpt)

encrptCoord = textToCoord(encrpt)
# print("Extracted sequence: ", encrptCoord)
decrptCoord = coordDecrypt(encrptCoord)
# print("Decrypted sequence: ", decrptCoord)
decrpt = coordToText(decrptCoord)
print("Decrypted text: ", decrpt)
