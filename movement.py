# movement.py

import goodGuys, enemies

class Character():
    
    def move():
        for each in goodGuys.Allies.group:
            if goodGuys.Allies.left > 0:
                goodGuys.Allies.xAxis -= goodGuys.Allies.speed
                goodGuys.Allies.left -=1
            else:
                pass
            if goodGuys.Allies.right > 0:
                goodGuys.Allies.xAxis += goodGuys.Allies.speed
                goodGuys.Allies.right -=1
            else:
                pass
            if goodGuys.Allies.up > 0:
                goodGuys.Allies.yAxis -= goodGuys.Allies.speed
                goodGuys.Allies.up -= 1
            else:
                pass
            if goodGuys.Allies.down > 0:
                goodGuys.Allies.yAxis += goodGuys.Allies.speed
                goodGuys.Allies.down -=1
            else:
                pass
            if goodGuys.Allies.jump >0:
                if goodGuys.Allies.facing == 'right':
                    goodGuys.Allies.xAxis += goodGuys.Allies.speed
                else: 
                    goodGuys.Allies.xAxis -= goodGuys.Allies.speed
                if goodGuys.Allies.inverted == 'inverted':
                    goodGuys.Allies.yAxis += goodGuys.Allies.speed
                else:
                    goodGuys.Allies.yAxis -= goodGuys.Allies.speed
            else:
                pass

        for each in enemies.Army.group:
            if enemies.Army.left >0:
                enemies.Army.xAxis -= enemies.Army.speed
                enemies.Army.left -=1
            else:
                pass
            if enemies.Army.right > 0:
                enemies.Army.xAxis += enemies.Army.speed
                enemies.Army.right -=1
            else:
                pass
            if enemies.Army.up > 0:
                enemies.Army.yAxis -= enemies.Army.speed
                enemies.Army.up -=1
            else:
                pass
            if enemies.Army.down > 0:
                enemies.Army.yAxis += enemies.Army.speed
                enemies.Army.down -=1
            if enemies.Army.jump >0:
                if enemies.Army.facing == 'right':
                    enemies.Army.xAxis += enemies.Army.speed
                else: 
                    enemies.Army.xAxis -= enemies.Army.speed
                if enemies.Army.inverted == 'inverted':

                    enemies.Army.yAxis += enemies.Army.speed
                else:
                    enemies.Army.yAxis -= enemies.Army.speed
            else:
                pass
            