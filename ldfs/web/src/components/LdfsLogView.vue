<template>
  <div>
    <div class="div_choice">
      <input type="text" placeholder="请输入关键词" style="line-height: 20px" v-model="key">
      <div style="display: inline-block; width: 19px"></div>
      <el-select v-model="operator" placeholder="operatorTypeList">
        <el-option
          v-for="item in operatorTypeList"
          :key="item"
          :label="item"
          :value="item">
        </el-option>
      </el-select>
      <div style="display: inline-block; width: 19px"></div>
      <el-select v-model="roundTime" placeholder="placeholder">
        <el-option
          v-for="item in roundTimeList"
          :key="item"
          :label="item"
          :value="item">
        </el-option>
      </el-select>
      <div style="display: inline-block; width: 19px"></div>
      <DateBox inputId="d2" v-model="startDate" style="width: 100px" format="yyyy-MM-dd"></DateBox>
      <div style="display: inline-block; width: 19px">→</div>
      <DateBox inputId="d2" v-model="endDate" style="width: 100px" format="yyyy-MM-dd"></DateBox>
      <input type="button" class="search" @click="search()">
      <div class="btns">
        <input type="button" class="mo-btn-x mo-btn-gray" value="导出" @click="exportLog">
      </div>
    </div>
    <el-table :data="data" style="width:100%" ref="multipleTable" height="690px" :highlight-current-row="true">
      <el-table-column type="index" label="序号" width="32"
                       :index="(paginations_num.current_page-1)*20+1"></el-table-column>
      <el-table-column prop="created" label="操作时间" min-width="130" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="key" label="分类" min-width="30" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="content" label="操作内容" min-width="144" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="ip" label="IP" min-width="60" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="user" label="用户" min-width="30" :show-overflow-tooltip="true"></el-table-column>
    </el-table>
    <pagination :paginations_num.sync="paginations_num"></pagination>
  </div>

</template>

<script>
  import Pagination from "@/common/pagination";
  export default {
    name: "LdfsLogView",
    components: {Pagination},
    data() {
      return {
        operator: "分类",
        roundTime: "最近一周",
        key: "",
        data: [],
        operatorTypeList: ['类型', '登录', '注销', '磁盘', '目录','日志'],
        roundTimeList: ["自定义","最近一周", "最近半月", "最近一月", "最近两月", "最近三月"],
        paginations_num: {
          current_page: 1,
          total_page: 1
        },
        getCheckIp:"",
        endDate: new Date(),
        custom_date:new Date(),
      }
    },
    mounted() {
      this.search()
    },
    methods: {
      search(page = 1) {
        let params = {
          st: this.dateFormat(this.startDate, 0),
          et: this.dateFormat(this.endDate, 1),
          page: page
        };
        if (this.key !== "") {
          params.content = this.key;
        } else {
          params.content = "";
        }
        if (this.operatorTypeList.indexOf(this.operator) > 0) {
          console.log(this.operatorTypeList.indexOf(this.operator));
          params.key = this.operator;
        }else{
          params.key = "";
        }
        console.log(params);
        this.axios.get("/ldfs/api/v1/log", {params: params}).then(res => {
          this.data = res.data.data.data;
          this.paginations_num.total_page = res.data.total;
        }).catch(error => {
          console.log("服务器连接失败");
        })
      },
      requestURl(url){
        this.axios.get(url,{responseType:"blob"}).then(res=>this.download(res)).catch(error=>{console.log("下载文件失败")})
      },
      download(response) {
        const {statusText, status} = response;
        if (response.data && response.data instanceof Blob) {
          //获取后台文件名
          let realFileName = response.headers["content-disposition"].split(";")[1].split("=")[1];
          console.log(realFileName);
          let blob = response.data;
          if (window.navigator.msSaveOrOpenBlob) {
            navigator.msSaveBlob(blob, realFileName);
          } else {
            let downloadElement = document.createElement('a');
            downloadElement.href = window.URL.createObjectURL(blob);
            downloadElement.download = realFileName;
            //兼容火狐浏览器
            document.body.appendChild(downloadElement);
            let evt = document.createEvent("MouseEvents");
            evt.initEvent("click", false, false);
            downloadElement.dispatchEvent(evt);
            document.body.removeChild(downloadElement);
          }
        }
        else {
          throw response
        }
      },
      exportLog(){
        console.log(this.dateFormat(this.startDate));
        let params = "start_time="+this.dateFormat(this.startDate)+"&end_time="+this.dateFormat(this.endDate);
        if (this.key !== "") {
          params += "&key=" + this.key;
        }
        if (this.operatorTypeList.indexOf(this.operator) !== 0) {
          params +="&operation="+this.operator
        }
        this.requestURl('/ldfs/api/v1/log_file?'+params);
      },
      dateFormat(time, flag) {
        var date=new Date(time);
        var year=date.getFullYear();
        var month= date.getMonth()+1<10 ? "0"+(date.getMonth()+1) : date.getMonth()+1;
        var day=date.getDate()<10 ? "0"+date.getDate() : date.getDate();
        if (flag == 0){
          return year+"-"+month+"-"+day + " 00:00:00";
        }else{
          return year+"-"+month+"-"+day + " 23:59:59";
        }
        
      }
    },
    computed: {
      startDate: {
        set(val) {
          this.custom_date = val;
          return val
        },
        get() {
          let start = new Date();
          this.endDate = new Date();
          switch (this.roundTime) {
            case "最近一周":
              return new Date(start.setTime(start.getTime() - 3600 * 1000 * 24 * 7));
            case "最近半月":
              return new Date(start.setTime(start.getTime() - 3600 * 1000 * 24 * 15));
            case "最近一月":
              return new Date(start.setTime(start.getTime() - 3600 * 1000 * 24 * 30));
            case "最近两月":
              return new Date(start.setTime(start.getTime() - 3600 * 1000 * 24 * 60));
            case "最近三月":
              return new Date(start.setTime(start.getTime() - 3600 * 1000 * 24 * 90));
            default:
              return this.custom_date
          }
        }
      }
    },
    watch: {
      "paginations_num.current_page": function (newVal, oldVal) {
        this.search(newVal)
      }
    },
  }
</script>

<style scoped>
  .div_choice {
    margin-top: 15px;
  }

  .sdc {
    background: red;
    color: #fff;
    padding: 5px;
    border-radius: 50%;
  }

  .f-field {
    width: 12em;
    height: 20px;
  }
</style>
