<style lang="stylus" scoped>
  .tree
    height 1000px
    background-size 100% 100%
    .main
      width 100%
      height calc(80% - 100px)
      margin-top -15px
</style>

<template>
  <div class="tree">
    <v-header :name="name" :legendArr="legendArr" :myChart="myChart"></v-header>
    <div class="main"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
import axios from 'axios'
import header from 'src/components/header/header'
import filter from 'src/components/filter/filter'

export default {
  name: 'tree',
  components: {
    'v-header': header,
    'v-filter': filter
  },
  methods: {
    myinit () {
      this.legendArr = this.myChart.getOption().series
      this.legendArr.forEach((data) => {
        data.selected = true
      })
      this.$root.charts.push(this.myChart)
      window.addEventListener('resize', function () {
        this.myChart.resize()
      }.bind(this))
    }
  },
  data () {
    return {
      legendArr: [],
      color: this.$store.state.color,
      styleArr: [],
      myChart: {},
      name: '进程树'
    }
  },
  mounted () {
    axios.get('static/data/tree/tree1.json').then((res) => {
      var data1;
      data1 = res.data;
      this.myChart = echarts.init(document.querySelector('.tree .main'), 'light')
      this.myChart.setOption({
        tooltip: {
          trigger: 'item',
          triggerOn: 'mousemove'
        },
        legend: {
          top: '2%',
          left: '3%',
          orient: 'vertical',
          data: [{
            name: '进程树'
          }],
          borderColor: '#c23531',
          textStyle: {
            color: '#fff'
          }
        },
        color: this.color,
        series: [
          {
            type: 'tree',
            name: '进程树',
            data: [data1],
            symbolSize: 7,
            label: {
              normal: {
                position: 'left',
                verticalAlign: 'middle',
                align: 'right',
                textStyle: {
                  color: '#fff'
                }
              }
            },
            leaves: {
              label: {
                normal: {
                  position: 'right',
                  verticalAlign: 'middle',
                  align: 'left',
                  textStyle: {
                    color: '#fff'
                  }
                }
              }
            },
            expandAndCollapse: true,
            animationDuration: 550,
            animationDurationUpdate: 750
          }
        ]
      })
    });
    this.myinit()
  }
}
</script>
