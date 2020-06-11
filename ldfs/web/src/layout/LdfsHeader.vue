/* eslint-disable */
<template>
<div>
	<div class="mainHeader">
		<!--浏览器版本检测-->
      	<div class="brower-version-prompt" v-show="version_prompt">
  			<div class="left-prompt-info">
	          	<div class="warn-icon"></div>
	          	<span>当前浏览器部分功能不支持,推荐使用<strong>Chrome</strong>及<strong>IE11</strong>浏览器</span>
        	</div>

	        <div class="right-prompt-info">
		    	<el-checkbox v-model="checkbox">不再提醒</el-checkbox>
		      	<div class="cancel-icon" @click="version_prompt=false"></div>
	        </div>
	    </div>
        <!--网页顶部-->
        <div id="headerContainer">
        	<div id="userInfo">
        		<a>{{username}}</a>
        	</div>
        </div>
    </div>
</div>
</template>

<script>

	// matStat将一个对象或数组里的值转化成计算属性的写法。
	// 将传入的数组或对象转成 computed 计算属性能够识别的代码。
	//import {mapState} from "vuex";

	export default {
		name:"LdfsHeader",
		data(){
			return {
				checkbox: false,
				version_prompt: false
			}
		},
		mounted(){
		 	// vue实例挂载的事件钩子函数，它只会执行一次
			this.currentYear = new Date().getFullYear();
			this.check_brower_version();
		},
		computed: {
			//...mapState(['username']);
			username(){
			  return "admin";
			}
		},
		methods:{
			check_brower_version(){
				// navigator.appVersion 浏览器的版本号
				// navigator.appName 浏览器的名称
				// navigator.language 浏览器使用的语言
				// navigator.platform 浏览器使用的平台
				// navigator.userAgent 浏览器的user-agent信息
				let userAgent = navigator.userAgent;
				try{
					let current_brower = this.getCurrentBrower();
					let brower_version = parseInt(this.getBrowerVersion());
					this.show_lower_version_prompt(current_brower, brower_version);
				}catch (e) {
					this.version_prompt = true;
				}

			},
			getBrowerVersion(){
				var userAgent = navigator.userAgent; //取得浏览器的userAgent字符串
		        let version;
		        if (userAgent.indexOf("Firefox") > -1) {
		          	version = userAgent.match(/firefox\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		          	return version;
		        } else if (userAgent.indexOf("Edge") > -1) {
		          	version = userAgent.match(/edge\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		          	return version;
		        } else if (userAgent.indexOf("Opera") > -1 || userAgent.indexOf("OPR") > -1) {
		          	if (userAgent.indexOf("Opera") > -1) {
		            	version = userAgent.match(/opera\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		            	return version;
		          	}
		          	if (userAgent.indexOf("OPR") > -1) {
		            	version = userAgent.match(/opr\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		            	return version;
		          	}
		        } else if (userAgent.indexOf("Chrome") > -1) {
		          	version = userAgent.match(/chrome\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		          	return version;
		        } else if (userAgent.indexOf("Safari") > -1) {
		          	version = userAgent.match(/safari\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		          	return version;
		        }
		        else if (userAgent.indexOf("MSIE") > -1 || userAgent.indexOf("Trident") > -1) {
		          	if (userAgent.indexOf("MSIE") > -1) {
		            	version = userAgent.match(/msie [\d.]+/gi)[0].match(/[\d]+/)[0];
		            	return version;
		          	}
		          	if (userAgent.indexOf("Trident") > -1) {
		            	versionTrident = userAgent.match(/trident\/[\d.]+/gi)[0].match(/[\d]+/)[0];
		            	version = parseInt(versionTrident) + 4;
		            	return version;
		          }
		        }

			},
			show_lower_version_prompt(b ,v){
				// b=brower obj, v= version int
				if (b == "Firefox" && v <= 28){
					this.version_prompt = true;
				} else if (b == "Opera" && v <= 17){
					this.version_prompt = true;
				} else if (b == "Chrome" && v <= 17){
					this.version_prompt = true;
				} else if (b == "Safari" && v <= 6){
					this.version_prompt = true;
				} else if (b == "IE" && vn <= 10){
					this.version_prompt = true;
				} else {

				}
			},
			getCurrentBrower(){
				let userAgent = navigator.userAgent;
				if (userAgent.indexOf("Firefox") > -1) {
          			return "Firefox";
		        } else if (userAgent.indexOf("Edge") > -1) {
		          return "Edge";
		        } else if (userAgent.indexOf("Opera") > -1 || userAgent.indexOf("OPR") > -1) {
		          return "Opera";
		        } else if (userAgent.indexOf("Chrome") > -1) {
		          return "Chrome";
		        } else if (userAgent.indexOf("Safari") > -1) {
		          return "Safari";
		        } else if (userAgent.indexOf("MSIE") > -1 || userAgent.indexOf("Trident") > -1) {
		          return "IE";
		        }
			},
		}
	}
;
</script>



<style scoped>
  
  /*头部样式*/
  .mainHeader {
    width: 100vw;
    height: 98px;
    background-color: #373d41;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
  }

  #headerContiner {
    height: 98px;
    margin: 0 128px 0 128px;
    position: relative;
  }

  .mainHeader #logo {
    float: left;
    margin: 36px 0 0 0;
  }

  .mainHeader .btnContainer a#exit:hover {
    background-position: 72px 0;
  }

  .mainHeader .btnContainer a#exit:active {
    background-position: 48px 0;
  }


  .mainHeader #userInfo {
    height: 12px;
    float: right;
    margin: 42px 18px 0 0;
    color: #ffffff;
    font: 12px/12px Microsoft YaHei;
  }

  .mainHeader #userInfo a:hover {
    color: #ffffff;
    text-decoration: none;
    cursor: pointer;
  }


  .v-model {
    flex: none;
  }

  .brower-version-prompt {
    background-color: #fffde4;
    position: fixed;
    width: 100%;
    height: 32px;
  }

  .right-prompt-info {
    float: right;
    padding-top: 9px;
    font-size: 12px;
  }

  .warn-icon {
    width: 18px;
    height: 18px;
    float: left;
    background: url("../assets/images/prompt_browser.png");
    margin-right: 10px;
  }

  .left-prompt-info {
    margin-left: 20px;
    display: inline-block;
    float: left;
    padding-top: 9px;
    font-size: 12px;
  }

  .cancel-icon {
    width: 13px;
    height: 13px;
    float: right;
    margin: 3px 20px 0 30px;
    cursor: pointer;
    display: inline-block;
    background: url("../assets/images/delete.png");
  }

  .cancel-icon:hover {
    background: url("../assets/images/delete.png") -13px 0;
  }
</style>


