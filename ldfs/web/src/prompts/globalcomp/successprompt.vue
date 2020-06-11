<template>
  <div class="Message">
    <el-dialog
      :modal="false"
      title="提示"
      :visible.sync="dialogVisible"
      width="186px"
      :top="message_top"
      @open="openCloseRound">
      <div>{{content}}</div>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: "MessageDialog",
    props: {
      dialogVisible: {
        default: false,
        type: Boolean,
      },
      content: {
        default: "",
        type: String,
      },
    },
    data() {
      return {
        message_top: "",
        screen_height: 0
      };
    },
    mounted() {
      this.screen_height = window.screen.height;
      this.message_top = this.screen_height / 2 + 205 + 43 + "px";
    },
    methods: {
      openCloseRound() {
        let t;
        clearTimeout(t);
        t = setTimeout(() => {
          this.dialogVisible = false;
        }, 2000);
      }
    },
  };
</script>

<style scoped>
</style>
