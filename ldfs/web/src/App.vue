<template>
  <router-view></router-view>
</template>

<script>
  export default {
    name: "App",
  }
</script>

<style>
  /* a链接 */
  .optionlink {
    margin-right: 8px;
    color: #007ac0;
    text-decoration: underline;
  }
  .data-content{
    margin-top: 32px;
  }
  .Message .el-dialog__header {
    display: none !important;
  }

  .Message .el-dialog__body {
    width: 186px;
    height: 41px;
    line-height: 43px;
    text-align: center;
    background: #434343;
    color: #ffffff;
    font-size: 14px;
  }


</style>
