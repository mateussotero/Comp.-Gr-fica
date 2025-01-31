from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from pathlib import Path
import sys
import math
import png

global largura
global altura

global a; a = 0
global xrot; xrot = 0.0
global yrot; yrot = 0.0

# Iluminacao com coordenadas
global ambientLight;ambientLight = (0.3, 0.3, 0.3, 1.0)
global diffuseLight; diffuseLight = (0.7, 0.7, 0.7, 0.7)
global specular; specular = (1.0, 1.0, 1.0, 1.0)
global specref; specref = (1.0, 1.0, 1.0, 1.0)

r1 = 2 #raio da Terra
r2 = 5 #raio do Sol
r3 = 0.5 #raio da Lua
n = 25
halfpi = math.pi/2

def f(u, v, r):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z

def LoadTextures():
    global texture
    texture =  glGenTextures(3) 
    ##################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    image_file = Path.cwd() / 'sol.png'
    print(image_file)
    reader = png.Reader(filename=image_file)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[1])
    image_file = Path.cwd() / 'mapa.png'
    print(image_file)
    reader = png.Reader(filename=image_file)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[2])
    image_file = Path.cwd() / 'lua.png'
    print(image_file)
    reader = png.Reader(filename=image_file)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def desenhaPlaneta(r):  #recebe como parâmetro o raio do planeta
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            glTexCoord2f(j/n,i/n); glVertex3fv(f(i,j,r))
            glTexCoord2f(j/n,(i+1)/n); glVertex3fv(f(i+1,j,r))
    glEnd()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   # glRotatef(xrot, 1.0, 0.0, 0.0)
   # glRotatef(yrot, 0.0, 1.0, 0.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[0]) # SOL
    glPushMatrix()
    glRotatef(a, 0.0, 0.0, 0.5)
    glTranslatef(0.0, 0.0, 0.0)
    desenhaPlaneta(r2)
    glPopMatrix()
    
    glBindTexture(GL_TEXTURE_2D, texture[1]) # TERRA
    glPushMatrix()
    glRotatef(a, 0.0, 0.0, -a) 
    glTranslatef(0.0, 12.0, 0.0)
    glRotatef(-100, 1.0, 0.0, 0.0) 
    glRotatef(a, 0.0, 1.0, 0.0)
    desenhaPlaneta(r1)
    
    glBindTexture(GL_TEXTURE_2D, texture[2]) # LUA
    glRotatef(a, 0.0, 0.0, a)
    glTranslatef(2.0, 1.0, 3.0)
    desenhaPlaneta(r3)
    glPopMatrix()

    glutSwapBuffers()
    a += 1

def specialkeys(key, x, y):
    global xrot
    global yrot

    if key == GLUT_KEY_UP:
        xrot -= 2.0
    if key == GLUT_KEY_DOWN:
        xrot += 2.0
    if key == GLUT_KEY_LEFT:
        yrot -= 2.0
    if key == GLUT_KEY_RIGHT:
        yrot += 2.0

    glutPostRedisplay()

def reshape(w, h):
    lightPos = (-5.0, 5.0, 10.0, 1.0)
    nRange = 15.0

    if h==0:
        h = 1

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # allows for reshaping the window without distorting
    # the GLUT shape
    if w <= h:
        glOrtho(-nRange, nRange, -nRange*h/w, nRange*h/w, -nRange, nRange)
    else:
        glOrtho(-nRange*w/h, nRange*w/h, -nRange, nRange, -nRange, nRange)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)

def keyboard(key, x, y):
    if key == "n":
        xrot, yrot = 0
    elif key == chr(27) or key == "q":
        sys.exit()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
largura = 900 #round(2 * glutGet(GLUT_SCREEN_WIDTH) / 3)
altura =  600 # round(2 * glutGet(GLUT_SCREEN_HEIGHT) / 3)
glutInitWindowSize(largura, altura)
glutCreateWindow("Sistema Solar")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
glMaterialfv(GL_FRONT, GL_SPECULAR, specref)
glMateriali(GL_FRONT, GL_SHININESS, 128)
InitGL(largura,altura)
glColor3ub(230, 100, 155)
glClearColor(0.0, 0.0, 0.0, 1.0)
gluPerspective(45.0, float(largura)/float(altura), 0.1, 100.0)
glTranslatef(0.0, 0.0, -8)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutSpecialFunc(specialkeys)
glutTimerFunc(50, timer, 1)
glutMainLoop()
