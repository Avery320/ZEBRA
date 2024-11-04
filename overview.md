# zebra

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
1. 單層
2. 雙層

---
## View

# 造型工具

## 幾何工具


## 表面紋理工具

### mappingTool

## 內層結構生成工具
1. 圓形
2. 多邊形
  
## fillInPattern

### 三角形
1. 數量
2. 密度


# 試體工具

## basicShape
### 方形

## 基本試驗工具

### pathTest
### 
### 

