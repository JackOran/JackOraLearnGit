## frame-vector-3.0记录

画板载入

- 传入type-name     **type-name="trans"** 

- 传入type-class      **:type-class="TMGridModule"**

- 获取moduleList，判断moduleList是否包含this.moduleName

  - ```js
    //包含的话直接获取
    const mod = DFManager.modules.getModuleByName(this.moduleName);
    this.graphView = mod.createGraphView();
    //没有包含的话，注册
    const mod = new this.typeClass();
    DFManager.modules.registerModule(mod);
    this.graphView = mod.createGraphView();
    ```