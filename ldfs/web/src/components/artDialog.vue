<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogVisible"
    :close-on-click-modal="false"
    :modal="modal"
    :width="width"
    :top="top"
    @closed="closed">
    <div class="separater"></div>
    <div class="slot-scope" :style="{height:height}">
      <slot :data="data"></slot>
    </div>
    <div class="el-dialog__footer" v-show="choice_show">
      <a class="mo-btn-gray confirm mo-btn-x mo-btn-x-left" href="javascript:" @click="choseTrue">确定</a>
      <a class="mo-btn-gray cancel mo-btn-x mo-btn-x-left" href="javascript:"
         @click='dialogVisible=false'>取消</a>
    </div>
  </el-dialog>
</template>

<script>
  export default {
    name: "artDialog",
    data() {
      return {
        top: "",
        data: [1, 2, 3, 4, 5],
        screen_height: 0,
        dialogVisible: false
      }
    },
    props: {
      height: {
        type: String,
        default: "144px"
      },
      title: {
        type: String,
        default: "提示"
      },
      width: {
        type: String,
        default: "400px"
      },
      choice_show: {
        type: Boolean,
        default: true
      },
      modal:{
        type:Boolean,
        default:true
      }
    },
    mounted() {
      this.screen_height = window.screen.height;
      this.top = (this.screen_height / 2 - 300).toString() + "px";
    },
    methods: {
      closed() {
        this.$emit("closed")
      },
      openBackup() {
        this.dialogVisible = true;
      },
      closePrompt() {
        this.dialogVisible = false;
      },
      choseTrue() {
        this.dialogVisible = false;
        this.$emit("detemine")
      }
    },
  }
</script>

<style scoped>

  .el-dialog__footer {
    text-align: center;
  }

</style>
