<template>
  <div class="contentContainer"><!--网站内容部分-->
    <div id="frame_content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
	export default {
		name: "LdfsBody"
	}
</script>

<style scoped>
  .contentContainer {
    height: calc(100vh - 98px - 17px - 32px);
    margin: 0 0 0 211px;
    padding: 0 114px 32px 0;
    overflow-x: auto !important;
    overflow-y: auto !important;
  }

  #frame_content {
    min-width: 841px;
  }
</style>
