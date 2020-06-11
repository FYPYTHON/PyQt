<template>
  <div>
    <div class="data-page pg">
      <input type="text" class="page-num" :value="paginations_num.current_page" @keyup.enter="setNum"><span
      class="pagination-font">/ {{paginations_num.total_page}}</span>
      <span class="lBtnIcon lBtnPrev" @click="prev()"></span><span class="lBtnIcon lBtnNext"
                                                                   @click="next()"></span>
      <span></span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "pagination",
    props: {
      paginations_num: {
        type:Object,
        default:{
          current_page:1,
          total_page:1
        }
      }
    },
    methods: {
      prev() {
        if (this.paginations_num.current_page > 1) {
          this.paginations_num.current_page--;
        }
      },
      next() {
        if (this.paginations_num.current_page < this.paginations_num.total_page) {
          this.paginations_num.current_page++
        }
      },
      setNum() {
        console.log(this.paginations_num.current_page)
      }
    },
    watch: {
      'paginations_num.total_page': {
        handler(newValue, oldValue) {
          if (this.paginations_num.current_page > newValue) {
            this.paginations_num.current_page = newValue
          }
        }
      }
    }
  }
</script>

<style scoped>
  .data-page {
    border: none;
    height: 35px;
    display: block;
    margin: 0;
  }

  .pg {
    zoom: 1;
    position: fixed;
    bottom: 32px;
    right: 128px;
  }

  .pg table {
    font-size: 12px;
    float: right;
    height: 30px;
  }

  .pg .page-num {
    border: none;
    border-bottom: 1px solid #bdbdbd;
    width: 22px;
    padding: 0;
    color: #666666;
    line-height: 14px;
    font-size: 12px;
    text-align: center;
    font-weight: bold;
    margin: 0 2px;
    height: auto;
    float: left;
  }

  .lBtnIcon {
    width: 21px;
    height: 20px;
    left: 0;
    line-height: 16px;
    top: 50%;
    margin-top: -8px;
    display: inline-block;
  }

  .lBtnPrev {
    background: url(../assets/images/pagination_icons.png?t=5.0.270688469) no-repeat;
    background-position: 0 -20px;
    cursor: pointer;
  }

  .lBtnNext {
    background: url(../assets/images/pagination_icons.png?t=5.0.270688469) no-repeat;
    cursor: pointer;
  }

  .lBtnPrev:hover {
    background-position: -42px -20px
  }

  .lBtnPrev:active {
    background-position: -21px -20px
  }

  .lBtnNext:hover {
    background-position: -42px 0
  }

  .lBtnNext:active {
    background-position: -21px 0
  }

  .pg a.l-btn span span.l-btn-text {
    top: 0;
    height: 30px;
  }

  .pagination-font {
    padding-right: 6px;
    font-size: 12px;
    float: left;
    line-height: 14px;
  }

  .l-btn-disabled .lBtnPrev {
    background-position: -63px -20px;
  }

  .l-btn-disabled .lBtnNext {
    background-position: -63px 0;
  }
</style>
