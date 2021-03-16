import Vue from 'vue'
import Router from 'vue-router';

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: '/',
      name: '/',
      component: resolve => require(["@/page/MainPage"], resolve),
      redirect: {name: "overview"},
      children:[
        {
          path: "ldfs/",
          name: "ldfs",
          component: resolve => require(["@/page/LdfsMainPage"], resolve),
          redirect: {name: "overview"},
          children:[
            {
              path: "overview/",
              name: "overview",
              component:resolve => require(["@/components/LdfsOverView"], resolve),
            },
            {
              path: "disk/",
              name: "disk",
              component:resolve => require(["@/components/LdfsDiskView"], resolve),
              redirect: {name: "manage"},
              children: [
                  {
                      path: "manage/",
                      name: "manage",
                      component:resolve => require(["@/components/LdfsDiskManage"], resolve),
                  },
                  {
                      path:"raid/",
                      name:"raid",
                      component:resolve => require(["@/components/LdfsRaidManage"], resolve),
                  },
              ]
            },
            {
              path: "region/",
              name: "region",
              component:resolve => require(["@/components/LdfsRegionView"], resolve),
              redirect: {name: "store"},
              children:[
                {
                  path: "quota/",
                  name: "quota",
                  component:resolve => require(["@/components/LdfsRegionView"], resolve),
                },
                {
                  path: "store/",
                  name: "store",
                  component:resolve => require(["@/components/LdfsRegionManage"], resolve),
                },
              ]
            },
            {
              path: "gfs/",
              name: "gfs",
              component:resolve => require(["@/components/LdfsGfsOverView"], resolve),
              redirect: {name: "state"},
              children:[
                {
                  path: "state/",
                  name: "state",
                  component:resolve => require(["@/components/LdfsGfsView"], resolve),
                },
                {
                  path: "volume/",
                  name: "volume",
                  component:resolve => require(["@/components/LdfsGfsVolume"], resolve),
                },
                {
                  path: "gfsdisk/",
                  name: "gfsdisk",
                  component:resolve => require(["@/components/LdfsGfsDisk"], resolve),
                },
              ]
            },
            {
              path: "log/",
              name: "log",
              component:resolve => require(["@/components/LdfsLogView"], resolve),
            },
          ]
        },
      ]
   },
  ]
})
