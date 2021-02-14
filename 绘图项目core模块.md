### EventComp(事件基础类)

- 属性
  - eventListeners (事件监听)
  - _beginUpdateCounter(开始更新数量)
  - _cacheEvent(缓存事件)
  
- 方法
  - on
  - _off
  - off
  - _fire
  - fire
  - cachefire
  - beginUpdate
  - endUpdate
  
- **DrawShapeProxy(元件显示代理类，方便以后扩展，如一类元件不显示，或不显示参数)**

  - draw() //绘图
  - layer() //层

- **DFModule(模块基类)**

  - endableDesgined() //是否可以设计子元件
  - devInfoList() //设备信息列表
  - **CadModule(封装与绘图相关的模块信息)**
    - createGraphView()  //创建视图
    -  stencilLib() //本模块的元件库画法

- **Layer(视图显示层)**

  - visible() //层是否可见
  - editable() //层是否可编辑
  - dataModel() //层对应的dataModel
  - ower() //返回所属的Layer
  - searchAlign() //搜索对齐点
  - searchShapeTerminals() //搜索元件连接点
  - graphView() //层显示的视图
  - **CanvasLayer(画布层)**
  - **HeatMapLayer(热图层)**
  - **ShapeLayer(显示元件的层)**
    - drawProxy() //显示代理，通过设置显示代理来控制元件的显示
    - shapeList() //元件列表
    - draw() //绘制本层
    - searchAlign() //搜索对齐点
    - searchShapeTerminals() //搜索元件终点

- **BaseSetting(基础设置基类，每一个模块应有相应的设置)**
  
  - canDrawShape() //元件是否要绘制
  - canDrawShapeParameter() //元件的参数是否要绘制
  - drawLinkPoint() //是否显示连接点
  - TMGridSettings
    - formatParameter() //对传入的shape进行设置
    - canDrawShape()     //元件是否要绘制
  
- **Selections(视图选择管理类)**

  - selectedShape()  //选中的元件或元件列表
  - selectShapes() //将shapes中所有的元件选中
  - clear() //清除选中元件
  - beginSelect() //开始进行选择操作
  - endSelect() //结束选择操作
  - graphView() //获取所属元件的视图
  - addSelectShape() //将元件选中
  - deleteSelectedShaped() //删除选中的元件

- **GraphView(基础视图类)**

  - canvas() //视图画布
  - originPos() //视图的左上角坐标
  - scale() //视图的放大缩小系数
  - getZoomIn() //得到的新的放大系数
  - getZoomOut() //得到新的缩小系数
  - width() //视图宽度
  - height() //视图高度
  - pixelRatio() //分辨率
  - layer() //视图中所有层
  - redraw() //刷新画布
  - viewerMatrix() //得到视图的显示矩阵
  - screenToWorld() //屏幕坐标转换为世界坐标
  - worldToScreen() //世界坐标转换为屏幕坐标
  - **ModuleGraphView(模块视图类,整合事件,工具,模块)**
    - doCreateShapeList() //默认创建的ShapeList
    - doCreateIncrementalUpdate() //创建增量更新
    - doCreateEventListener() //创建默认的事件监听
    - doCreateDrawProxy() //创建默认的显示代理
    - createDefaultTools() //每一个视图都需要的工具
    - createCustomTools() //创建视图专用工具
    - createStencilTool() //创建StencilShape的工具

- **DefaultEventListener(默认的事件监听类)**

  - hotKeyList() //热键列表
  - graphView() //获取所属元件的视图
  - bindEvent() //绑定事件
  - unBindEvent() //解除绑定事件

- **DataPlugin(数据插件基类)**

  - ower() //所属的ShapeList
  - name() //name
  - **ModuleDataPlugin(模块数据插件)**
    - onEndLoadFromJSON
  - **TopoManager(拓扑排序)**
    - find() //根据TerminalId查询相应的ConnectivityNode
    - fixLoadFromJson() //在loadFromJSON时，有可能shape未能载入，在全部载入后，需要修正Terminals的属性
    - findTerminals() //在指定的矩形中查找连接点
    - _DealWithUnLimitedLinks() //对无限连接点的元件进行拓扑分析
    - getLinkedShapes() //根据连接点，返回所有连接的元件
  - **IDManagerPlugin(ID管理插件)**
    - allocateId() //分配ID
    - removeId()  //移除id
    - onDataAdd() //元件增加到列表时,检查是否重复的ID
    - onDataRemove()  //移除数据id
  - **ShapeBoundManager(元件大小范围管理类,快速定位交互的元件)**
    - onDataAdd() //增加一个元件
    - onDataRemove() //移除一个元件
    - addShape() //增加一个元件
    - onShapeTransformChanged() //元件尺寸\位置改变时,重新更新列表
    - intesectRect() //查找与指定矩形相交的元件列表
  - **EdgeManagerPlugin(边界管理插件)**
    - onDataAdd() //增加一个边缘元件
    - onDataRemove() //移除一个边缘元件
    - edgeLayoutAgentList
    - onEndLoadFromJSON

- **ToolBase(基本工具类)**

  - ```markdown
    /**
       * 基本工具类
       * caption : 标题
       * icon : 图标的name
       * istoggled : 是否有按下和非按下状态
       * enabled : 是否用可
       * group : group名称,同一组中只有一个是可按下的
       * tooltip : 提示
       * tag :
       * hotkey : 热键
       * name : 工具名称
       * visible : true 可见 false 隐藏
       * beginGroup : 是否开始新的分组
       */
    ```

  - icon() //获取图标的name

  - enabled() //是否可用

  - executeHandler() //执行处理

  - **ViewerTool(视图工具)**

    - viewer() //获取视图

  - **CadToolBase(基础视图工具)**

    - isContinueAction() //是否连续使用此工具，如否，使用一次之后会自动返回到默认工具
    - **CanvasTool(画布工具)**
      - useWheelZoom() //是否允许鼠标滚轮缩放图形
      - toolStates() //工具状态
      - **CreateShapeTool(在GraphView中创建Shape的工具类)**
        - canCreateShape() //是否可以创建shape
        - createShapeAndAddToList() //创建元件并添加到列表中
        - **LineTool(创建直线工具)**
          - **RectTool(创建矩形工具)**
        - **LinkShapeTool(增加连接点)**
          - createShape() //从坐标集中创建元件
      - **SelectTool(选择工具，默认工具)**
        - doMouseMove() //鼠标移动
        - _drawRect() //画矩形
      - **PasteTool(粘贴工具类)**
        - onAfterCreateAssistant() //由于StencilShape的ChildShapes不保存到JSON中,所以需要设置ModuleDataPlugin用于将画法重新获取
        - loadShapes() //加载元件
        - **StencilTool(创建StencilShape工具)**
          - stencilShape() //获取stencil元件
    
  - **CopyTool(复制选中的元件)**

    - execute() //执行复制

  - **DeleteShapeTool(删除选中的元件)**

    - execute() //执行删除

  - **CutShapeTool(删除选中的元件，并复制到剪贴板上)**

    - execute() //执行删除选中的元件，并复制懂啊剪贴板上

  - **GraphViewFitContentTool(整图显示)**

    - execute() //执行整图显示

- **Tlist(列表的基础类，对数组封装，实现数据的增加，删除，替换)**
  
  - 方法
    - length()    //获取长度
    - getItem()  //根据索引获取数据
    - add()         //添加数据到列表
    - remove()  //移除数据
    - delete()    //根据索引删除数据
    - clear()      //清除数据
    - indexOf() //数组的索引号
    - toArray()  //转换为数组
    - exchange() //互换两个位置的元素
  - **DataModel(数据模型的基类)**
    - 方法
      - graphView(所属原件的视图)
      - getShape(根据索引获取数据)
      - findShape(根据id查找原件)
      - orderByShape(按DataModel中的原件进行排序)
      - getAllShapeboundRect(得到全部原件的矩形)
    - **ShapeList(图形元件列表管理类,使用数据插件技术对元件进行管理)**
    - **ShapeReader(元件读取类)**
      - 方法
        - shapesBoundManager() //边界管理
        - topoManager() //拓扑管理
        - IDManager() //Id管理
        - add()
        - onShapePropertyChanged() //原件属性发生变化时，需要进行消息广播
        - onShapeFree()  //释放
        - remove() //移除数据
        - exchange() //互换两个位置的元素
        - toJSON() //转换为JSON串
        - isLoading() //是否正在从JSON中读取
        - loadFromJSON()  //从JSON中读取数据
        - copyFromShapeList() //从另一个ShapeList中复制所有元件,本ShapeList复制前的元件将被清除
        - toImage() //生成图标
        - findShapeByClassId() //根据Shape的ShapeClassID，获取相应的元件列表
      - **ChildShapeList(子元件列表， 如变压器，由一系列子元件组成)**
        - 方法
          - owerShape() //获取自己的原件
            - 类ShapeProperty  //元件属性列表类
              - 方法
                - add() //添加属性
                - setPropertyVisible() //设置属性是否可见
                - changeProperty() //改变属性的的属性
                - hideAllPropertys() //将所有属性设为隐藏
                - getEditablePropertys() //得到所有可见的属性
                - deleteProperty() //删除属性
          - getGroupShapes() //获取指定分组的子元件
          - copyFromShapeList() //从另一个ShapeList中复制所有元件,本ShapeList复制前的元件将被清除
          - getOutLineShapes() //获取最外层的元件列表
      - **StencilLib(管理本模块中所有可设计原件列表)**
        - add() //添加原件
          - super.add(shape, index)
        - find() //根据条件查找元件的画法
        - getStencilList() //获取一类元件的所有画法
        - getStencilDrawIdList() //获取一类元件所有状态元件列表
        - deleteStencil() //删除元件
        - rebuildStencil() //根据Shape的DrawID和StatusID重新加载子元件和连接点
        - newStencilShape() //根据类ID和第一个连接点位置创建实体StencilShape
  - **PointList(Point列表)**
    - getItem() //重写GetItem，返回复制过的点
    - toJSON() //生成JSON
    - loadFromJSON() //从JSON中读取数据
    - debug()
  - **SortList(排序列表的基类)**
    - findNextEqua()  //是否继续查找下一个相等的数据
    - comp() //比较两个数据
    - find() //为数据Item查找合适的位置
    - adds() //批量增加
    - **XYSortList(元件边界管理)**
      - deleteShape()  //删除元件
      - getItemByName() //通过元件来获取数据
  - **DataPluginManager(数据插件管理器，shapeList使用数据插件机制来扩展相应的功能对数据进行增加，删除，获取，写入，开始更新，结束更新)**
    - ower() //获取所属的shapeList
    - add() //添加数据到列表
    - remove() //移除数据
    - getPluginByName() //根据名称获取插件
  - **Layers(Layer管理器)**
    - add() //添加层到列表中
    - checkLayerIndex() //检查层索引
    - getLayerById() //根据Id获取相应的图层
    - searchAlign() //搜索对齐点
    - searchShapeInDrawedShapes() //在屏幕上绘制的元件中，查找指定条件的元件
    - getAllLayerBoundRect() //获取所有Layer的BoundRect
    - draw() //所有图层绘制
    - isEmptyDataModule() //是否是空的数据模型
  - **ConnectivityNodes**
    - add() 
    - remove()
    - find() //查找指定的TerminaId所在的ConnectivityNode
    - findConnectivityNode() //根据id查找ConnectivityNode
  - **ConnectivityNode(连接信息,在Items中的所有Terminal都连接在一起)**
    - clear()
    - add()
    - checkOneTerminal() //检查是否存在一个Terminal的情况,如果有的话,需要移除
    - remove() //移除
    - deleteTerminal() //删除Terminal
    - getTerminalList() //得到Terminal列表
    - getTerminalListNum() //获取Terminal列表长度
  - **DFModuleList(模块列表)**
    - registerModule() //注册模块
    - getModuleByName() //获取模块名称
    - getDevInfo() //获取设备信息
  - **ToolList(工具列表类)**
    - getToolByName() //根据名称获取工具
    - removeToolByName() //根据名称删除工具 