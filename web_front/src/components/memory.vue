<template>
<div id="memory"></div>
</template>

<script>
export default {
  name: 'memory',
  mounted () {
    function randomData () {
      value = myRandom(1560, 13384)
      now = new Date(+now + 3000)
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
      for (var i = 0; i < 2; i++) {
        data.push(randomData())
      }

      myChart.setOption({
        title: {
          text: '内存'
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
            formatter: '{value} MB'
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
    }, 3000)
    let echarts = require('echarts')
    // 基于准备好的dom，初始化echarts实例
    let myChart = echarts.init(document.getElementById('memory'), 'light')
  }
}
</script>

<style scoped>
#memory{
  height: 600px;
  width: 800px;
}
</style>
