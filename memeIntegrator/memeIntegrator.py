# Import Statements
from PIL import Image, ImageFont, ImageDraw


class textBlock :

    def __init__ (self, text, fontSize, font): 

        # Top Text
        self.text = text
        self.fontSize = fontSize
        self.font = font
        self.textW, self.textH, self.textLen, self.spacesIndex = self.prepareText (text, fontSize, font)

    # Functions
    def getTextDim (self, textStr, font) :
        ascent, descent = font.getmetrics()
        textW = font.getmask (textStr).getbbox ()[2]
        textH = font.getmask (textStr).getbbox ()[3] + descent
        print ("Text Width in function: ", textW)
        return (textW, textH)

    def findSpaces (self, text) :
        textLen = len (text)
        print ("Text Length: ", textLen)
        spacesList = []
        for element in range (0, textLen) :
            if text [element] == ' ' :
                spacesList.append (element)
        return textLen, spacesList

    def prepareText (self, text, fontSize, font) :
        textW, textH = self.getTextDim (text, font)
        print ("Width: ", textW)
        print ("Height: ", textH)
        textLen, spacesIn = self.findSpaces (text)
        print ("The spaces are at: ", spacesIn)
        return textW, textH, textLen, spacesIn

    def adjustText (self, imageWidth, text, textWidth, textLen, font, fontSize, SpacesIndex) :
        print ("Adjusting the text")
        print ("passtrhoughs:")
        print (imageWidth, text, textWidth, textLen, font, fontSize, SpacesIndex)
        # Is text to small?
        if ((textLen <= 24) & (textWidth + 10) < imageWidth) :
            while (((textWidth + 10) * 1.2) < imageWidth) :
                print ("expand")
                fontSize = int (fontSize) * 1.2
                font = ImageFont.truetype ('impact.ttf', int (fontSize))
                textWidth, textHeight = self.getTextDim (text, font)
            return font, textWidth
        # Is text to big?
        # Shrink Text
        if ((textLen <= 24) & (textWidth > imageWidth)) :
            while ((textWidth * .9) > imageWidth) :
                print ("shrink")
                fontSize = int (fontSize) * .9
                font = ImageFont.truetype ('impact.ttf', int (fontSize))
                textWidth, textHeight = self.getTextDim (text, font)
            return font, textWidth

# Gather Materials
image = Image.open ("PatrickCreep.jpg")
imageWidth, imageHeight = image.size
print ("Width: ", imageWidth)
print ("Height: ", imageHeight)
textColor = "#FFFFFF"
borderColor = "#000000"
borderSize = 4
defaultFontSize = 100

# Text Objects
print ("\nTop Obj")
top = textBlock ("Come here kid", 100, ImageFont.truetype ('impact.ttf', defaultFontSize))
print ("\nBot Obj")
bot = textBlock ("I have candy", 100, ImageFont.truetype ('impact.ttf', defaultFontSize))


# Fitting the Text
# def adjustText (imageWidth, text, textWidth, textLen, font, fontSize, SpacesIndex) :
print ("\nAdjusting Top: ")
top.font, top.textW = top.adjustText (imageWidth, top.text, top.textW, top.textLen, top.font, top.fontSize, top.spacesIndex)
print ("\nAdjusting Bottom: ")
bot.font, bot.textW = bot.adjustText (imageWidth, bot.text, bot.textW, bot.textLen, bot.font, bot.fontSize, bot.spacesIndex)

# if (textW > imageWidth) :
#     fontSize = int (fontSize) / 2
#     font = ImageFont.truetype ('impact.ttf', int (fontSize))

topOffset = 10

botOffset = ((imageWidth - bot.textW) / 2)

# Make Meme
image_editable = ImageDraw.Draw (image)

drawer = ImageDraw.Draw (image)

drawer.text ((topOffset, 0), top.text, font = top.font, fill = textColor, stroke_width = borderSize, stroke_fill = borderColor, align = 'center')

drawer.text ((botOffset, 550), bot.text, font = bot.font, fill = textColor, stroke_width = borderSize, stroke_fill = borderColor, align = 'center')

image.save ("result.jpg")