import FreeCAD as App
import Part

doc = App.newDocument("TL5020_Stand_25mm_Corrected")

# Grunnmål
stand_height = 250  # høyde
stand_width = 370   # bredde (ytterkant)
stand_depth = 280   # dybde
tube_size = 25      # rørdimensjon (25x25 mm firkantrør)

# Justert dybdeoffset (foran peker nå i negativ Y-retning)
front_offset = -stand_depth + tube_size

# ------------------------
# VENSTRE C-formet side
# ------------------------

left_vertical = Part.makeBox(tube_size, tube_size, stand_height)
left_vertical.translate(App.Vector(0, 0, 0))

left_top = Part.makeBox(tube_size, stand_depth, tube_size)
left_top.translate(App.Vector(0, front_offset, stand_height - tube_size))

left_bottom = Part.makeBox(tube_size, stand_depth, tube_size)
left_bottom.translate(App.Vector(0, front_offset, 0))

# ------------------------
# HØYRE C-formet side
# ------------------------

right_vertical = Part.makeBox(tube_size, tube_size, stand_height)
right_vertical.translate(App.Vector(stand_width - tube_size, 0, 0))

right_top = Part.makeBox(tube_size, stand_depth, tube_size)
right_top.translate(App.Vector(stand_width - tube_size, front_offset, stand_height - tube_size))

right_bottom = Part.makeBox(tube_size, stand_depth, tube_size)
right_bottom.translate(App.Vector(stand_width - tube_size, front_offset, 0))

# ------------------------
# Tverrbjelker
# ------------------------

bottom_front = Part.makeBox(stand_width, tube_size, tube_size)
bottom_front.translate(App.Vector(0, front_offset, 0))

top_back = Part.makeBox(stand_width, tube_size, tube_size)
top_back.translate(App.Vector(0, 0, stand_height - tube_size))

top_front = Part.makeBox(stand_width, tube_size, tube_size)
top_front.translate(App.Vector(0, front_offset, stand_height - tube_size))

# ------------------------
# Vektstøtte: Vertikale rør 2 cm foran de eksisterende vertikale rørene, inne i C-formen
# ------------------------

support_offset = -60  # 2 cm foran de eksisterende vertikale rørene

left_support = Part.makeBox(tube_size, tube_size, stand_height)
left_support.translate(App.Vector(0, support_offset, 0))

right_support = Part.makeBox(tube_size, tube_size, stand_height)
right_support.translate(App.Vector(stand_width - tube_size, support_offset, 0))

# ------------------------
# Sammensetting
# ------------------------

parts = [
    left_vertical, left_top, left_bottom,
    right_vertical, right_top, right_bottom,
    bottom_front, top_back, top_front,
    left_support, right_support  # legg til støtterørene her
]

assembly = parts[0]
for part in parts[1:]:
    assembly = assembly.fuse(part)

Part.show(assembly)
doc.recompute()

# Automatisk visning og sentrering
App.Gui.activeDocument().activeView().viewAxometric()
App.Gui.SendMsgToActiveView("ViewFit")
