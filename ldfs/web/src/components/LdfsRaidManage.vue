<template>
  <div>
    <div class="raid-text">RAID配置</div>
    <input type="button" value="添加" class="mo-btn-x mo-btn-gray AddBtn" @click="add">
    <el-table
      :data="tableData"
      style="width:100%"
      ref="multipleTable"
      height="690px"
      :highlight-current-row="true"
    >
      <el-table-column type="index" label="序号" width="32" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="type" label="raid模式" min-width="100" :show-overflow-tooltip="true"></el-table-column>
      <el-table-column prop="disks" label="磁盘" min-width="100" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span>{{scope.row.disks.map((disks)=>{return disks}).join(', ')}}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" min-width="50" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <a class="optionlink" @click="cancel_mode(scope.$index)">取消模式</a>
        </template>
      </el-table-column>
    </el-table>
    <artDialog ref="raidArt" :height="'355px'" :title="'添加'" @detemine="detemine" @closed="cancelDialog">
      <template slot-scope="data">
        <div class="scope-content-top">
          <div>
            <span class="scope-item-name">请选择模式</span>
            <div class="scope-content-select">
              <el-select v-model="mode" placeholder="placeholder">
                <el-option
                  v-for="(item,index) in choice_raid"
                  :key="index"
                  :label="item"
                  :value="item"
                ></el-option>
              </el-select>
            </div>
            <span class="scope-prompt-text">请选择{{mode==="RAID10"?4:mode==="RAID5"?3:2}}块磁盘</span>
          </div>
        </div>
        <div class="scope-content-middle">
          <div class="scope-content-middle-item">请选择磁盘</div>
          <div class="checked-content-box-item">
            <el-checkbox-group v-model="checkedDisk">
              <div v-for="disk in disk_data" :key="disk.id" class="el-checkdisk">
                <el-checkbox :label="disk" :key="disk.id">{{disk.name}}</el-checkbox>
              </div>
            </el-checkbox-group>
          </div>
        </div>
      </template>
    </artDialog>
  </div>
</template>

<script>
  import artDialog from "./artDialog";

  export default {
    name: "LdfsRaidManage",
    components: {artDialog},
    data() {
      return {
        mode: "RAID0",
        checkedDisk: [],
        tableData: [],
        disk_data: [],
        disabledDisk:[],
        choice_raid: ["RAID0", "RAID1", "RAID5", "RAID10"]
      };
    },
    created() {
      this.init();
    },
    methods: {
      init() {
        this.axios.get("/ldfs/api/v1/raid").then(res => {
          this.tableData = res.data.data;
          console.log("raid get:", res.data.data);
        });
        this.axios.get('/ldfs/api/v1/disk').then(
          res => {
            this.disk_data = res.data.data;
            console.log("raid manage...");
            console.log(this.disk_data)
          }
        )
      },

      cancel_mode(index) {
        this.$prompt.success({
          dialogVisible: true,
          show: true,
          detemine: true,
          content: `请确认是否取消RAID?`
        });
        this.$prompt.instance.$on("detemine", () => {
          this.$prompt.success({
            dialogVisible: true,
            content: `取消raid配置中请稍后!`,
            error: false,
            show: false
          });
          this.axios
            .delete("/ldfs/api/v1/raid", {
              data: {id: this.tableData[index].id}
            })
            .then(res => {
              this.$prompt.instance.promptClose();
              if (res.data.code === 0) {
                this.init();
                this.$successPrompt.success({
                  dialogVisible: true,
                  content: "取消RAID模式成功",
                });
              } else {
                this.$prompt.success({
                  dialogVisible: true,
                  content: `取消RAID模式失败,` + res.data.msg,
                  error: true
                });
              }
            }).catch(error => {
            this.$prompt.instance.promptClose();
            this.$prompt.success({
              dialogVisible: true,
              content: `取消RAID模式失败`,
              error: true
            });
          });
        });
      },

      add() {
        console.log(this.tableData.map(item=>item.disks.map(value=>value.id)).flatten());
        //console.log(this.tableData.map(item=>item.disk.map(value=>value.disk_id)));
        this.disk_data.filter(item=>{
        });
        this.$refs.raidArt.openBackup();
      },

      detemine() {
        if (this.mode === "RAID5") {
          if (this.checkedDisk.length >= 3) {
            return
          }
        }
        if (this.mode === "RAID10") {
          if (this.checkedDisk.length >= 4) {
            return
          }
        }
        let data = {
          disks: this.checkedDisk.map(item => item.id),
          type: this.mode
        };
        console.log(data);
        this.$prompt.success({
          dialogVisible: true,
          content: `raid配置中请稍后!`,
        });
        this.axios.post("/ldfs/api/v1/raid", data).then(res => {
          this.$prompt.instance.promptClose();
          if (res.data.code === 0) {
            this.$successPrompt.success(
              {
                dialogVisible: true,
                content: "设置RAID模式成功",
              }
            );
            this.init()
          } else {
            this.$prompt.success({
              dialogVisible: true,
              content: `添加raid失败,<br>` + res.data.msg,
              error: true
            });
          }
        });
      },

      cancelDialog() {
        this.checkedDisk = []
      }
    },
    watch: {
      checkedDisk(newValue, oldValue) {
        console.log(newValue)
      }
    },
  };
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

  .scope-content-top {
    margin-top: 41px;
    margin-left: 75px;
  }

  .scope-item-name {
    width: 81px;
    display: inline-block;
    vertical-align: bottom;
  }

  .scope-content-middle {
    margin-top: 38px;
    margin-left: 75px;
    width: 300px;
    display: inline-block;
  }

  .scope-content-middle-item {
    width: 80px;
    height: 200px;
    float: left;
  }

  .scope-prompt-text {
    font-size: 12px;
    color: #8B8B8B;
    position: relative;
    top: 20px;
  }

  .scope-content-select {
    position: absolute;
    display: inline-block;
  }

  .checked-content-box-item {
    display: inline-block;
  }

  .scope-content-checkbox {
    margin-bottom: 14px;
  }

  .el-checkdisk {
    margin-bottom: 14px;
  }
</style>
