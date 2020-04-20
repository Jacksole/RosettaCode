import Image
def FloodFill( fileName, initNode, targetColor, replaceColor ):
   img = Image.open( fileName )
   pix = img.load()
   xsize, ysize = img.size
   Q = []
   if pix[ initNode[0], initNode[1] ] != targetColor:
      return img
   Q.append( initNode )
   while Q != []:
      node = Q.pop(0)
      if pix[ node[0], node[1] ] == targetColor:
         W = list( node )
         if node[0] + 1 < xsize:
            E = list( [ node[0] + 1, node[1] ] )
         else:
            E = list( node )
      # Move west until color of node does not match targetColor
      while pix[ W[0], W[1] ] == targetColor:
         pix[ W[0], W[1] ] = replaceColor
         if W[1] + 1 < ysize:
            if pix[ W[0], W[1] + 1 ] == targetColor:
               Q.append( [ W[0], W[1] + 1 ] )
         if W[1] - 1 >= 0:
            if pix[ W[0], W[1] - 1 ] == targetColor:
               Q.append( [ W[0], W[1] - 1 ] )
         if W[0] - 1 >= 0:
            W[0] = W[0] - 1
         else:
            break
      # Move east until color of node does not match targetColor
      while pix[ E[0], E[1] ] == targetColor:
         pix[ E[0], E[1] ] = replaceColor
         if E[1] + 1 < ysize:
            if pix[ E[0], E[1] + 1 ] == targetColor:
               Q.append( [ E[0], E[1] + 1 ] )
         if E[1] - 1 >= 0:
            if pix[ E[0], E[1] - 1 ] == targetColor:
               Q.append( [ E[0], E[1] -1 ] )
         if E[0] + 1 < xsize:
            E[0] = E[0] + 1
         else:
            break
      return img

# "FloodFillClean.png" is name of input file
# [55,55] the x,y coordinate where fill starts
# (0,0,0,255) the target colour being filled( black in this example )
# (255,255,255,255) the final colour ( white in this case )
img = FloodFill( "FloodFillClean.png", [55,55], (0,0,0,255), (255,255,255,255) )
#The resulting image is saved as Filled.png
img.save( "Filled.png" )
