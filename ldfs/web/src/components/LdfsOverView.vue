<template>
<div>
    <div class="margin-line" ref="screenWidth" id="screenWidth"></div>
    <div class="sysinfo-group">
        <span class="text-title">系统信息</span>
    </div>
    <div class="sysinfo-item-group">
        <div class="text-title-1">服务器运行时间</div>
        <span class="text-content">{{uptime}}</span>
    </div>
    <div class="sysinfo-item-group">
        <div class="text-title-1">当前时间</div>
        <span class="text-content" >{{currentDatetime}}</span>
    </div>
</div>
</template>

<script>
    export default {
        name: "LdfsOverView",
        data(){
            return {
                uptime: "",
                currentDatetime: "",
            }
        },
        created(){
            // 获取当前时间
            // this.getCurrentDatetime();
        },
        mounted(){
            
            this.timeout = setInterval(() => {
                this.getCurrentDatetime();
            }, 1000);
        },
        destroyed(){
            clearInterval(this.timeout);
        },
        methods:{
            getCurrentDatetime(){
                this.currentDatetime = new Date().toLocaleString();
                console.log(this.currentDatetime);
            },
        },
    }
</script>

<style scoped>
.margin-line {
    margin-top: 23px;
}
.sysinfo-group{
    min-width: 110px;
    display: inline-block;
}
.sysinfo-item-group{
    min-width: 220px;
    display: inline-block;
}
.text-title{
    font-size: 12px;
    font-weight: bold;
    margin-bottom: 5px;
    width: 220px;
}
.text-title-1{
    font-size: 12px;
    font-weight: bold;
    display: inline-block;
    width: 92px;
    color: #8b8b8b;
}
.text-content{
    color: #4e4e4e;
    font-size: 12px;
}
</style>