from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import numpy as np

r = 1
n = 30
halfpi = math.pi/2

def f(u, v):
    theta = (v*2*math.pi)/(n-1)
    a=(u*2/(n-1))
    x = a*math.cos(theta)
    y = a*a
    z = a*math.sin(theta)
    return x, y, z

def cor(t, c1 = np.array([0,0,0]), c2 = np.array([1,1,1])): 
    return t*(c2 - c1)

def desenhaEsfera():
    glBegin(GL_TRIANGLE_STRIP) 
    for i in range(n):
        for j in range(n):
            glColor3fv(cor(j/(n))) 
            glVertex3fv(f(i,j))
            glVertex3fv(f(i+1,j)) 
        
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslate(0,-2,0)
    glRotatef(a,0,1,0)
    desenhaEsfera()    
    glPopMatrix()
    glutSwapBuffers()
    a += 3
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Paraboloide")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()


