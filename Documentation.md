(in progress)

# Background

The following information is directly copied from [Wikipedia](https://en.wikipedia.org/wiki/Polybius_square).

This is a typical form of a 5x5 Polybius square:

![ảnh](https://github.com/lananh-tran/Polybius-Encryptor/assets/118518981/91187f86-12ba-4152-b907-b368fc5a6f13)

The message is transformed into coordinates on the Polybius square, and the coordinates are recorded vertically:

![ảnh](https://github.com/lananh-tran/Polybius-Encryptor/assets/118518981/cd43437a-d086-417c-8776-bdb4659d5ba3)

Then the coordinates are read row by row: 34  25  45  34  43  31  41  54

Next, the coordinates are converted into letters using the same square:

![ảnh](https://github.com/lananh-tran/Polybius-Encryptor/assets/118518981/a1e758e2-a3f7-4e99-ab4b-a1367a6d6f61)

Thus, after encryption, we get:

![ảnh](https://github.com/lananh-tran/Polybius-Encryptor/assets/118518981/a6eb9a9e-5139-43d3-8e9f-38335fed28cd)

# The Polybius cube

This is the structure of my Polybius cube, with each character having its corresponding set of coordinates (x, y, z):

![ảnh](https://github.com/lananh-tran/Polybius-Encryptor/assets/118518981/bec8f3ff-34f5-46da-9dad-52d8eab4fceb)

![ảnh](https://github.com/lananh-tran/Polybius-Encryptor/assets/118518981/92b35189-e7dd-44fd-ab72-0ac8d90ef251)

## Text to Coordinates

When the user enters a text, the program will start to extract the corresponding Polybius cube coordinates of each character with the textToCoord() function based on the character ASCII code. The z-coordinate is calculated using the following function, since a character in a higher z-level, with the same Oxy coordinates, is its previous counterpart in the lower z-level adding 9. For instance, the ASCII value for 'a' = (1, 1, 1) is 97, and 'j' = (1, 1, 2) is located right above 'a', has the ASCII value of 106.

```zCoord = int((ord(char) - ord('a')) / 9 + 1)```

Next, the x and y-coordinate are calculated by the following formulae, with the reference character being the first character in every z-level. This is because the y-coordinate depends on a character's distance away from its reference point, and the x-coordinate depends on the remainder in the division of this distance with 3, which is the size of the square.

```
yCoord = int((ord(char) - ord('a')) / 3 + 1)
xCoord = int((ord(char) - ord('a')) % 3 + 1)
```

## Coordinates to Text

To convert a sequence of coordinates, with every set of (x, y, z) positioned next to each other correspondingly, the formula below was used. This is due to the fact that when moving from one 1x1x1 cube to another within our Polybius cube, we need an increment of 1 to increase 1 in the x-value, an increment of 3 to increase 1 in the y-value, and an increment of 9 to increase 1 in the z-value. The number 96 accounts for the ASCII value of 'a' = 97, and that we are counting from 0.

```letterOrd = 3 * (yNew - 1) + xNew + 9 * (zNew - 1) + 96```

## Encryption

We need to process the obtained sequence so that it appears as if it was read row-by-row. For example, take the (x, y) coordinate sequence of the word "some": 113322122221. We want to obtain the new sequence: 131212223221. This can be done by combining the first digit with the digit first, second, and third digit 3 steps away from it. Therefore, 2 for-loops were implemented to group the digits 3 steps away from each other, from left to right.

```
for i in range(0, 3):
    for j in range (0, len(sequnc) - 1, 3):
      coord = int(coords[i + j]) # extract coordinate values "row-by-row"
      prcssdSequnc = prcssdSequnc + str(coord)
```

## Decryption

To revert the processed sequence back to its original form, notice that each coordinate value is n steps away from the other coordinate values in its original set, with n being the number of letters in our original text. All we have to do is to extract these sets, and put them next to each other to obtain the original sequence.

```
for i in range(0, charNum):
    xNew = int(coords[i])
    yNew = int(coords[i + charNum])
    zNew = int(coords[i + charNum * 2])
```
