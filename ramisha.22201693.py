ramisha.22201693.py

#task1 


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
hrithikkk = 500
hritti = 500

# Rain properties
hritzzik = []
hrikkkz = 150  # Number of raindrops
silawatt = 0.0  # Rain bend angle

# Background color (day/night transition)
hrithiksilawat = [0.53, 0.81, 0.92]  # Day sky color (light blue)
hritzzwat = 0.01  # Color change speed
hritttkw = True  # Day mode flag
hritttk = 0  # Animation counter

def init_hrittik():
    """Initialize raindrops"""
    global hritzzik
    hritzzik = []
    for _ in range(hrikkkz):
        x = random.uniform(-250.0, 250.0)
        y = random.uniform(0.0, 250.0)
        speed = random.uniform(2.0, 5.0)
        hritzzik.append([x, y, speed])

def draw_hrithik_point(x, y):
    """Draw a point"""
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_hrithik_line(x1, y1, x2, y2):
    """Draw a line"""
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_hrithik_triangle(x1, y1, x2, y2, x3, y3):
    """Draw a filled triangle"""
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def draw_house():
    """Draw the house using primitives"""

    # House body (rectangle using two triangles)
    glColor3f(0.8, 0.6, 0.4)  # Brown color
    draw_hrithik_triangle(-100, 50, 100, 50, -100, -150)
    draw_hrithik_triangle(100, 50, 100, -150, -100, -150)

    # Roof (triangle)
    glColor3f(0.6, 0.2, 0.2)  # Dark red
    draw_hrithik_triangle(-125, 50, 0, 125, 125, 50)

    # Door (rectangle using two triangles)
    glColor3f(0.4, 0.2, 0.1)  # Dark brown
    draw_hrithik_triangle(-25, -150, 25, -150, -25, -50)
    draw_hrithik_triangle(25, -150, 25, -50, -25, -50)

    # Window 1 (left) - background
    glColor3f(0.5, 0.7, 0.9)  # Light blue
    draw_hrithik_triangle(-75, 0, -35, 0, -75, -40)
    draw_hrithik_triangle(-35, 0, -35, -40, -75, -40)

    # Window 2 (right) - background
    draw_hrithik_triangle(35, 0, 75, 0, 35, -40)
    draw_hrithik_triangle(75, 0, 75, -40, 35, -40)

    # Window frames (lines)
    glColor3f(0.2, 0.2, 0.2)
    glLineWidth(2)

    # Left window frame
    draw_hrithik_line(-75, 0, -35, 0)
    draw_hrithik_line(-75, -40, -35, -40)
    draw_hrithik_line(-75, 0, -75, -40)
    draw_hrithik_line(-35, 0, -35, -40)
    draw_hrithik_line(-55, 0, -55, -40)
    draw_hrithik_line(-75, -20, -35, -20)

    # Right window frame
    draw_hrithik_line(35, 0, 75, 0)
    draw_hrithik_line(35, -40, 75, -40)
    draw_hrithik_line(35, 0, 35, -40)
    draw_hrithik_line(75, 0, 75, -40)
    draw_hrithik_line(55, 0, 55, -40)
    draw_hrithik_line(35, -20, 75, -20)

    glLineWidth(1)

    # Door knob (point)
    glColor3f(0.9, 0.8, 0.1)  # Yellow
    glPointSize(5)
    draw_hrithik_point(15, -100)
    glPointSize(1)

def draw_rain():
    """Draw animated rain"""
    global silawatt

    # Rain color based on background
    if hritttkw:
        glColor3f(0.4, 0.5, 0.7)  # Blue-ish rain for day
    else:
        glColor3f(0.7, 0.8, 0.9)  # Lighter rain for night

    glLineWidth(2)

    for drop in hritzzik:
        x_offset = silawatt * (250.0 - drop[1]) / 250.0  # Bend effect
        draw_hrithik_line(drop[0] + x_offset, drop[1],
                         drop[0] + x_offset, drop[1] - 15)

    glLineWidth(1)

def update_rain():
    """Update raindrop positions"""
    for drop in hritzzik:
        drop[1] -= drop[2]  # Move down

        # Reset raindrop when it goes below screen
        if drop[1] < -250:
            drop[0] = random.uniform(-250.0, 250.0)
            drop[1] = 250.0
            drop[2] = random.uniform(2.0, 5.0)

def draw_ground():
    """Draw ground"""
    if hritttkw:
        glColor3f(0.3, 0.7, 0.3)  # Green grass for day
    else:
        glColor3f(0.1, 0.3, 0.1)  # Dark green for night

    draw_hrithik_triangle(-250, -150, 250, -150, -250, -250)
    draw_hrithik_triangle(250, -150, 250, -250, -250, -250)

def setup_projection():
    """Set up 2D coordinate system"""
    glViewport(0, 0, hrithikkk, hritti)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 0, 1)
    glMatrixMode(GL_MODELVIEW)

def display():
    """Main display function"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()

    # Draw ground
    draw_ground()

    # Draw rain
    draw_rain()

    # Draw house
    draw_house()

    glutSwapBuffers()

def animate():
    """Animation timer"""
    global hritttk
    update_rain()
    hritttk += 1
    glutPostRedisplay()

def keyboard_listener(key, x, y):
    """Handle keyboard input"""
    global hrithiksilawat, hritttkw

    # 'd' key - transition to day (light background)
    if key == b'd' or key == b'D':
        hrithiksilawat[0] = min(0.53, hrithiksilawat[0] + hritzzwat)
        hrithiksilawat[1] = min(0.81, hrithiksilawat[1] + hritzzwat * 1.5)
        hrithiksilawat[2] = min(0.92, hrithiksilawat[2] + hritzzwat * 1.7)
        if hrithiksilawat[0] >= 0.5:
            hritttkw = True
        glClearColor(hrithiksilawat[0], hrithiksilawat[1], hrithiksilawat[2], 1.0)

    # 'n' key - transition to night (dark background)
    elif key == b'n' or key == b'N':
        hrithiksilawat[0] = max(0.05, hrithiksilawat[0] - hritzzwat)
        hrithiksilawat[1] = max(0.05, hrithiksilawat[1] - hritzzwat * 1.5)
        hrithiksilawat[2] = max(0.15, hrithiksilawat[2] - hritzzwat * 1.5)
        if hrithiksilawat[0] <= 0.1:
            hritttkw = False
        glClearColor(hrithiksilawat[0], hrithiksilawat[1], hrithiksilawat[2], 1.0)

    glutPostRedisplay()

def special_key_listener(key, x, y):
    """Handle special keys (arrow keys)"""
    global silawatt

    # Left arrow - bend rain left
    if key == GLUT_KEY_LEFT:
        silawatt -= 5
        if silawatt < -80:
            silawatt = -80

    # Right arrow - bend rain right
    elif key == GLUT_KEY_RIGHT:
        silawatt += 5
        if silawatt > 80:
            silawatt = 80

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(hrithikkk, hritti)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"House in Rainfall - Hrithik Silawat")

    glClearColor(0.53, 0.81, 0.92, 1.0)  # Day sky

    init_hrittik()

    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)

    print("=" * 50)
    print("House in Rainfall - OpenGL Assignment")
    print("By: Hrithik Silawat")
    print("=" * 50)
    print("\nControls:")
    print("  LEFT ARROW  - Bend rain to the left")
    print("  RIGHT ARROW - Bend rain to the right")
    print("  D key       - Transition to Day (light background)")
    print("  N key       - Transition to Night (dark background)")
    print("=" * 50)

    glutMainLoop()

if __name__ == "__main__":
    main()


#task2


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


# BASIC WINDOW CONFI
hrithikk_width, hrithzzz_height = 500, 500
silatt_speed = 0.25
hrithiksilawat_blink = False
hrii_freeze = False
hrithzzz_counter = 0

# store all points here
hrithikk_points = []

# predefined colors and directions
hrithikk_colors = [(1, 0, 0), (0, 0, 1), (0, 1, 0), (0.5, 0, 0.5)]
hrithikk_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
hrithikk_positions = [(-100, -100), (100, -100), (-100, 100), (100, 100)]

# initialize two points — UPDATED LOOP
for hritik_loop_index in range(2):
    hrithikk_points.append({
        'x': hrithikk_positions[hritik_loop_index][0],
        'y': hrithikk_positions[hritik_loop_index][1],
        'dx': hrithikk_directions[hritik_loop_index][0],
        'dy': hrithikk_directions[hritik_loop_index][1],
        'clr': hrithikk_colors[hritik_loop_index],
        'orig': hrithikk_colors[hritik_loop_index]
    })



# HELPER FUNCTIONS

def hrii_convert_coord(mx, my):
    new_x = mx - (hrithikk_width / 2)
    new_y = (hrithzzz_height / 2) - my
    return new_x, new_y


def hrithzzz_draw_point(px, py, size, color):
    glColor3f(color[0], color[1], color[2])
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(px, py)
    glEnd()



# EVENT HANDLERS

def hrithzzz_mouse(btn, state, mx, my):
    global hrithiksilawat_blink, hrithikk_points

    px, py = hrii_convert_coord(mx, my)

    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        hrithiksilawat_blink = not hrithiksilawat_blink
        print("Blink:", "ON" if hrithiksilawat_blink else "OFF")

    elif btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        rand_dx = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        rand_dy = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        rand_color = (random.random(), random.random(), random.random())

        hrithikk_points.append({
            'x': px,
            'y': py,
            'dx': rand_dx,
            'dy': rand_dy,
            'clr': rand_color,
            'orig': rand_color
        })


def hrithzzz_key(key, x, y):
    global hrii_freeze
    if key == b' ':
        hrii_freeze = not hrii_freeze
        print("Points are Frozen" if hrii_freeze else "Points are Active")
    glutPostRedisplay()


def hrithzzz_special(key, x, y):
    global silatt_speed

    if hrii_freeze:
        return

    if key == GLUT_KEY_UP:
        silatt_speed *= 1.2
        print("Speed increased")

    elif key == GLUT_KEY_DOWN:
        silatt_speed /= 1.2
        print("Speed decreased")

    glutPostRedisplay()



# DISPLAY & ANIMATION

def hrithzzz_display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)

    for p in hrithikk_points:
        hrithzzz_draw_point(p['x'], p['y'], 10, p['clr'])

    glutSwapBuffers()


def hrithzzz_animate():
    global hrithikk_points, hrithiksilawat_blink, hrithzzz_counter

    if hrii_freeze:
        return

    for p in hrithikk_points:
        p['x'] += p['dx'] * silatt_speed
        p['y'] += p['dy'] * silatt_speed

        if p['x'] >= hrithikk_width / 2 or p['x'] <= -hrithikk_width / 2:
            p['dx'] *= -1

        if p['y'] >= hrithzzz_height / 2 or p['y'] <= -hrithzzz_height / 2:
            p['dy'] *= -1

    # blinking logic
    if hrithiksilawat_blink:
        hrithzzz_counter += 1
        if hrithzzz_counter >= 10:
            for p in hrithikk_points:
                p['clr'] = (0, 0, 0) if p['clr'] != (0, 0, 0) else p['orig']
            hrithzzz_counter = 0

    glutPostRedisplay()



# INIT WINDOW

def hrithzzz_init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(107, hrithikk_width / hrithzzz_height, 1, 999.0)



# MAIN FUNCTION

glutInit()
glutInitWindowSize(hrithikk_width, hrithzzz_height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"THE AMAZING BOX - Hrithik Silawat")

hrithzzz_init()

glutDisplayFunc(hrithzzz_display)
glutIdleFunc(hrithzzz_animate)
glutMouseFunc(hrithzzz_mouse)
glutKeyboardFunc(hrithzzz_key)
glutSpecialFunc(hrithzzz_special)

glutMainLoop()
