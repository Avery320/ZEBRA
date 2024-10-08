# zebra

- 這個插件以斑馬(zebra)，靈感來自於阿蘭 圖靈(Allen Turling)所提出的圖靈斑紋(turling pattern)，指的是動物在生長過程中，因帶有不同色素的細胞在擴散量與擴散速度的差異下互相作用，所產生的不同型態的斑紋。
- 這同時代表著，在一個無序狀態下的模型，透過對應的邏輯，將其轉換成有序且符合機器人工作的資料結構，這也同時呼應了點的所包含的數據資料，不單單只有位置資訊，而同時容納工作平面、速度、擠出量等參數。
- This tool is applied to optimization the workflow of the robotic 3d concrete printing.

- __author__     = ['Avery Tsai']
- __email__      = ['n76124052@gs.ncku.edu.tw']

---
## design_model

### 1_points
#### 1. List Points ([0],[0])
#### 2. Flatten Points ([0])
#### 3. Graft Points ([0, 0])

### 2_surface

### 3_mesh

---
## slicing_tool
- This is order to translate design object to sorted vertexes data structure.
- input
  - object : Surface, Mesh
- output
  - curve: List
  - points: List

### surface_slicing

### mesh_slicing

---
## optimizition_tool
- This tool is order to optimize robotic working path and layers vertex structure.
- input:
  - curve: List
  - points: list

### divideCurve_byCurvature


### sorted_points
### control_sorted_points


---
## analysis_tool

- input:
  - curve: List
  - points: List
  - mesh: -

### 1_points

### 斜率分析

### 疊合比例分析

---
## pathDesign_tool

### secendPath_generate

### pattern_generate

---
## roboticPrinting_tool

### slicingbyLayers(分段切片工具)

### printingBaseModule

### jointSection

---
## View
