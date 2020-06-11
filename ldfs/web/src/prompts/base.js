class BaseTemplate {
  /**
   *
   * @param instance 模板实例
   */
  constructor(instance) {
    this._instance = instance;
  }
  promptDialogOprate(kwargs) {
    let keys = Reflect.ownKeys(kwargs);
    keys.forEach(k=>this._instance[k]=kwargs[k])
  }
  success(kwargs) {
    this.promptDialogOprate(kwargs);
  }
  error(kwargs) {
    this.promptDialogOprate(kwargs);
  }
  get instance() {
    return this._instance;
  }
}

function base(instance){
  return new BaseTemplate(instance)
}

export default base
