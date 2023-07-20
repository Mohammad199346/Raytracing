from sightpy import *

# Define materials to use
white_diffuse = Glossy(diff_color=rgb(1.0, 1.0, 1.0), n=vec3(1.3 + 1.91j, 1.3 + 1.91j, 1.4 + 2.91j), roughness=0.2, spec_coeff=0.0, diff_coeff=0.8)
red_diffuse = Glossy(diff_color=rgb(0.8, 0.1, 0.1), n=vec3(1.3 + 1.91j, 1.3 + 1.91j, 1.4 + 2.91j), roughness=0.2, spec_coeff=0.0, diff_coeff=0.8)
mirror = Glossy(diff_color=rgb(0.95, 0.95, 0.95), n=vec3(0.15 + 3.58j, 0.4 + 2.37j, 1.54 + 1.91j), roughness=0.0, spec_coeff=0.8, diff_coeff=0.2)
glass = Glossy(diff_color=rgb(0.8, 0.8, 0.9), n=vec3(1.5 + 0.01j, 1.5 + 0.01j, 1.5 + 0.01j), roughness=0.05, spec_coeff=0.8, diff_coeff=0.2)

# Set Scene
Sc = Scene(ambient_color=rgb(0.2, 0.2, 0.2))

# Camera Setup
Sc.add_Camera(look_from=vec3(0.0, 0.0, -15.0),
              look_at=vec3(0.0, 0.0, 0.0),
              screen_width=400,
              screen_height=300)

# Light Setup
Sc.add_DirectionalLight(Ldir=vec3(-0.5, -1.0, -0.5), color=rgb(1.0, 1.0, 1.0))

# Cornell Box Scene
# Back Wall
Sc.add(Plane(material=white_diffuse, center=vec3(0, 0, 10), width=120, height=120, u_axis=vec3(5, 0, 0), v_axis=vec3(0, 5, 0)))

# Floor
Sc.add(Plane(material=white_diffuse, center=vec3(0, -10, 0), width=120, height=120, u_axis=vec3(5, 0, 0), v_axis=vec3(0, 0, 5)))

# Ceiling
Sc.add(Plane(material=white_diffuse, center=vec3(0, 10, 0), width=120, height=120, u_axis=vec3(5, 0, 0), v_axis=vec3(0, 0, 5)))

# Left Wall
Sc.add(Plane(material=red_diffuse, center=vec3(-10, 0, 0), width=120, height=120, u_axis=vec3(0, 5, 0), v_axis=vec3(0, 0, 5)))

# Right Wall
Sc.add(Plane(material=mirror, center=vec3(10, 0, 0), width=120, height=120, u_axis=vec3(0, 5, 0), v_axis=vec3(0, 0, 5)))

# Glass Sphere
Sc.add(Sphere(material=glass, center=vec3(-3, -4, -5), radius=1, max_ray_depth=3))

# Reflective Sphere
Sc.add(Sphere(material=mirror, center=vec3(3, -5, -5), radius=1, max_ray_depth=3))

# Render
img = Sc.render(samples_per_pixel=8)

img.save("EXAMPLE.png")

img.show()
