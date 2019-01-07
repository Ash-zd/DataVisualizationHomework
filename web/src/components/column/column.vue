<!-- 柱状图 -->
<style lang="stylus" scoped>
.columnChart
  height 800px
  background-size 100% 100%
  color white
  .main
    width 100%
    height calc(100% - 100px)
    margin-top -15px
</style>

<template>
<div class="columnChart">
  <v-header :name="name" :legendArr="legendArr" :myChart="myChart"></v-header>
  <div class="main"></div>
</div>

</template>

<script>
import echarts from 'echarts'
import header from 'src/components/header/header'
import filter from 'src/components/filter/filter'
import axios from 'axios'

export default {
  data () {
    return {
      legendArr: [],
      color: this.$store.state.color,
      myChart: {},
      name: '使用率',
      option: {},
      cpuData: []
    }
  },
  methods: {
    myinit () {
      this.legendArr = this.myChart.getOption().series;
      this.legendArr.forEach((data) => {
        data.selected = true
      });
      this.$root.charts.push(this.myChart);
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
    setInterval(function () {
      axios.get("http://localhost:8000/api/cpumemory/info/").then((res) => {
        this.myChart = echarts.init(document.querySelector('.columnChart .main'), 'light');
        this.myChart.setOption({
          title: {
            show: true
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            show: false,
            textStyle: {
              color: 'white'
            }
          },
          color: this.color,
          calculable: true,
          xAxis: [{
            name: '',
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
            data: res.data['name']
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
              },
              formatter: '{value} %'
            },
            name: '使用率',
            type: 'value',
            nameTextStyle: {
              color: 'rgba(255, 255, 255, 0.69)'
            },
            max: 100
          }],
          series: [{
            name: 'CPU',
            type: 'bar',
            data: res.data['percent'],
            barWidth: 50,
            barGap: 0,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top',
                  textStyle: {
                    color: 'white',
                    fontSize: 16
                  }
                }
              }
            }
          }]
        });
      });
    }, 5000);
    this.myinit()
  }
}

</script>
