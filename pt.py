from PIL import ImageFont

font = ImageFont.truetype("arial.ttf", 14)
sample = "Lorem ipsum dolor sit amet, partem periculis an duo, eum lorem paulo an, mazim feugiat lobortis sea ut. In est error eirmod vituperata, prima iudicabit rationibus mel et. Paulo accumsan ad sit, et modus assueverit eum. Quod homero adversarium vel ne, mel noster dolorum te, qui ea senserit argumentum complectitur. Duo at laudem explicari deterruisset, eu quo hinc mnesarchum. Vel autem insolens atomorum at, dolorum suavitate voluptatum duo ex."

#METHOD 2
width = 0
for c in sample:
    width += font.getsize(c)[0]
print (width)