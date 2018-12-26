<template>
<div id="net">
  <div id="download"></div>
  <div id="upload"></div>
</div>
</template>

<script>
export default {
  name: 'net',
  mounted () {
    let echarts = require('echarts')
    let myChart1 = echarts.init(document.getElementById('download'), 'light')
    let myChart2 = echarts.init(document.getElementById('upload'), 'light')
    myChart1.showLoading()
    myChart2.showLoading()
    const option1 = {
      tooltip: {
        formatter: '{a} <br/>{b} : {c}%'
      },
      series: [
        {
          name: '网络io',
          type: 'gauge',
          detail: {formatter: '{value}Mbps'},
          data: [{value: 50, name: '下载速度'}]
        }
      ]
    }
    const option2 = {
      tooltip: {
        formatter: '{a} <br/>{b} : {c}%'
      },
      series: [
        {
          name: '网络io',
          type: 'gauge',
          detail: {formatter: '{value}Mbps'},
          data: [{value: 50, name: '上传速度'}]
        }
      ]
    }

    setInterval(function () {
      option1.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0
      option2.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0
      myChart1.hideLoading()
      myChart2.hideLoading()
      myChart1.setOption(option1, true)
      myChart2.setOption(option2, true)
    }, 2000)
  }
}
</script>

<style scoped>
  #net{
    height: 600px;
    width: 100%;
    display: flex;
  }
  #download{
    height: 80%;
    width: 50%;
  }
  #upload{
    flex-grow: 1;
    height: 80%;
    width: 50%;
  }
</style>
