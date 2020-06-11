<template>
<div>
<div class="div_top">
	<div class="sysinfo-item-group">
        <div class="text-title-1">GFS集群信息</div>
        <input type="button" value="添加成员" class="mo-btn-x mo-btn-gray AddBtn" @click="addPeer">
    </div>
	<el-table :data="data" style="width:100%" ref="multipleTable" height="690px" :highlight-current-row="true">
        <el-table-column type="index" label="序号" width="32"
        :index="(paginations_num.current_page-1)*20+1"></el-table-column>
        <el-table-column prop="hostname" label="服务器名称" min-width="60" :show-overflow-tooltip="true"></el-table-column>
        <el-table-column prop="state" label="在线状态" min-width="50" :show-overflow-tooltip="true"></el-table-column>
        <el-table-column prop="uuid" label="UUID" min-width="244" :show-overflow-tooltip="true"></el-table-column>
        <el-table-column label="操作" min-width="50" :show-overflow-tooltip="true">
	        <template slot-scope="scope">
	          <a class="optionlink" @click="delete_peer(scope.row.hostname)">删除成员</a>
	        </template>
        </el-table-column>
    </el-table>
    <pagination :paginations_num.sync="paginations_num"></pagination>

    <artDialog ref="gfsArt" :height="'125px'" :title="'添加新成员'" @detemine="detemine" @closed="cancelDialog">
      <template>
        <div class="scope-content-top">
          <div>
            <span class="scope-item-name">请输入待添加成员名称：</span>
            </br>
            <input type="text" placeholder="hostname" style="line-height: 20px" v-model="inputhost">
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
	name: "LdfsGfsView",
	components: {Pagination, artDialog},
	data(){
		return {
			data: [],
			inputhost: "",
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
			this.axios.get("/ldfs/api/v1/gfs", {params: {'page':page}}).then(res => {
	          	this.data = res.data.data;
	          	this.paginations_num.total_page = res.data.total;
	        }).catch(error => {
	          	console.log("服务器连接失败");
	        })
		},
		delete_peer(hostname){
			console.log(hostname);
			this.axios.delete("/ldfs/api/v1/gfs", {data:{'hostname': hostname}}).then(res => {
	        this.$prompt.instance.promptClose();
	        if (res.data.code === 0) {
	            this.$successPrompt.success(
		            {
		                dialogVisible: true,
		                content: "成员删除成功",
		            }
	            );
	            this.search()
	        } else {
	            this.$prompt.success({
	                dialogVisible: true,
	                content: `删除成员失败,<br>` + res.data.msg,
	                error: true
	            });
	          }
	        });
		},
		addPeer(){
			this.$refs.gfsArt.openBackup();
		},
		cancelDialog() {
        	
     	},
		detemine(){
			this.axios.post("/ldfs/api/v1/gfs", {'hostname': this.inputhost}).then(res => {
	        this.$prompt.instance.promptClose();
	        if (res.data.code === 0) {
	            this.$successPrompt.success(
		            {
		                dialogVisible: true,
		                content: "成员添加成功",
		            }
	            );
	            this.search()
	        } else {
	            this.$prompt.success({
	                dialogVisible: true,
	                content: `添加成员失败,<br>` + res.data.msg,
	                error: true
	            });
	          }
	        });
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
	    margin-top: 41px;
	    margin-left: 75px;
 	}
 	.scope-item-name {
	    width: 200px;
	    display: inline-block;
	    vertical-align: bottom;
	    margin-bottom: 12px;
    }

</style>