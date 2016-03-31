# coding: utf-8

import os
import codecs
import subprocess


class lolwut:
    
    def __init__(self, lel, inf):
        self.inf = inf
        self.lel = lel
        self.recs = []
        self.finalrecs = []
        self.currentrecs = []
        self.tryrecs = []
        self.usedId = []
        self.pages = 1
        self.doFor(lel)
        print("done Dofor")
        self.validIs = []
        self.maximizePage()
        self.writeText(self.currentrecs, "../cuisine/tex/"+self.lel+".tex")
        self.compileTex()

    def parse(self, filename, fout):
        f = open(filename, "r")
        data = f.readlines()
        recipe = ""
        skip = 0
        for i in range(len(data)):
            #print(data[i])
            if skip == 0:
                if data[i] == "#\n":
                    self.parseRecipe(recipe, fout)
                    recipe = ""
                    skip = 1
                else:
                    recipe += data[i]
            else:
                skip -= 1
        f.close()

    def parseRecipe(self, recipe, fout):
        recipe = recipe.split("\n")
        res = "\\begin{minipage}[c]{\\textwidth}\n"
        title, personne, auteur = self.handleTitle(recipe[0])
        res += "\\recette{"+title+"}\n"
        if auteur != "":
            res += "\\otor{"+auteur+"}\n"
        i = 2
        if recipe[i] != "$":
            if personne != "":
                res += "\\ingredients[("+personne+")]{\n"
            else:
                res += "\\ingredients{\n"
            while recipe[i] != "":
                res += "\\item " + self.repChar(recipe[i]) + "\n"
                i += 1
            res += "}\n"
        else:
            i+=1
        i += 1
        while i < len(recipe):
            res += self.repChar(recipe[i]) + "\\\\\n"
            last = recipe[i]
            i += 1
        self.append(res+"\n\\end{minipage}\n\n", fout)

    def handleTitle(self, data):
        title = ""
        personne = ""
        auteur = ""
        nb = 0
        for char in data:
            if char != "[" and char != "]" and char != "{" and char != "}" and char != "\n" and char != "\r":
                if nb == 0:
                    title += char
                elif nb == 1:
                    personne += char
                elif nb == 2:
                    auteur += char
            elif char == "{":
                nb = 1
            elif char == "[":
                nb = 2
        return self.repChar(title), self.repChar(personne), self.repChar(auteur)

    def repChar(self, data):
        data = data.replace("\xc2°", u"\\degrees")
        data = data.replace("\xc2¼", u"$\\nicefrac{1}{4}$")
        data = data.replace("\xc2½", u"$\\nicefrac{1}{2}$")
        data = data.replace("\xc2¾", u"$\\nicefrac{3}{4}$")
        return data

    def append(self, data, file):
        #print(data)
        self.recs.append(data)
        """
        f = open(file, "a")
        f.write(data)
        f.close()    """


    def writeText(self, data, file):
        f = open(file, "w")
        for line in data:
            f.write(line)
        f.close()

    def doFor(self, lel):
        print(lel)
        f = open("../cuisine/tex/"+lel+".tex", "w")
        f.close()
        self.parse("raw/"+lel+".txt", "../cuisine/tex/"+lel+".tex")
        
        
        

    def maximizePage(self):
        self.validId = list(range(len(self.recs)))
        while len(self.recs) != len(self.currentrecs):
            print("==================== "+str(self.pages)+" ====================")
            print(self.newPage())
            self.currentrecs = self.currentrecs + self.tryrecs
            self.tryrecs = []
            self.pages += 1
                

    def newPage(self):
        space = True
        hold = None
        while space:
            i = 0
            if len(self.validId) == 0:
                return "done"
            self.tryrecs.append(self.recs[self.validId[i]])
            self.usedId.append(self.validId[i])
            hold = self.validId.pop(0)
            space = self.goTry()
            if not space:
                self.usedId.pop()
                self.tryrecs.pop()
                self.validId.insert(0, hold)
        self.tryAdd(0)

    def tryAdd(self, b):
        a = 0
        for i in self.validId:
            if i >= b:
                self.tryrecs.append(self.recs[i])
                self.usedId.append(i)
                space = self.goTry()
                if space:
                    self.validId.pop(a)
                    self.tryAdd(i)
                    return
                else:
                    self.usedId.pop()
                    self.tryrecs.pop()
            a+=1
                    

    def goTry(self):
        self.writeText(self.tryrecs, "../cuisine/tex/"+self.lel+".tex")
        self.compileTex()
        print(self.usedId)
        current = self.getNbPage()
        if current == 1:
            return True
        else:
            return False

    def compileTex(self):
        cmd = "pdflatex C:/Users/Simon/Desktop/mamette/cuisine/"+self.inf+".tex -output-directory=C:/Users/Simon/Desktop/mamette/cuisine/"
        CREATE_NO_WINDOW = 0x08000000
        #subprocess.call(cmd)
        subprocess.call(cmd, creationflags=CREATE_NO_WINDOW)
        #os.system(cmd)


    def getNbPage(self):
        cmd = "pdfinfo ../cuisine/"+self.inf+".pdf"
        res = os.popen(cmd).read().strip()
        res = res.split("\n")
        res = res[5]
        res = res[6:]
        res = res.strip()
        res = int(res)
        print(res)
        return res

    

if __name__ == "__main__":
    #a = lolwut("sauce", "trysauce")
    #a = lolwut("entree", "tryentree")
    a = lolwut("plat", "tryplat")
    a = lolwut("sauce", "trysauce")
    a = lolwut("dessert", "trydessert")
