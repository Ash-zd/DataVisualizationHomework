<template lang="html">
  <div class="dashboard">
        <div class="flex-container column">
          <div class="item one" @click="clickChart('1')" style="transform: translate(-28%,-37.5%) scale(0.25)">
            <multipleColumn></multipleColumn>
          </div>
          <div class="item two" @click="clickChart('2')" style="transform: translate(-28%,-11.5%) scale(0.25)">
            <column1></column1>
          </div>
          <div class="item three" @click="clickChart('3')" style="transform: translate(-28%,14.5%) scale(0.25)">
            <v-line></v-line>
          </div>
          <div class="item four" @click="clickChart('4')" style="transform: translate(-28%,40.5%) scale(0.25)">
            <p>Pass.</p>
          </div>
          <div class="item five active" @click="clickChart('5')" style="transform: translate(36%, 0) scale(1)">
            <point></point>
          </div>
        </div>
  </div>
</template>

<script>
import column from 'src/components/column/column'
import line from 'src/components/line/line'
import multipleColumn from 'src/components/multipleColumn/multipleColumn'
import point from 'src/components/point/point'

export default {
  data() {
    return {
      items: []
    }
  },
  mounted() {
    this._init()
  },
  methods: {
    _resize() {
      this.$root.charts.forEach((myChart) => {
        myChart.resize()
      })
    },
    _init() {
      this.items = document.querySelectorAll('.flex-container .item')
      for (let i = 0; i < this.items.length; i++) {
        this.items[i].dataset.order = i + 1;
      }
    },
    clickChart(clickIndex) {
      let activeItem = document.querySelector('.flex-container .active');
      let activeIndex = activeItem.dataset.order;
      let clickItem = this.items[clickIndex - 1];
      if (activeIndex === clickIndex) {
        return
      }
      activeItem.classList.remove('active');
      clickItem.classList.add('active');
      this._setStyle(clickItem, activeItem)
    },
    _setStyle(el1, el2) {
      let transform1 = el1.style.transform;
      let transform2 = el2.style.transform;
      el1.style.transform = transform2;
      el2.style.transform = transform1
    }
  },
  components: {
    'column1': column,
    'column2': column,
    multipleColumn,
    point,
    'v-line': line
  }
}

</script>

<style lang="stylus" scoped>
*
  box-sizing: border-box;
.point,.multipleColumn,.columnChart,.line
  height 100%!important
  width 100%!important
  background none!important
.item
    padding: 0px;
    margin: 0px;
    width: 68%;
    height: 100%;
    position absolute
    transform scale(0.33)
    text-align: center;
    transition:all 0.7s;
    background rgba(32, 32, 35, 0.5)
.dashboard
    position relative
    width 100%
    height 100%
    margin:0px;
    padding:0px;
    padding-top 5%
    background-size 100% 100%
.flex-container.column
    position relative
    height: 95%;
    width: 95%;
    overflow: hidden;
    margin:  0 auto 10px auto;
    box-sizing: content-box;
.active
    height 100%
    width: 69%;
    margin-left: 10px;
    line-height: 300px;
</style>
