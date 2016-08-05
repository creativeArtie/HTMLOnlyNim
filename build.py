import os.path

def createFiles(stack1, stack2, stack3, player):
  'produce the long list of files'
  if (stack1 != 0 or stack2 != 0 or stack3 != 0):
    if player == 2:
      player = 1
    else:
      player = 2
    if writeFile(stack1, stack2, stack3, player):
      for x in range(1, 3):
        if stack1 >= x:
          createFiles(stack1 - x, stack2, stack3, player)
        if stack2 >= x:
          createFiles(stack1, stack2 - x, stack3, player)
        if stack3 >= x:
          createFiles(stack1, stack2, stack3 - x, player)

def writeFile(stack1, stack2, stack3, player):
  'print out the single file'
  #Open
  fName = "p" + str(player) + "/" + \
        str(stack1) + "_" + str(stack2) + "_" + str(stack3) + ".html";
  if os.path.isfile(fName):
    return 0
  f = open(fName, "w")
  #File heading
  f.write("<!DOCTYPE html><html><body>")
  #Page Heading
  f.write("<p>Player " + str(player) + " Start</p>")
  #Table
  f.write("<table>")
  f.write("<tr><td>" + str(stack1) + "</td><td>" + str(stack2) + "</td><td>" + 
          str(stack3) + "</td></tr>")
  f.write("<tr><td>")
  #Choices
  for x in range(1, 4):
    if stack1 >= x:
      printOptions(f, player, stack1 - x, stack2, stack3, x)
  f.write("</td><td>")
  for x in range(1, 4):
    if stack2 >= x:
      printOptions(f, player, stack1, stack2 - x, stack3, x)
  f.write("</td><td>")
  for x in range(1, 4):
    if stack3 >= x:
      printOptions(f, player, stack1, stack2, stack3 - x, x)
  f.write("</td></tr>")
  f.write("<table></body></html>")
  f.close()
  return 1

def printOptions(f, player, stack1, stack2, stack3, size):
  if player == 1:
    player = 2
  else:
    player = 1
  begin = "<a href=\"../p" + str(player) + "/"
  middle = ".html\" target=\"_self\">Take "
  end = "</a><br>"
  link = str(stack1) + "_" + str(stack2) + "_" + str(stack3)
  f.write(begin + link + middle + str(size) + end)

createFiles(8, 7, 6, 2);
