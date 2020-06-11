import Vue from 'vue'
import App from './App'
import Element from 'element-ui';

import router from '@/router';
import store from '@/store';


// import css
import './assets/css/common.css';


import 'vx-easyui/dist/themes/default/easyui.css';
import 'vx-easyui/dist/themes/icon.css';
import 'vx-easyui/dist/themes/vue.css';
// ui
import EasyUI from 'vx-easyui';
import './assets/css/reset-easyui.css';
import './assets/css/reset.css';
// api axios 
import axios from "./apiaxios/axios";
Vue.prototype.axios = axios;
// echart
import Echart from "echarts";
Vue.prototype.echart = Echart;

Vue.use(EasyUI);
Vue.use(Element);
Vue.use(Echart);

// prompt
import prompt from '@/prompts/prompt'
Vue.use(prompt.promptDialog);
Vue.use(prompt.successDialog);

// Vue.config.productionTip = false;


/* eslint-disable no-new */
const fsm = new Vue({
  el: '#app',
  router,
  // store,
  components: { App },
  template: `<App/>`
});

export default fsm
