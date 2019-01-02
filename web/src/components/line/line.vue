<!-- 层叠柱状图 -->
<style lang="stylus" scoped>
.line
  height 1000px
  background-size 100% 100%
  .main
    width 100%
    height calc(100% - 100px)
    margin-top -15px
</style>

<template>
<div class="line">
  <v-header :name="name" :legendArr="legendArr" :myChart="myChart"></v-header>
  <v-filter :myChart="myChart" v-if="myChart._dom"></v-filter>
  <div class="main"></div>
</div>

</template>

<script>
import echarts from 'echarts'
import header from 'src/components/header/header'
import filter from 'src/components/filter/filter'

export default {
  data () {
    return {
      legendArr: [],
      color: this.$store.state.color,
      myChart: {},
      name: '访问折线图'
    }
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
  components: {
    'v-header': header,
    'v-filter': filter
  },
  mounted () {
    // 基于准备好的dom，初始化echarts实例
    this.myChart = echarts.init(document.querySelector('.line .main'), 'light')
    this.myChart.setOption({
      title: {
        show: false
      },
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        show: false
      },
      toolbox: {
        show: false
      },
      color: this.color,
      calculable: true,
      xAxis: [{
        name: '日期',
        type: 'category',
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        nameTextStyle: {
          color: 'rgba(255, 255, 255, 0.69)'
        },
        axisLabel: {
          textStyle: {
            color: 'white'
          }
        },
        data: ['2018-12-20', '2018-12-21', '2018-12-22', '2018-12-23', '2018-12-24', '2018-12-25', '2018-12-26']
      }],
      yAxis: [{
        axisLine: {
          show: false
        },
        nameLocation: 'end',
        nameGap: 20,
        nameRotate: 0,
        axisTick: {
          show: false
        },
        splitLine: {
          lineStyle: {
            color: ['rgba(230, 230, 230, 0.2)']
          }
        },
        axisLabel: {
          textStyle: {
            color: 'white',
            fontSize: 14
          }
        },
        name: '访问量',
        type: 'value',
        nameTextStyle: {
          color: 'rgba(255, 255, 255, 0.69)'
        }
      }],
      series: [{
        name: '站点1',
        type: 'line',
        stack: '总量',
        data: [120, 132, 101, 134, 90, 230, 210]
      }, {
        name: '站点2',
        type: 'line',
        stack: '总量',
        data: [220, 182, 191, 234, 290, 330, 310]
      }, {
        name: '站点3',
        type: 'line',
        stack: '总量',
        data: [150, 232, 201, 154, 190, 330, 410]
      }, {
        name: '站点4',
        type: 'line',
        stack: '总量',
        data: [320, 332, 301, 334, 390, 330, 320]
      }, {
        name: '站点5',
        type: 'line',
        stack: '总量',
        data: [820, 932, 901, 934, 1290, 1330, 1320]
      }]
    })
    this.myinit()
  }
}

</script>
