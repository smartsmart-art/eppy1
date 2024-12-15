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
construction.Layers = ["I   nsulationMaterial"]
construction.Layer_Thickness = [0.1]  # 假设保温层厚度为0.1m

for wall in [wall1, wall2, wall3, wall4]:
    wall.Construction_Name = "WallConstruction"

# 保存IDF文件
idf.saveas("1ZoneBoxBuilding.idf")

#    - 在上述代码中，`1ZoneBoxBuilding.idf`是保存的文件名，你可以根据自己的需求修改文件名和保存路径。需要注意的是，`C:/EnergyPlusV9 - 2 - 0/Energy+.idd`这个路径是`IDF`文件格式定义文件（`.idd`）的路径，你需要将其替换为你自己电脑上实际的EnergyPlus版本对应的`.idd`文件路径。
#
# 2. **进行模拟**
#    - **通过EnergyPlus软件进行模拟**
#      - 安装并打开EnergyPlus软件。在EnergyPlus软件界面中，打开刚才保存的`1ZoneBoxBuilding.idf`文件。然后在软件中设置模拟参数，如模拟的时间周期（例如，一年的能耗模拟可以设置起始日期和结束日期）、气象文件（`.epw`文件）等。气象文件包含了模拟所需的当地气象数据，如温度、湿度、太阳辐射等。
#      - 设置好所有参数后，在EnergyPlus软件中运行模拟。模拟完成后，EnergyPlus会生成一系列的输出文件，包括`.eso`（Energy Simulation Output）文件，它包含了模拟过程中的详细数据，如每个时间步长的室内温度、能耗等信息；还有`.html`文件，用于查看模拟结果的概要信息。
#    - **通过命令行进行模拟（更灵活，适用于自动化流程）**
#      - 找到EnergyPlus软件的安装目录，在命令行（例如，Windows的`cmd`或者Linux的`bash`）中切换到该目录。假设EnergyPlus软件安装在`C:/EnergyPlusV9 - 2 - 0/`目录下，且`1ZoneBoxBuilding.idf`文件保存在当前目录下，使用以下命令进行模拟：

# - 其中，`-w`
# 选项后面跟着气象文件（`.epw
# `文件）的路径，`1
# ZoneBoxBuilding.idf
# `是要模拟的建筑模型文件。你需要将气象文件路径替换为实际使用的气象文件的真实路径。这种方式可以方便地将模拟过程集成到自动化脚本中，例如在Python脚本中通过
# `subprocess`
# 模块来调用这个命令进行模拟。以下是一个简单的
# `subprocess`
# 调用示例：
# ```python
import subprocess

# 假设EnergyPlus安装目录和idf文件、气象文件路径如下
energyplus_path = "C:/EnergyPlusV9 - 2 - 0/energyplus"
weather_file_path = "C:/Path/To/WeatherFile.epw"
idf_file_path = "1ZoneBoxBuilding.idf"
command = [energyplus_path, "-w", weather_file_path, idf_file_path]
try:
    subprocess.check_call(command)
    print("模拟成功完成。")
except subprocess.CalledProcessError as e:
    print("模拟过程出现错误:", e)