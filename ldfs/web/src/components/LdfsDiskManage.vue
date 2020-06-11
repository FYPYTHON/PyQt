<template>
  <div>
    <input type="button" value="刷新" class="mo-btn-x mo-btn-gray AddBtn" @click="refresh">
    <span class="raid-text">磁盘管理</span>
    <el-table :data="tableData" style="width:100%" ref="multipleTable" height="690px" :highlight-current-row="true">
      <el-table-column type="index" label="序号" width="32" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="ip" label="IP" min-width="60" :show-overflow-tooltip="true">
      </el-table-column>
      <el-table-column prop="slot" label="盘符" min-width="60" :show-overflow-tooltip="true">
      </el-table-column>
      <el-table-column prop="name" label="名称" min-width="60" :show-overflow-tooltip="true">
      </el-table-column>
      <el-table-column prop="total_size" label="总容量" min-width="60" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span>{{scope.row.total_size | numFilter}} G</span>
        </template>
      </el-table-column>
      <el-table-column prop="used_size" label="可用量" min-width="60" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span>{{scope.row.free_size | numFilter}} G</span>
        </template>
      </el-table-column>
      <el-table-column prop="status" label="存储状态" min-width="60" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span v-if="scope.row.status===1">已应用</span>
          <span v-else>未应用</span>
        </template>
      </el-table-column>
      <el-table-column prop="raid" label="Raid配置" min-width="60" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span>{{scope.row.raid}}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" min-width="50" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <a class="optionlink" @click="stopAndCancel(scope.$index)" v-if="scope.row.status">删除</a>
          <a class="optionlink" @click="addDisk(scope.$index)" v-if="!scope.row.status">添加</a>
        </template>
      </el-table-column>
    </el-table>

  </div>
</template>

<script>
  export default {
    name: "LdfsDiskManage",
    data() {
      return {
        tableData: [],
      }
    },
    created() {
      this.init();
    },
    filters: {
      numFilter (value) {
      // 截取当前数据到小数点后两位
      value = value / 1024 / 1024 / 1024
      let realVal = parseFloat(value).toFixed(2)
      return realVal
      }
    },
    methods: {
      init(flash) {
        if (flash === "flash") {
          this.$prompt.success({
            dialogVisible: true,
            content: `正在刷新页面,请稍后`
          });
        }
        this.axios.get('/ldfs/api/v1/disk').then(
          res => {
            console.log(res.data);
            this.tableData = res.data.data;
            if (flash === "flash") {
              this.$prompt.instance.promptClose();
              this.$successPrompt.success(
                {
                  dialogVisible: true,
                  content: "数据刷新成功"
                }
              )
            }
          }
        ).catch(error => {
          this.$prompt.instance.promptClose();
          this.$prompt.success({
            dialogVisible: true,
            error: true,
            content: `数据刷新失败`
          })
        })
      },
      stopAndCancel(index) {
        this.$prompt.success({
          dialogVisible: true,
          show: true,
          detemine: true,
          content: `磁盘会格式化, 请保存数据!<br>是否继续清空数据并停用磁盘?`
        });
        this.$prompt.instance.$on("detemine", () => {
          // 应用请求
          this.$prompt.success({
            dialogVisible: true,
            show: false,
            detemine: false,
            content: `正在停用中请稍后!`
          });
          this.axios.delete('/ldfs/api/v1/disk', {data: {'id': this.tableData[index].id, "slot": this.tableData[index].slot}}).then(res => {
            this.$prompt.instance.promptClose();
            if (res.data.code===0) {
              this.$successPrompt.success(
                {
                  dialogVisible: true,
                  content: "清空并停用成功"
                }
              );
              this.init();
              return
            }

            this.$prompt.success({
              dialogVisible: true,
              show: true,
              detemine: true,
              content: `清空并通用失败,<br>` + res.data.msg,
            })

          })
        });
      },
      addDisk(index) {
        console.log("add disk:",index);
        this.$prompt.success({
          dialogVisible: true,
          show: true,
          detemine: true,
          content: `磁盘会格式化, 请保存数据!<br>是否继续应用数据?`
        });
        this.$prompt.instance.$on("detemine", () => {
          // 应用请求
          this.$prompt.success({
            dialogVisible: true,
            show: false,
            detemine: false,
            content: `正在修改请稍后!`
          });
          this.axios.post('/ldfs/api/v1/disk', {'id': this.tableData[index].id, "slot": this.tableData[index].slot}).then(res => {
            this.$prompt.instance.promptClose();
            if (res.data.code===0) {
              this.$successPrompt.success(
                {
                  dialogVisible: true,
                  content: "应用成功"
                }
              );
              this.init()
            } else {
              this.$prompt.success({
                dialogVisible: true,
                show: true,
                detemine: true,
                content: `应用失败,` + res.data.msg,
              })
            }
          })
        });
      },
      refresh() {
        this.init("flash");
      }
    },
  }
</script>

<style scoped>
  .raid-text {
    color: #4e4e4e !important;
    font-size: 12px;
    font-weight: bold;
    padding: 22px 0 3px 0;
    display: inline-block;
  }

  .AddBtn {
    float: right;
    margin-top: 18px;
  }
</style>
