<template>
    <div class="mainContainer">
      <Ldfs-header></Ldfs-header>
      <Ldfs-menu></Ldfs-menu>
      <Ldfs-body></Ldfs-body>
    </div>
</template>

<script>

  import LdfsHeader from "@/layout/LdfsHeader";
  import LdfsMenu from "@/layout/LdfsMenu";
  import LdfsBody from "@/layout/LdfsBody";
	export default {
		name: "LdfsMainPage",
    components:{LdfsHeader, LdfsMenu, LdfsBody}
	}
</script>

<style scoped>
  .mainContainer {
    width: 100vw;
    margin-left: calc((100% - 100vw) / 2);
    position: relative;
    top: 98px;
  }
</style>
