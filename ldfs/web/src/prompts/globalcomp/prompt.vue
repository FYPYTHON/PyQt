<template>
  <el-dialog
    title="提示"
    :visible.sync="dialogVisible"
    :close-on-click-modal="false"
    width="400px"
    :top="top"
    @close="closePrompt"
  >
    <div class="separater"></div>
    <div :style="{height:height}">
      <div class="info-wrap">
        <div class="info">
          <div class="prompt">
            <img src="../../assets/images/prompt.png" v-show="imgShow">
            <div style="display:inline-block;vertical-align: top">
              <span v-html="content"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="btn-wrapper" v-show='show'>
      <a class="mo-btn-gray confirm mo-btn-x mo-btn-x-left" href="javascript:" @click="choseTrue">确定</a>
      <a class="mo-btn-gray cancel mo-btn-x mo-btn-x-left" href="javascript:"
         @click='dialogVisible=false'>取消</a>
    </div>
    <div class="btn-wrapper" v-show='error'>
      <a class="mo-btn-gray confirm mo-btn-x mo-btn-x-left" href="javascript:"
         @click='dialogVisible=false'>关闭</a>
    </div>
  </el-dialog>
</template>

<script>

  export default {
    name: "prompt",
    props: {
      dialogVisible: {
        default: false,
        type: Boolean
      },
      content: {
        default: "",
        type: String
      },
      show: {
        default: false,
        type: Boolean
      },
      error: {
        default: false,
        type: Boolean
      },
      detemine: {
        default: false,
        type: Boolean
      },
      height:{
        type:String,
        default:"144px",
      },
      imgShow:{
        type:Boolean,
        default:true
      }
    },
    data() {
      return {
        top: "",
        screen_height: 0,
      };
    },
    mounted() {
      this.screen_height = window.screen.height;
      this.top = (this.screen_height / 2 - 300).toString() + "px";
    },
    methods: {
      choseTrue() {
        this.dialogVisible = false;
        this.$emit("detemine");
      },
      promptClose(){
        this.dialogVisible = false
      },
      closePrompt() {
        this.content="";
        this.detemine=false;
        this.error=false;
        this.show = false;
        this.content = "";
        this.imgShow = true;
        this.$off("detemine")
      }
    }
  };
</script>

<style scoped>
  .btn-wrapper {
    bottom: 0;
  }

  .prompt {
    vertical-align: top;
  }
</style>
