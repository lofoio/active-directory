## creat some points for ploting
## plotting method: line() polygon()
sage: L = [[6*cos(pi*i/100)+5*cos((6/2)*pi*i/100),\
...   6*sin(pi*i/100)-5*sin((6/2)*pi*i/100)] for i in range(200)]
sage: p = polygon(L, rgbcolor=(1/8,1/4,1/2))
sage: t = text("hypotrochoid", (5,4), rgbcolor=(1,0,0))
sage: show(p+t)
var('x, y')
a=plot_vector_field((x, y), (x, -3, 3), (y, -3, 3), color='blue')
b=plot_vector_field((y, -x), (x, -3, 3), (y, -3, 3), color='red')
show(a + b, aspect_ratio=1, figsize=(4, 4))
