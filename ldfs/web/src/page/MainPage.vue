<template>
  <div class="wrap-outer">
      <router-view></router-view>
  </div>
</template>

<script>
  import LdfsHeader from "@/layout/LdfsHeader";

	export default {
		name: "MainPage",
	}
</script>

<style scoped>
  .wrap-outer {
    margin-left: calc(100vw - 100%);
  }
</style>

// <!-- 路由匹配到的组件将显示在这里 -->
// <router-view></router-view>

