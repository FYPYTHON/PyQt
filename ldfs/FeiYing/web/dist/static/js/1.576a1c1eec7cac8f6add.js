webpackJsonp([1],{Nfr2:function(e,r,t){"use strict";var i={name:"LdfsHeader",data:function(){return{checkbox:!1,version_prompt:!1}},mounted:function(){this.currentYear=(new Date).getFullYear(),this.check_brower_version()},computed:{username:function(){return"admin"}},methods:{check_brower_version:function(){navigator.userAgent;try{var e=this.getCurrentBrower(),r=parseInt(this.getBrowerVersion());this.show_lower_version_prompt(e,r)}catch(e){this.version_prompt=!0}},getBrowerVersion:function(){var e=navigator.userAgent;if(e.indexOf("Firefox")>-1)return e.match(/firefox\/[\d.]+/gi)[0].match(/[\d]+/)[0];if(e.indexOf("Edge")>-1)return e.match(/edge\/[\d.]+/gi)[0].match(/[\d]+/)[0];if(e.indexOf("Opera")>-1||e.indexOf("OPR")>-1){if(e.indexOf("Opera")>-1)return e.match(/opera\/[\d.]+/gi)[0].match(/[\d]+/)[0];if(e.indexOf("OPR")>-1)return e.match(/opr\/[\d.]+/gi)[0].match(/[\d]+/)[0]}else{if(e.indexOf("Chrome")>-1)return e.match(/chrome\/[\d.]+/gi)[0].match(/[\d]+/)[0];if(e.indexOf("Safari")>-1)return e.match(/safari\/[\d.]+/gi)[0].match(/[\d]+/)[0];if(e.indexOf("MSIE")>-1||e.indexOf("Trident")>-1){if(e.indexOf("MSIE")>-1)return e.match(/msie [\d.]+/gi)[0].match(/[\d]+/)[0];if(e.indexOf("Trident")>-1)return versionTrident=e.match(/trident\/[\d.]+/gi)[0].match(/[\d]+/)[0],parseInt(versionTrident)+4}}},show_lower_version_prompt:function(e,r){"Firefox"==e&&r<=28?this.version_prompt=!0:"Opera"==e&&r<=17?this.version_prompt=!0:"Chrome"==e&&r<=17?this.version_prompt=!0:"Safari"==e&&r<=6?this.version_prompt=!0:"IE"==e&&vn<=10&&(this.version_prompt=!0)},getCurrentBrower:function(){var e=navigator.userAgent;return e.indexOf("Firefox")>-1?"Firefox":e.indexOf("Edge")>-1?"Edge":e.indexOf("Opera")>-1||e.indexOf("OPR")>-1?"Opera":e.indexOf("Chrome")>-1?"Chrome":e.indexOf("Safari")>-1?"Safari":e.indexOf("MSIE")>-1||e.indexOf("Trident")>-1?"IE":void 0}}},n={render:function(){var e=this,r=e.$createElement,t=e._self._c||r;return t("div",[t("div",{staticClass:"mainHeader"},[t("div",{directives:[{name:"show",rawName:"v-show",value:e.version_prompt,expression:"version_prompt"}],staticClass:"brower-version-prompt"},[e._m(0),e._v(" "),t("div",{staticClass:"right-prompt-info"},[t("el-checkbox",{model:{value:e.checkbox,callback:function(r){e.checkbox=r},expression:"checkbox"}},[e._v("不再提醒")]),e._v(" "),t("div",{staticClass:"cancel-icon",on:{click:function(r){e.version_prompt=!1}}})],1)]),e._v(" "),t("div",{attrs:{id:"headerContainer"}},[t("div",{attrs:{id:"userInfo"}},[t("a",[e._v(e._s(e.username))])])])])])},staticRenderFns:[function(){var e=this.$createElement,r=this._self._c||e;return r("div",{staticClass:"left-prompt-info"},[r("div",{staticClass:"warn-icon"}),this._v(" "),r("span",[this._v("当前浏览器部分功能不支持,推荐使用"),r("strong",[this._v("Chrome")]),this._v("及"),r("strong",[this._v("IE11")]),this._v("浏览器")])])}]};var a=t("VU/8")(i,n,!1,function(e){t("ShQI")},"data-v-567f0742",null);r.a=a.exports},ShQI:function(e,r){},ZWLk:function(e,r){},sCCV:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0});t("Nfr2");var i={render:function(){var e=this.$createElement,r=this._self._c||e;return r("div",{staticClass:"wrap-outer"},[r("router-view")],1)},staticRenderFns:[]};var n=t("VU/8")({name:"MainPage"},i,!1,function(e){t("ZWLk")},"data-v-68b43034",null);r.default=n.exports}});
//# sourceMappingURL=1.576a1c1eec7cac8f6add.js.map