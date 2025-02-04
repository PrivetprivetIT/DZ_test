from hitbox import Hitbox

hb1 = Hitbox(0, 100, 100, 100)
hb2 = Hitbox(50, 100, 100, 100)
hb3 = Hitbox(160, 100, 100, 100)

intersection1 = hb1.intersects(hb2)
intersection2 = hb2.intersects(hb3)
intersection3 = hb1.intersects(hb3)

print(intersection1)
print(intersection2)
print(intersection3)