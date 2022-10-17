## This contains the script snippets that come with the documetation for testing

##################################################################### addons.py
# from vedo import Axes, Box, show
# box = Box(pos=(1,2,3), length=8, width=9, height=7).alpha(0.1)
# axs = Axes(box, c='k')  # returns Assembly object
# for a in axs.unpack():
#     print(a.name)
# show(box, axs).close()

# from vedo import Box, show
# b = Box(pos=(0, 0, 0), length=80, width=90, height=70).alpha(0.1)
# show(
#     b,
#     axes={
#         "xtitle": "Some long variable [a.u.]",
#         "number_of_divisions": 4,
#         # ...
#     },
# )

##################################################################### base.py

# from vedo import *
# c1 = Cube()
# c2 = c1.clone().c('violet').alpha(0.5) # copy of c1
# v = vector(0.2,1,0)
# p = vector(1,0,0)  # axis passes through this point
# c2.rotate(90, axis=v, point=p)
# l = Line(-v+p, v+p).lw(3).c('red')
# show(c1, l, c2, axes=1).close()

# from vedo import *
# objs = []
# for i in range(-5, 5):
#     p = [i/3, i/2, i]
#     v = vector(i/10, i/20, 1)
#     c = Circle(r=i/5+1.2).pos(p).orientation(v).lw(3)
#     objs += [c, Arrow(p,p+v)]
# show(objs, axes=1).close()

# from vedo import *
# c1 = Cube()
# c2 = c1.clone().c('violet').alpha(0.5) # copy of c1
# v = vector(0.2,1,0)
# p = vector(1,0,0)  # axis passes through this point
# c2.rotate(90, axis=v, point=p)
# # get the inverse of the current transformation
# T = c2.get_transform(invert=True)
# c2.apply_transform(T)  # put back c2 in place
# l = Line(p-v, p+v).lw(3).c('red')
# show(c1.wireframe().lw(3), l, c2, axes=1)


# from vedo import *
# tetmesh = TetMesh(dataurl+'limb_ugrid.vtk')
# tetmesh.color('rainbow')
# cu = Cube(side=500).x(500) # any Mesh works
# tetmesh.cut_with_box(cu).show(axes=1).close()

##################################################################### mesh.py
# from vedo import Sphere
# Sphere().crop(right=0.3, left=0.1).show()


# from vedo import *
# c1 = Cylinder(pos=(0,0,0), r=2, height=3, axis=(1,.0,0), alpha=.1).triangulate()
# c2 = Cylinder(pos=(0,0,2), r=1, height=2, axis=(0,.3,1), alpha=.1).triangulate()
# intersect = c1.intersect_with(c2).join(reset=True)
# spline = Spline(intersect).c('blue').lw(5)
# show(c1, c2, spline, intersect.labels('id'), axes=1).close()


# from vedo import *
# grid = Grid()#.triangulate()
# circle = Circle(r=0.3, res=24).pos(0.11,0.12)
# line = Line(circle, closed=True, lw=4, c='r4')
# grid.imprint(line)
# show(grid, line, axes=1).close()


##################################################################### picture.py
# from vedo import Picture, dataurl
# pic = Picture(dataurl+'dog.jpg').pad()
# pic.append([pic,pic,pic], axis='y')
# pic.append([pic,pic,pic,pic], axis='x')
# pic.show(axes=1).close()


# import vedo
# p = vedo.Picture(vedo.dataurl+'images/dog.jpg').bw()
# vedo.show(p, p.clone().enhance(), N=2, mode='image', zoom='tight')


# from vedo import Picture, show
# pic1 = Picture("https://aws.glamour.es/prod/designs/v1/assets/620x459/547577.jpg")
# pic2 = pic1.clone().invert()
# pic3 = pic1.clone().binarize()
# show(pic1, pic2, pic3, N=3, bg="blue9")


# import vedo
# pic = vedo.Picture(vedo.dataurl+"images/dog.jpg")
# pic.rectangle([100,300], [100,200], c='green4', alpha=0.7)
# pic.line([100,100],[400,500], lw=2, alpha=1)
# pic.triangle([250,300], [100,300], [200,400])
# vedo.show(pic, axes=1)


##################################################################### plotter.py
# from vedo import Cone
# Cone().show(axes=1).fly_to([1,0,0]).show()


# from vedo import settings, Cube, Plotter
# settings.use_parallel_projection = True # or else it doesnt make sense!
# cube = Cube().alpha(0.2)
# plt = Plotter(size=(900,600), axes=dict(xtitle='x (um)'))
# plt.add_scale_indicator(units='um', c='blue4')
# plt.show(cube, "Scale indicator with units").close()


# from vedo import *

# def func(evt): # called every time the mouse moves
#     # evt is a dotted dictionary
#     if not evt.actor:
#         return  # no hit, return
#     print("point coords =", evt.picked3d)
#     # print("full event dump:", evt)

# elli = Ellipsoid()
# plt = Plotter(axes=1)
# plt.add_callback('mouse hovering', func)
# plt.show(elli).close()


##################################################################### pointcloud.py
# from vedo import Ellipsoid, show, visible_points
# s = Ellipsoid().rotate_y(30)
# #Camera options: pos, focal_point, viewup, distance,
# # clippingRange, parallelScale, thickness, viewAngle
# camopts = dict(pos=(0,0,25), focal_point=(0,0,0))
# show(s, camera=camopts, offscreen=True)
# m = visible_points(s)
# #print('visible pts:', m.points()) # numpy array
# show(m, new=True, axes=1) # optionally draw result on a new window


# import numpy as np
# from vedo import *
# def fibonacci_sphere(n):
#     s = np.linspace(0, n, num=n, endpoint=False)
#     theta = s * 2.399963229728653
#     y = 1 - s * (2/(n-1))
#     r = np.sqrt(1 - y * y)
#     x = np.cos(theta) * r
#     z = np.sin(theta) * r
#     return [x,y,z]
# Points(fibonacci_sphere(1000)).show(axes=1).close()


# from vedo import *
# s = Sphere(res=10).linewidth(1).c("orange").compute_normals()
# point_ids = s.labels('id', cells=False).c('green')
# cell_ids  = s.labels('id', cells=True ).c('black')
# show(s, point_ids, cell_ids).close()


# from vedo import Sphere, show
# sph = Sphere(quads=True, res=4).compute_normals().wireframe()
# sph.celldata["zvals"] = sph.cell_centers()[:,2]
# l2d = sph.labels("zvals", cells=True, precision=2).backcolor('orange9')
# show(sph, l2d, axes=1).close()


# from vedo import Cube, show
# c1 = Cube().rotate_z(5).x(2).y(1)
# print("cube1 position", c1.pos())
# T = c1.get_transform()  # rotate by 5 degrees, sum 2 to x and 1 to y
# c2 = Cube().c('r4')
# c2.apply_transform(T)   # ignore previous movements
# c2.apply_transform(T, concatenate=True)
# c2.apply_transform(T, concatenate=True)
# print("cube2 position", c2.pos())
# show(c1, c2, axes=1).close()


# from vedo import Disc, show
# disc = Disc(r1=1, r2=1.2)
# mesh = disc.extrude(3, res=50).linewidth(1)
# mesh.cut_with_cylinder([0,0,2], r=0.4, axis='y', invert=True)
# show(mesh, axes=1)


# from vedo import Disc, show
# disc = Disc(r1=1, r2=1.2)
# mesh = disc.extrude(3, res=50).linewidth(1)
# mesh.cut_with_sphere([1,-0.7,2], r=1.5, invert=True)
# show(mesh, axes=1)

# from vedo import *
# import numpy as np
# arr = np.random.randn(100000, 3)/2
# pts = Points(arr).c('red3').pos(5,0,0)
# cube = Cube().pos(4,0.5,0)
# assem = pts.cut_with_mesh(cube, keep=True)
# show(assem.unpack(), axes=1).close()


##################################################################### shapes.py
# from vedo import Line
# pts = [[1, 0, 0], [5, 2, 0], [3, 3, 1]]
# ln = Line(pts, c='r', lw=5).pattern('- -', repeats=10)
# ln.show(axes=1).close()


# from vedo import *
# shape = load(dataurl+"timecourse1d.npy")[58]
# pts = shape.rotate_x(30).points()
# tangents = Line(pts).tangents()
# arrs = Arrows(pts, pts+tangents, c='blue9')
# show(shape.c('red5').lw(5), arrs, bg='bb', axes=1).close()

# from vedo import *
# from vedo.pyplot import plot
# shape = load(dataurl+"timecourse1d.npy")[55]
# curvs = Line(shape.points()).curvature()
# shape.cmap('coolwarm', curvs, vmin=-2,vmax=2).add_scalarbar3d(c='w')
# shape.render_lines_as_tubes().lw(12)
# pp = plot(curvs, ac='white', lc='yellow5')
# show(shape, pp, N=2, bg='bb', sharecam=False).close()


# from vedo import Line, show
# aline = Line([(0,0,0),(1,3,0),(2,4,0)])
# surf1 = aline.sweep((1,0.2,0), res=3)
# surf2 = aline.sweep((0.2,0,1))
# aline.color('r').linewidth(4)
# show(surf1, surf2, aline, axes=1).close()

# from vedo import *
# pts = [(-4,-3),(1,1),(2,4),(4,1),(3,-1),(2,-5),(9,-3)]
# ln = Line(pts, c='r', lw=2).z(0.01)
# rl = RoundedLine(pts, 0.6)
# show(Points(pts), ln, rl, axes=1).close()

# from vedo import *
# import numpy as np
# pts = np.random.randn(25,3)
# for i,p in enumerate(pts):
#     p += [5*i, 15*sin(i/2), i*i*i/200]
# show(Points(pts), Bezier(pts), axes=1).close()

# from vedo import *
# import numpy as np
# xcoords = np.arange(0, 2, 0.2)
# ycoords = np.arange(0, 1, 0.2)
# sqrtx = sqrt(xcoords)
# grid = Grid(s=(sqrtx, ycoords))
# grid.show(axes=8)

# # can also create a grid from np.mgrid:
# X, Y = np.mgrid[-12:12:1000*1j, 0:15:1000*1j]
# vgrid = Grid(s=(X[:,0], Y[0]))
# vgrid.show(axes=8).close()

# from vedo import *
# settings.immediate_rendering = False
# plt = Plotter(N=18)
# for i in range(18):
#     ps = ParametricShape(i).color(i)
#     plt.at(i).show(ps, ps.name)
# plt.interactive()