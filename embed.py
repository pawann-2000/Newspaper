import discord

class embed:
    def __init__(self,title="Not Assigned",description="Not Assigned",color="blue"):
        self.tittle = title
        self.description = description
        allowedColors = ["red","orange","green","blue","purple","yello","teal","magenta"]
        if color in allowedColors:
            if color == "red":
                self.color = discord.Color.red()
            elif color == "orange":
                self.color = discord.Color.orange()
            elif color == "green":
                self.color = discord.Color.green()
            elif color == "blue":
                self.color = discord.Color.blue()
            elif color == "purple":
                self.color = discord.Color.purple()
            elif color == "yellow":
                self.color = discord.Color.yellow()
            elif color == "teal":
                self.color = discord.Color.teal()
            elif color == "magenta":
                self.color = discord.Color.magenta()
        else:
            self.color = discord.Color.blue()
        self.embed = discord.Embed(title=self.tittle, description=self.description, color=self.color)
    
    def setTitle(self,title):
        self.embed.title = title
    
    def setDescription(self,description):
        self.embed.description = description
    
    def setColor(self,color):
        self.embed.color = color

    def getEmbed(self):
        return self.embed
