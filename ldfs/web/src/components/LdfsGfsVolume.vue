<template>
<div>
<div class="div_top">
	<div class="sysinfo-item-group">
        <div class="text-title-1">GFS卷信息</div>
        <input type="button" value="新建卷" class="mo-btn-x mo-btn-gray AddBtn" @click="addVolume">
    </div>
	<el-table :data="data" style="width:100%" ref="multipleTable" height="690px" :highlight-current-row="true">
        <el-table-column type="index" label="序号" width="32"
        :index="(paginations_num.current_page-1)*20+1"></el-table-column>
        <el-table-column prop="VolumeName" label="卷名称" min-width="60" :show-overflow-tooltip="true"></el-table-column>
        <el-table-column prop="Status" label="在线状态" min-width="50" :show-overflow-tooltip="true"></el-table-column>
        <el-table-column prop="NumberofBricks" label="Brick数量" min-width="50" :show-overflow-tooltip="true">
        	<template slot-scope="scope">
          		<a class="optionlink" @click="getBricks(scope.$index)">{{scope.row.NumberofBricks}}</a>
        	</template>
        </el-table-column>
        <el-table-column prop="VolumeID" label="UUID" min-width="244" :show-overflow-tooltip="true"></el-table-column>
        <el-table-column label="操作" min-width="100" :show-overflow-tooltip="true">
	        <template slot-scope="scope">
	          <a class="optionlink" @click="start_vol(scope.row.VolumeName)" v-if="scope.row.Status==='Stopped'">启用卷</a>
	          <a class="optionlink" @click="start_vol(scope.row.VolumeName)" 
	          v-else-if="scope.row.Status ==='Created'">启用卷</a>
	          <a class="optionlink" @click="stop_vol(scope.row.VolumeName)" 
	          v-else>停用卷</a>
	        </template>
        </el-table-column>
    </el-table>
    <pagination :paginations_num.sync="paginations_num"></pagination>

    <artDialog ref="gfsArt" :height="'h_art'+'px'" :title="'新建卷'" @detemine="detemine" @closed="cancelDialog">
      <template>
        <div class="scope-content-top">
          <div>
            <span class="scope-item-name">请输入卷名称：</span>
            <input class="scope-item-value" type="text" placeholder="gvol" style="line-height: 20px" v-model="volname">
            <span class="scope-item-name">请输入副本数：</span>
            <input class="scope-item-value" type="text" placeholder="replica" style="line-height: 20px" v-model="replica">
            <span class="scope-item-name">请输入brick：</span>
            </br>
            <input class="scope-item-value-long" type="text" placeholder="brick" style="line-height: 20px" v-model="inputbrick">
            <input type="button" value="添加" class="mo-btn-x mo-btn-gray ScopeBtn" @click="addBricks">
            <span class="scope-item-name">当前已添加：</span>
            <ul v-for="bk in inputbricks">
            	<li style="border:1px solid red">{{bk}}</li>
            </ul>

          </div>
        </div>
      </template>
    </artDialog>
    <artDialog ref="brickArt" :height="'125px'" :title="'Bricks展示'" @detemine="bricksShow" @closed="cancelDialog">
      <template>
        <div class="scope-content-top">
          <div>
            <ol v-for="(bk,index) in bricks">
            	<li>{{index + 1}}: {{bk}}</li>
            </ol>
          </div>
        </div>
      </template>
    </artDialog>
</div>
</div>
</template>

<script>
import Pagination from "@/common/pagination";
import artDialog from "./artDialog";
export default {
	name: "LdfsGfsVolume",
	components: {Pagination, artDialog},
	data(){
		return {
			data: [],
			bricks:[],
			inputbricks:[],
			volname: "",
			replica: 0,
			inputbrick:"",
			h_art:"125",
			paginations_num: {
	            current_page: 1,
	            total_page: 1
	        },
		}
	},
	mounted() {
		this.search();
	},
	methods: {
		search(page = 1){
			this.axios.get("/ldfs/api/v1/gfs/volume", {params: {'page':page}}).then(res => {
	          	this.data = res.data.data;
	          	this.paginations_num.total_page = res.data.total;
	        }).catch(error => {
	          	console.log("服务器连接失败");
	        })
		},
		start_vol(volname){
			console.log(volname);
			this.axios.put("/ldfs/api/v1/gfs/volume", {'volname': volname}).then(res => {
	        this.$prompt.instance.promptClose();
	        if (res.data.code === 0) {
	            this.$successPrompt.success(
		            {
		                dialogVisible: true,
		                content: "卷启用成功",
		            }
	            );
	            this.search()
	        } else {
	            this.$prompt.success({
	                dialogVisible: true,
	                content: `卷启用失败,<br>` + res.data.msg,
	                error: true
	            });
	          }
	        });
		},
		stop_vol(volname){
			console.log(volname);
			this.axios.delete("/ldfs/api/v1/gfs/volume", {data:{'volname': volname}}).then(res => {
	        this.$prompt.instance.promptClose();
	        if (res.data.code === 0) {
	            this.$successPrompt.success(
		            {
		                dialogVisible: true,
		                content: "停用卷成功",
		            }
	            );
	            this.search()
	        } else {
	            this.$prompt.success({
	                dialogVisible: true,
	                content: `停用卷失败,<br>` + res.data.msg,
	                error: true
	            });
	          }
	        });
		},
		addVolume(){
			this.$refs.gfsArt.openBackup();
		},
		cancelDialog() {
        	
     	},
		detemine(){
			this.axios.post("/ldfs/api/v1/gfs/volume", {'volname': this.volname, 'bricks': this.inputbricks, 'replica': this.replica}).then(res => {
	        this.$prompt.instance.promptClose();
	        if (res.data.code === 0) {
	            this.$successPrompt.success(
		            {
		                dialogVisible: true,
		                content: "卷添加成功",
		            }
	            );
	            this.search()
	        } else {
	            this.$prompt.success({
	                dialogVisible: true,
	                content: `卷成员失败,<br>` + res.data.msg,
	                error: true
	            });
	          }
	        });
		},
		getBricks(index){
			this.bricks = this.data[index].bricks;
			this.$refs.brickArt.openBackup();
		},
		bricksShow(){

		},
		addBricks(){
			if (this.inputbricks.length) {
		        let repeatFlag = this.inputbricks.some(el => {
		        	if (el == this.inputbrick) return true
		      	})
		      	if (repeatFlag) {
		        	console.log('当前参数值重复,不能添加');
		      	} else {
			        this.inputbricks.push(this.inputbrick)
			        this.inputbrick = ''
		      	}
		    } else {
		      this.inputbricks.push(this.inputbrick)
		      this.inputbrick = ''
		    }
		},
	},
	watch: {
        "paginations_num.current_page": function (newVal, oldVal) {
            this.search(newVal)
        }
    },
}
</script>

<style scoped>
    .div_top {
    	margin-top: 15px;
    }
   .text-title-1{
	    font-size: 14px;
	    font-weight: bold;
	    display: inline-block;
	    width: 92px;
	    color: #8b8b8b;
	}
	.AddBtn {
	    float: right;
	    margin-top: 18px;
  	}
  	.scope-content-top {
	    margin-top: 21px;
	    margin-left: 75px;
 	}
 	.scope-item-name {
	    width: 100px;
	    display: inline-block;
	    vertical-align: bottom;
	    margin-bottom: 6px;
	    //border:1px solid red;
    }
    .scope-item-value {
    	width: 100px;
    	vertical-align: bottom;
    	margin-bottom: 6px;
    	display: inline-block;
    }
    .scope-item-value-long{
    	width: 200px;
    	vertical-align: bottom;
    	margin-bottom: 6px;
    	display: inline-block;
    }
    .scope-item-value-longs{
    	width: 200px;
    	vertical-align: bottom;
    	margin-bottom: 6px;
    	display: inline-block;
    }
    .ScopeBtn {
    	float: right;
    }

</style>