import promptTemplate from './globalcomp/prompt';
import successPromptTemplate from './globalcomp/successprompt';
import base from './base'


const promptDialog = {
  install(Vue) {
    // 同时这个子类也就是组件
    const promptConstructor = Vue.extend(promptTemplate);
    // 生成一个该子类的实例
    const instance = new promptConstructor();

    // 将这个实例挂载在我创建的div上
    instance.$mount(document.createElement('div'));

    // 并将此div加入全局挂载点内部
    document.body.appendChild(instance.$el);

    //定义一个外部的变量，用于控制调用多次提示组件时，清除延时器
    Vue.prototype.$prompt = base(instance)
  }
};

const successDialog = {
  install(Vue) {
    // 同时这个子类也就是组件
    const successPromptConstructor = Vue.extend(successPromptTemplate);
    // 生成一个该子类的实例
    const instance = new successPromptConstructor();

    // 将这个实例挂载在我创建的div上
    instance.$mount(document.createElement('div'));

    // 并将此div加入全局挂载点内部
    document.body.appendChild(instance.$el);

    //定义一个外部的变量，用于控制调用多次提示组件时，清除延时器
    Vue.prototype.$successPrompt = base(instance)
  }
};

const prompt = {
  promptDialog,
  successDialog
};

export default prompt
