import eppy
from eppy.modeleditor import IDF
# 设置EnergyPlus的IDF版本对应的idd文件路径
IDF.setiddname("C:/EnergyPlusV9 - 2 - 0/Energy+.idd")
idf = IDF()
building = idf.newidfobject("Building")
building.Name = "1ZoneBoxBuilding"
building.Terrain = "City"
building.North_Axis = 0.0
building.Num_Storys = 1

# - ** 定义方盒建筑的尺寸（以边长为例） **
# - 假设方盒建筑的边长为
# `L`，这里设置为10米（可根据需要修改）。
# ```python

L = 10
building.Width = L
building.Depth = L
building.Height = L

# 地面
ground_surface = idf.newidfobject("BuildingSurface:Detailed")
ground_surface.Name = "GroundSurface"
ground_surface.Surface_Type = "Floor"
ground_surface.Outside_Boundary_Condition = "Ground"
ground_surface.Outside_Boundary_Condition_Object = "Ground"
ground_surface.Corners = ((0, 0, 0), (L, 0, 0), (L, L, 0), (0, L, 0))
ground_surface.Area = L * L
# 屋顶
roof_surface = idf.newidfobject("BuildingSurface:Detailed")
roof_surface.Name = "RoofSurface"
roof_surface.Surface_Type = "Roof"
roof_surface.Outside_Boundary_Condition = "Outdoors"
roof_surface.Outside_Boundary_Condition_Object = "Outdoors"
roof_surface.Corners = ((0, 0, L), (L, 0, L), (L, L, L), (0, L, L))
roof_surface.Area = L * L

# - ** 定义建筑的外墙表面（四个侧面） **
# - 以下代码定义了四个外墙表面，构成了方盒建筑的外立面。
# ```python
# 外墙1
wall1 = idf.newidfobject("BuildingSurface:Detailed")
wall1.Name = "Wall1"
wall1.Surface_Type = "Wall"
wall1.Outside_Boundary_Condition = "Outdoors"
wall1.Outside_Boundary_Condition_Object = "Outdoors"
wall1.Corners = ((0, 0, 0), (L, 0, 0), (L, 0, L), (0, 0, L))
wall1.Area = L * L
# 外墙2
wall2 = idf.newidfobject("BuildingSurface:Detailed")
wall2.Name = "Wall2"
wall2.Surface_Type = "Wall"
wall2.Outside_Boundary_Condition = "Outdoors"
wall2.Outside_Boundary_Condition_Object = "Outdoors"
wall2.Corners = ((L, 0, 0), (L, L, 0), (L, L, L), (L, 0, L))
wall2.Area = L * L
# 外墙3
wall3 = idf.newidfobject("BuildingSurface:Detailed")
wall3.Name = "Wall3"
wall3.Surface_Type = "Wall"
wall3.Outside_Boundary_Condition = "Outdoors"
wall3.Outside_Boundary_Condition_Object = "Outdoors"
wall3.Corners = ((L, L, 0), (0, L, 0), (0, L, L), (L, L, L))
wall3.Area = L * L
# 外墙4
wall4 = idf.newidfobject("BuildingSurface:Detailed")
wall4.Name = "Wall4"
wall4.Surface_Type = "Wall"
wall4.Outside_Boundary_Condition = "Outdoors"
wall4.Outside_Boundary_Condition_Object = "Outdoors"
wall4.Corners = ((0, L, 0), (0, 0, 0), (0, 0, L), (0, L, L))
wall4.Area = L * L

WWR = 0.3
total_wall_area = 4 * L * L
window_area_per_wall = (WWR * total_wall_area) / 4
# 在每个外墙面上设置窗户（简单示例，均匀分布）
# 外墙1上的窗户
window1 = idf.newidfobject("FenestrationSurface:Detailed")
window1.Name = "Window1"
window1.Surface_Type = "Window"
window1.Outside_Boundary_Condition = "Outdoors"
window1.Outside_Boundary_Condition_Object = "Outdoors"
window1.Corners = ((0, 0, 0.5), (L/2, 0, 0.5), (L/2, 0, L - 0.5), (0, 0, L - 0.5))
window1.Area = window_area_per_wall
# 外墙2上的窗户
window2 = idf.newidfobject("FenestrationSurface:Detailed")
window2.Name = "Window2"
window2.Surface_Type = "Window"
window2.Outside_Boundary_Condition = "Outdoors"
window2.Outside_Boundary_Condition_Object = "Outdoors"
window2.Corners = ((L, 0, 0.5), (L, L/2, 0.5), (L, L/2, L - 0.5), (L, 0, L - 0.5))
window2.Area = window_area_per_wall
# 外墙3上的窗户
window3 = idf.newidfobject("FenestrationSurface:Detailed")
window3.Name = "Window3"
window3.Surface_Type = "Window"
window3.Outside_Boundary_Condition = "Outdoors"
window3.Outside_Boundary_Condition_Object = "Outdoors"
window3.Corners = ((L, L, 0.5), (L/2, L, 0.5), (L/2, L, L - 0.5), (L, L, L - 0.5))
window3.Area = window_area_per_wall
# 外墙4上的窗户
window4 = idf.newidfobject("FenestrationSurface:Detailed")
window4.Name = "Window4"
window4.Surface_Type = "Window"
window4.Outside_Boundary_Condition = "Outdoors"
window4.Outside_Boundary_Condition_Object = "Outdoors"
window4.Corners = ((0, L, 0.5), (0, L/2, 0.5), (0, L/2, L - 0.5), (0, L, L - 0.5))
window4.Area = window_area_per_wall

# 3. **保温层及厚度设置**
#    - **定义保温材料和构造**
#      - 首先定义保温材料的属性，如导热系数、密度和比热容等，然后创建一个包含保温层的建筑构造。
#      ```python
# 添加保温材料对象到IDF文件
insulation_material = idf.newidfobject("Material")
insulation_material.Name = "InsulationMaterial"
insulation_material.Thermal_Conductivity = 0.03  # 假设导热系数，单位W/m - K
insulation_material.Density = 30.0  # 假设密度，单位kg/m3
insulation_material.Specific_Heat = 1000.0  # 假设比热容，单位J/kg - K

# 添加构造对象（包含保温层）到IDF文件
construction = idf.newidfobject("Construction")
construction.Name = "WallConstruction"
construction.Layers = ["InsulationMaterial"]
construction.Layer_Thickness = [0.1]  # 假设保温层厚度为0.1m

for wall in [wall1, wall2, wall3, wall4]:
    wall.Construction_Name = "WallConstruction"

# 保存IDF文件
idf.saveas("1ZoneBoxBuilding.idf")