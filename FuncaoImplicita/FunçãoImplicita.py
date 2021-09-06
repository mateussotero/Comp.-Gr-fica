from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

x0 = -1
xn = 1

y0 = -1
yn = 1

n = 30
dx = (xn - x0)/n
dy = (yn - y0)/n

def f(x,y):
    # Paraboloide Hiperbolico
    return x**2-y**2

def f2(x,y):
    # Paraboloide Circular
    return x**2+y**2

def cor(t, c1 = np.array([0,0,0]), c2 = np.array([1,1,1])): #c1 vermelho c2 azul t variando no range de c1 ate c2
    return c1 + t*(c2 - c1)    

def desenhaSuperficie():
    y = y0
    for i in range(n):
        x = x0       
        glBegin(GL_TRIANGLE_STRIP)        
        for j in range(n): 
            glColor3fv(cor(j/(n-1))) #chama a função cor e varia ela de acordo com o j (numero entre 0 e 1)
            glVertex3f(x, y, f(x, y)) #vertice 1
            glVertex3f(x, y + dy, f(x, y + dy)) #vertice 2
            x += dx
        glEnd()
        y += dy

def desenhaSuperficie2():
    y = y0
    for i in range(n):
        x = x0       
        glBegin(GL_TRIANGLE_STRIP)        
        for j in range(n):  
            glColor3fv(cor(j/(n-1)))
            glVertex3f(x, y, f2(x, y)) #vertice 1
            glVertex3f(x, y + dy, f2(x, y + dy)) #vertice 2           
            x += dx        
        glEnd()        
        y += dy

a = 0
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslate(-2, 2, 4)
    glRotatef(-a,1,0,0)
    desenhaSuperficie()   
    glPopMatrix()
    glPushMatrix()
    glTranslate(2, -2, 4)
    glRotatef(-a,1,0,0)
    desenhaSuperficie2()   
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
glutCreateWindow("Função Implicita")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()


