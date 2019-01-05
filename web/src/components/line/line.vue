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
      name: '网络IO',
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
    let sentData = [];
    let recvData = [];
    setInterval(function () {
      axios.get('http://localhost:8000/api/net/io/').then((res) => {
        sentData.push(res.data['sent']);
        recvData.push(res.data['recv']);
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
            data: ['入站流量', '出站流量'],
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
            name: '入站流量',
            type: 'line',
            data: recvData,
            smooth: true
          }, {
            name: '出站流量',
            type: 'line',
            data: sentData,
            smooth: true
          }]
        });
      })
    }, 2000);
    this.myinit();
  }
}

</script>
