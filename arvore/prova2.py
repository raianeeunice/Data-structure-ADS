import os

class Node :
  def __init__(self, data, isQuestion=False, left=None, right=None) :
    self.data = data
    self.isQuestion = isQuestion
    self.left  = left
    self.right = right

  def __str__(self) :
    question = "?" if self.isQuestion else ""
    return str(self.data + question)

  def getLeft(self) :
    return self.left

  def getRight(self) :
    return self.right

  def getDado(self) :
    return self.data
  
  def setLeft(self, left) :
    self.left = left

  def setRight(self, right) :
    self.right = right

  def setDado(self, data) :
    self.data = data
  
  def setIsQuestion(self, isQuestion):
    self.isQuestion = isQuestion
  
  def getIsQuestion(self):
    return self.isQuestion

def show_tree(root, idt=0, resp=""):
  if root is not None:
    # resp = "" if root.getIsQuestion() else resp
    print(' '*idt, resp, root)
    show_tree(root.getLeft(), idt+2, "Não?")
    show_tree(root.getRight(), idt+2, "Sim?")

def skynet() :
  # start with a singleton
  root = Node("carro")

  print("Olá! Bem-vindo(a,e) ao programa de treinamento da Skynet")
  # loop until the user quits
  while 1 :
    if yes("Deseja ver o que a SkyNet sabe até agora? "):
      show_tree(root)
      if not yes("Quer continuar? "):
        print("Tchau :)")
        break

    os.system("cls")

    # walk the node
    node = root
    while node.getLeft() != None :
      prompt = node.getDado() + "? "
      if yes(prompt):
        node = node.getRight()
      else:
        node = node.getLeft()

    # make a guess
    guess = node.getDado()
    prompt = "É um(a) " + guess + "? "
    if yes(prompt) :
      print ("Consegui!")
      print()
      if yes("Quer continuar? "):
        os.system("cls")
        continue
      else :
        print("Tchau :)")
        break

    # get new information
    prompt  = "O que você está pensando, então ? "
    answer  = input(prompt)
    prompt  = "Qual a diferença entre %s e %s? "
    question = input(prompt % (answer,guess))

    # add new information to the node
    node.setDado(question)
    node.setIsQuestion(True)
    prompt = "Se fosse %s a resposta seria? "
    if yes(prompt % answer) :
      node.setLeft(Node(guess))
      node.setRight(Node(answer))
    else :
      node.setLeft(Node(answer))
      node.setRight(Node(guess))
    os.system("cls")

def yes(ques) :
  ans = (input(ques)).lower()
  return (ans[0:1] == 'y')


if __name__ == "__main__":
  skynet()