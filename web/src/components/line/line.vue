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
      name: 'IO监视',
      recv: [],
      sent: []
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
    let netSentData = [];
    let netRecvData = [];
    let diskWriteData = [];
    let diskReadData = [];
    setInterval(function () {
      axios.get('http://localhost:8000/api/netdisk/io/').then((res) => {
        netSentData.push(res.data['net']['sent']);
        netRecvData.push(res.data['net']['recv']);
        diskWriteData.push(res.data['disk']['write']);
        diskReadData.push(res.data['disk']['read']);
        this.myChart = echarts.init(document.querySelector('.line .main'), 'light');
        this.myChart.setOption({
          title: {
            show: true
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            show: true,
            data: ['入站流量速率', '出站流量速率', '磁盘写入速率', '磁盘读取速率'],
            textStyle: {
              color: 'white'
            }
          },
          color: this.color,
          calculable: true,
          xAxis: [{
            name: '时间',
            // type: 'category',
            type: 'time',
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
            }
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
            name: 'Kb/s',
            type: 'value',
            nameTextStyle: {
              color: 'rgba(255, 255, 255, 0.69)'
            }
          }],
          series: [{
            name: '入站流量速率',
            type: 'line',
            data: netRecvData,
            smooth: true
          }, {
            name: '出站流量速率',
            type: 'line',
            data: netSentData,
            smooth: true
          }, {
            name: '磁盘写入速率',
            type: 'line',
            data: diskWriteData,
            smooth: true
          }, {
            name: '磁盘读取速率',
            type: 'line',
            data: diskReadData,
            smooth: true
          }]
        });
      })
    }, 2000);
    this.myinit();
  }
}

</script>
