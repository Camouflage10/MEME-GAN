# Import Statements
from asyncio.windows_events import NULL
from calendar import firstweekday
from fileinput import filename
from PIL import Image, ImageFont, ImageDraw

import memeDict

def getTextDim (textStr, font) :
    ascent, descent = font.getmetrics()
    textW = font.getmask (textStr).getbbox ()[2]
    textH = font.getmask (textStr).getbbox ()[3] + descent
    print ("Text Width in function: ", textW)
    return (textW, textH)

def findSpaces (text) :
    print ("Inside findSpaces: " + text)
    textLen = len (text)
    print ("Text Length: ", textLen)
    spacesList = []
    for element in range (0, textLen) :
        if text [element] == ' ' :
            spacesList.append (element)
    spaceListLen = len (spacesList)
    return textLen, spacesList, spaceListLen

class textBlock :

    def __init__ (self, text, fontSize, font): 

        # Top Text
        self.text = text
        self.fontSize = fontSize
        self.font = font
        self.prepareText (text, fontSize, font)

    # Functions


    def findSpaces (self, text) :
        textLen = len (text)
        print ("Text Length: ", textLen)
        spacesList = []
        for element in range (0, textLen) :
            if text [element] == ' ' :
                spacesList.append (element)
        return textLen, spacesList

    def splitStr (self, text, textLen, spacesIndex) :

        str1 = ""
        str2 = ""
        print (str1)
        print (str2)

        place = len (spacesIndex) / 2
        dividePoint = spacesIndex [int(place)]
        print ("\n\n DIVIDE POINT")
        print (dividePoint)          
        print ("\n\n")
        for element in range (0, dividePoint) :
            str1 = str1 + text [element]
        for element in range (dividePoint + 1, textLen) :
            str2 = str2 + text [element]
        print (str1)
        print (str2)
        return

    def prepareText (self, text, fontSize, font) :


        if (textLen > 24) :
            textLen, spacesIn = self.findSpaces (text)
            print ("The spaces are at: ", spacesIn)
            str1, str2 = self.splitStr (text, textLen, font)
            text1W, text1H = self.getTextDim (text, font)
            print ("Width: ", text1W)
            print ("Height: ", text1H)
            adjustText (imageWidth)

        # adjust text here

        return



    def adjustText (self, imageWidth, text, textWidth, textLen, font, fontSize, spacesIndex) :

        print ("Adjusting the text")
        print ("passtrhoughs:")
        print (imageWidth, text, textWidth, textLen, font, fontSize, spacesIndex)
        print ("--------------------------------------------\n\n")

# Splitting the two strings

        # Adjusting the sizes of the first and second strings

        str1Len = len (self.str1)
        str2Len = len (self.str2)

        str1W, str1H = self.getTextDim (self.str1, self.font)
        str2W, str2H = self.getTextDim (self.str2, self.font)     

        if (textLen > 24) :
            place = len (self.spacesIndex) / 2
            dividePoint = self.spacesIndex [int(place)]
            print ("\n\n DIVIDE POINT")
            print (dividePoint)          
            print ("\n\n")

            for element in range (0, dividePoint) :
                self.str1 = self.str1 + self.text [element]
            for element in range (dividePoint + 1, textLen) :
                self.str2 = self.str2 + self.text [element]
            print (self.str1)
            print (self.str2)

            # Adjusting the sizes of the first and second strings

            str1Len = len (self.str1)
            str2Len = len (self.str2)

            self.str1W, self.str1H = self.getTextDim (self.str1, font)
            self.str2W, self.str2H = self.getTextDim (self.str2, font)      
            
            # First String Check
            if (str1Len <= 24) :
                if ((self.str1W + 10) < imageWidth) :
                    while (((self.str1W + 10) * 1.2) < imageWidth) :
                        print ("expand")
                        fontSize = int (fontSize) * 1.2
                        font = ImageFont.truetype ('impact.ttf', int (fontSize))
                        self.str1W, str1H = self.getTextDim (self.str1, font)
                # Is text to big?
                # Shrink Text
                elif (self.str1W >= imageWidth) :
                    while (self.str1W >= imageWidth) :
                        print ("shrink")
                        fontSize = int (fontSize) * .9
                        font = ImageFont.truetype ('impact.ttf', int (fontSize))
                        self.str1W, self.str1H = self.getTextDim (self.str1, font)
                
            # Second String Check
            if (str2Len <= 24) :
                if ((self.str2W + 10) < imageWidth) :
                    while (((self.str2W + 10) * 1.2) < imageWidth) :
                        print ("expand")
                        fontSize = int (fontSize) * 1.2
                        font = ImageFont.truetype ('impact.ttf', int (fontSize))
                        self.str2W, self.str2H = self.getTextDim (self.str2, font)
                # Is text to big?
                # Shrink Text
                elif (self.str2W >= imageWidth) :
                    while (self.str2W >= imageWidth) :
                        print ("shrink")
                        fontSize = int (fontSize) * .9
                        font = ImageFont.truetype ('impact.ttf', int (fontSize))
                        self.str2W, self.str2H = self.getTextDim (self.str2, font)

            return font, self.str1W, self.str1, self.str2


# No String Splitting

        # Is text to small?            
        if (textLen <= 24) :
            if ((textWidth + 10) < imageWidth) :
                while (((textWidth + 10) * 1.2) < imageWidth) :
                    print ("expand")
                    fontSize = int (fontSize) * 1.2
                    font = ImageFont.truetype ('impact.ttf', int (fontSize))
                    textWidth, textHeight = self.getTextDim (text, font)
                return font, textWidth, text, ""
            # Is text to big?
            # Shrink Text
            elif (textWidth >= imageWidth) :
                while (textWidth >= imageWidth) :
                    print ("shrink")
                    fontSize = int (fontSize) * .9
                    font = ImageFont.truetype ('impact.ttf', int (fontSize))
                    textWidth, textHeight = self.getTextDim (text, font)
            return font, textWidth, text, ""

# Gather Materials





# # Text Objects
# print ("\nTop Obj")
# top = textBlock ("Oh Come my little children", 100, ImageFont.truetype ('impact.ttf', defaultFontSize))
# print ("\nBot Obj")
# bot = textBlock ("I have candy", 100, ImageFont.truetype ('impact.ttf', defaultFontSize))


# Fitting the Text
# def adjustText (imageWidth, text, textWidth, textLen, font, fontSize, SpacesIndex) :

# print ("\nAdjusting Top: ")
# top.font, top.textW, top.str1, top.str2 = top.adjustText (imageWidth, top.text, top.textW, top.textLen, top.font, top.fontSize, top.spacesIndex)
# print ("\nAdjusting Bottom: ")
# bot.font, bot.textW, bot.str1, bot.str2 = bot.adjustText (imageWidth, bot.text, bot.textW, bot.textLen, bot.font, bot.fontSize, bot.spacesIndex)

# if (textW > imageWidth) :
#     fontSize = int (fontSize) / 2
#     font = ImageFont.truetype ('impact.ttf', int (fontSize))

# topOffset = ((imageWidth - top.textW) / 2)
# topOffset2= ((imageWidth - top.textW) / 2)

# botOffset = ((imageWidth - bot.textW) / 2)
# botOffset2 = ((imageWidth - top.textW) / 2)



# drawer.text ((topOffset, 10), top.text, font = top.font, fill = textColor, stroke_width = borderSize, stroke_fill = borderColor, align = 'center')

# drawer.text ((botOffset, imageHeight - bot.textH - 25), bot.text, font = bot.font, fill = textColor, stroke_width = borderSize, stroke_fill = borderColor, align = 'center')






# drawer.text ((memeDict.drake [""], 1))


print ("What type of meme do you want?")
getInput = int (input ("Press \"1\" for drake meme\nPress \"2\" for button meme\nChoice: "))

if (getInput == 1) :
    memeType = "drake"
    tempDict = memeDict.drake
else :
    memeType = "button"
    tempDict = memeDict.button


numTexts = tempDict.get ("numTexts")

# XL, XR, YT, YB
meme2DArray = [[], [], [], []]

meme2DArray [0] = tempDict.get ("xBorder_L") # Left
meme2DArray [1] = tempDict.get ("xBorder_R") # Right
meme2DArray [2] = tempDict.get ("yBorder_T") # Top
meme2DArray [3] = tempDict.get ("yBorder_B") # Bot

print (meme2DArray)

# Get Image and Text Components Ready
image = Image.open (tempDict ["fileName"])
imageWidth, imageHeight = image.size
print ("Width: ", imageWidth)
print ("Height: ", imageHeight)
textColor = "#FFFFFF"
borderColor = "#000000"
borderSize = 4
defaultFontSize = 100

startingFontSize = tempDict.get ("startingFont")

startingFont = ImageFont.truetype ('impact.ttf', int (startingFontSize))

# Get Strings Ready
strInput = []
strFontSize = []
for i in range (numTexts) :
    temp = input ("Enter meme text for block #" + str(i) + ": ")
    strInput.append ([temp])
    # First List is the list of each line of the meme text, second list will be the size for that 
    strFontSize.append (defaultFontSize)
print (strInput)
print (strFontSize)

# Resize All Text
for i in range (numTexts) :
    frameW = meme2DArray [1] [i] - meme2DArray [0] [i]
    frameH = meme2DArray [3] [i] - meme2DArray [2] [i]


    textLen, spacesList, spaceListLen = findSpaces (strInput [i] [0])
    print ("Spaces stuff: ", textLen, spacesList, spaceListLen)

    while (True) :
        for j in range (len (strInput [i])) :

            tempW, tempH = getTextDim (strInput [j], strFontSize [i])

            # Too Small
            if (tempW > frameW) :

                print ("Too Small")

                print (strFontSize [i])

                strFontSize [i] = 1.1 * strFontSize [i]

                print (strFontSize [i])

                break

            # Too Tall
            elif (tempH < frameH) :
                print ("Too Tall")

            # Too Long 
            elif (tempW < frameW) :
                print ("Too Long")

            # If Perfect
            else :
                print ("Perfect")
                break

# for i in range (numTexts) :

#     tempStrW, tempStrH = getTextDim (strInput, startingFont)





# Make Meme
image_editable = ImageDraw.Draw (image)

drawer = ImageDraw.Draw (image)

for i in range (numTexts) :
    print ("For loop iteration: ", i)

    temp = len (strInput [i])
    for j in range (temp) :
        drawer.text ((meme2DArray [0] [i], meme2DArray [2] [i]), strInput [i] [j], font = startingFont, fill = textColor, stroke_width = borderSize, stroke_fill = borderColor, align = 'center')

image.save ("result2.jpg")
