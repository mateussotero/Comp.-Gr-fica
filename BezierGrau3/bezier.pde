
  float p1x = 100;
  float p1y = 100;
  float p2x = 200;
  float p2y = 200;
  float p3x = 600;
  float p3y = 200;
  float p4x = 700;
  float p4y = 100;
    float ax = 0;
    float bx = 0;
    float cx = 0;
    float dx = 0;
    float ex = 0;
    float fx = 0;
    float ay = 0;
    float by = 0;
    float cy = 0;
    float dy = 0;
    float ey = 0;
    float fy = 0;
    
    void setup()
{
  size(800,600);
}
    
void draw()
{
  background(128);
  
   if(mousePressed && (mouseButton == LEFT)){
  p2x = mouseX;
  p2y = mouseY;}
  else if(mousePressed && (mouseButton == RIGHT)){
  p3x = mouseX;
  p3y = mouseY;
  }

 beginShape();
 
vertex(p1x, p1y);
 for(float t = 0; t <= 1; t += 0.01)
 {
    ax = p1x + t*(p2x-p1x);
    bx = p2x + t*(p3x-p2x);
    cx = p3x + t*(p4x-p3x);
    dx = ax + t*(bx-ax);
    ex = bx + t*(cx-bx);
    fx = dx + t*(ex-dx);
    ay = p1y + t*(p2y-p1y);
    by = p2y + t*(p3y-p2y);
    cy = p3y + t*(p4y-p3y);
    dy = ay + t*(by-ay);
    ey = by + t*(cy-by);
    fy = dy + t*(ey-dy);
    vertex(fx,fy);  
  }
 
  
  vertex(p4x, p4y);
  endShape(CLOSE); 
  
  line (p1x,p1y,p2x,p2y);
    line (p2x,p2y,p3x,p3y);
      line (p3x,p3y,p4x,p4y);
      
 // line (ax,ay,bx,by);
 // line (bx,by,cx,cy);
 // line (dx,dy,ex,ey);
      
}

  
