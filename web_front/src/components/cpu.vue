<template>
  <div id="cpu">
  </div>
</template>

<script>

export default {
  name: 'cpu',
  mounted () {
    let echarts = require('echarts')
    // 基于准备好的dom，初始化echarts实例
    let myChart = echarts.init(document.getElementById('cpu'), 'light')
    myChart.showLoading()
    function randomData () {
      value = myRandom(5, 85)
      now = new Date(+now + 2000)
      return {
        name: now.toString(),
        value: [
          now,
          value
        ]
      }
    }

    function myRandom (lower, upper) {
      return Math.floor(Math.random() * (upper - lower + 1)) + lower
    }

    var data = []
    var now = new Date()
    // var oneDay = 24 * 3600 * 1000
    var value = Math.random() * 100
    /* for (var i = 0; i < 100; i++) {
      data.push(randomData())
    } */

    setInterval(function () {
      data.push(randomData())

      myChart.hideLoading()
      myChart.setOption({
        title: {
          text: 'CPU'
        },
        tooltip: {
          trigger: 'axis',
          formatter: function (params) {
            params = params[0]
            var date = new Date(params.name)
            return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1]
          },
          axisPointer: {
            animation: false
          }
        },
        xAxis: {
          type: 'time',
          splitLine: {
            show: true
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: '{value} %'
          },
          splitLine: {
            show: true
          }
        },
        series: [{
          name: '模拟数据',
          type: 'line',
          showSymbol: true,
          hoverAnimation: true,
          data: data,
          smooth: true,
          areaStyle: {}
        }]
      })
    }, 2000)
  }
}
</script>
<style scoped>
  #cpu {
    height: 600px;
    width: 800px;
  }
</style>
