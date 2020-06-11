<template>
  <div class="menuContainer"><!--菜单栏-->
    <div>
      <ul id="mainMenu">
        <li class="level1">
          <router-link :to="{name:'overview'}">系统首页</router-link>
        </li>
        <li class="level1">
          <router-link :to="{name:'disk'}" @click="storage_manage_show=!storage_manage_show" :class="storage_manage">
            磁盘管理
          </router-link>
        </li>
        <ul class="level2" v-show="storage_manage_show">
          <li>
            <router-link :to="{name:'manage'}">磁盘配置</router-link>
          </li>
          <li>
            <router-link :to="{name:'raid'}">RAID配置</router-link>
          </li>
        </ul>
        <li class="level1">
          <router-link :to="{name:'region'}" @click="data_save_show=!data_save_show" :class="data_save">目录管理
          </router-link>
        </li>
        <ul class="level2" v-show="data_save_show">
          <li>
            <router-link :to="{name:'quota'}">目录配置</router-link>
          </li>
          <li>
            <router-link :to="{name:'store'}">存储配置</router-link>
          </li>
        </ul>
        <li class="level1">
          <router-link :to="{name:'gfs'}" @click="data_gfs_show=!data_gfs_show" :class="gfs_show">集群管理</router-link>
        </li>
        <ul class="level2" v-show="data_gfs_show">
          <li>
            <router-link :to="{name:'state'}">集群状态</router-link>
          </li>
          <li>
            <router-link :to="{name:'gfsdisk'}">集群磁盘</router-link>
          </li>
          <li>
            <router-link :to="{name:'volume'}">集群卷块</router-link>
          </li>
        </ul>
        <li class="level1">
          <router-link :to="{name:'log'}">日志管理</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "LdfsMenu",
    data() {
      return {
        storage_manage_show: false,
        data_save_show: false,
        storage_manage: "",
        data_save: "",
        data_gfs_show: false,
        gfs_show: "",
      }
    },
    created() {
      let to = this.$route.fullPath;
      this.path_event(to)
    },
    methods: {
      path_event(to) {
        if (to.match('/disk')) {
          this.storage_manage = 'bg_col_li3';
          this.storage_manage_show = true;
          this.data_save = "";
          this.data_save_show = false;
          this.data_gfs_show = false;
          this.gfs_show = "";
        } else if (to.match('/region')) {
          this.data_save = 'bg_col_li3';
          this.data_save_show=true;
          this.storage_manage = '';
          this.storage_manage_show = false;
          this.data_gfs_show = false;
          this.gfs_show = "";
        } else if (to.match('/gfs')) {
          this.data_save = '';
          this.data_save_show= false;
          this.storage_manage = '';
          this.storage_manage_show = false;
          this.data_gfs_show = true;
          this.gfs_show = 'bg_col_li3';
        } else {
          this.storage_manage = '';
          this.storage_manage_show = false;
          this.data_save = "";
          this.data_save_show = false
          this.data_gfs_show = false;
          this.gfs_show = '';
        }
      }
    },
    watch: {
      '$route.fullPath': {
        handler(val, oldval) {
          this.path_event(val);
        }
      }
    }
  }
</script>

<style scoped>
  /*菜单的样式*/
  #mainMenu .router-link-active {
    background: url(../assets/images/tab_select.png?t=5.0.0.0_1339108041) no-repeat;
    color: white;
    background-color: #53AFE4;
    background: -webkit-gradient(linear, left bottom, right bottom, from(#2D8BC0), to(#53AFE4));

  }

  .menuContainer {
    width: 175px;
    height: calc(100% - 98px - 17px - 32px);
    float: left;
    position: fixed;
    top: 115px;
    border-right: solid 1px #949799;
  }

  .menuContainer ul {
    margin-right: 36px;
  }

  .menuContainer li {
    text-align: right;
    font-weight: 400;
    font-size: 14px;
    color: #4e4e4e;
    cursor: pointer;
    margin-bottom: 5px;
  }

  .menuContainer a {
    padding: 2px 4px;
  }

  .menuContainer a:hover {
    color: #007ac0;
    font-size: 14px;
  }

  .menuContainer li ul.level2 {
    display: none;
  }

  .menuContainer .menu_select {
    font-weight: 400;
    color: #fff;
    background-color: #53afe4;
  }

  .menuContainer .menu_select1 {
    font-weight: 700;
    color: #000000;
  }

  .menuContainer .sub_menu_select {
    font-size: 12px;
    color: #ffffff;
    background-color: #53afe4;
  }

  .menuContainer .level2 {
    padding: 6px 0 24px;
    font-size: 12px;
    margin: 0;
  }

  .menuContainer .level2 li {
    margin-bottom: 12px;
  }

  .menuContainer .level2 li a {
    padding: 3px 4px;
    font-size: 12px;
  }

  .menuContainer .level2 li a:hover {
    color: #007ac0;
    font-size: 12px;
  }

  .bg_col {
    background: #53afe4;
    color: white;
  }

  .bg_col_li3 {
    font-weight: 700;
    background: white !important;
    color: black !important;
  }
</style>
