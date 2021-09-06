from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,1,1),(0.5,0.5,0.5),(0.4,0.4,0.4),(0.3,0.3,0.3),(0,0,0) )
a = 0
n=3 #variavel que controla a quantidade de lados do prisma

def desenhaPiramide():
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex3f(0,0,0)
    raio = 1
    for i in range(0,n+1):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x,y,-1)
    glEnd()



def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslate(0,0.5,4)
    glRotatef(270,1,0,0)
    glRotatef(a,0,0,1)
    desenhaPiramide()  
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
glutCreateWindow("Prisma")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()

