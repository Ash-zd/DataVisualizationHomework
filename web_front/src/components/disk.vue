<template>
  <div id="disk"></div>
</template>

<script>
export default {
  name: 'disk',
  mounted () {
    let echarts = require('echarts')
    let myChart = echarts.init(document.getElementById('disk'), 'light')
    myChart.setOption({
      title: {
        text: '本机硬盘容量统计',
        x: 'center'
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        x: 'left',
        data: ['C盘', 'D盘', 'E盘', 'F盘']
      },
      series: [
        {
          name: '容量大小',
          type: 'pie',
          selectedMode: 'single',
          radius: [0, '30%'],

          label: {
            normal: {
              position: 'inner'
            }
          },
          labelLine: {
            normal: {
              show: false
            }
          },
          data: [
            {value: 220, name: '硬盘1', selected: true},
            {value: 960, name: '硬盘2'}

          ]
        },
        {
          name: '容量大小',
          type: 'pie',
          radius: ['40%', '55%'],
          label: {
            normal: {
              formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
              backgroundColor: '#eee',
              borderColor: '#aaa',
              borderWidth: 1,
              borderRadius: 4,
              rich: {
                a: {
                  color: '#999',
                  lineHeight: 22,
                  align: 'center'
                },
                hr: {
                  borderColor: '#aaa',
                  width: '100%',
                  borderWidth: 0.5,
                  height: 0
                },
                b: {
                  fontSize: 16,
                  lineHeight: 33
                },
                per: {
                  color: '#eee',
                  backgroundColor: '#334455',
                  padding: [2, 4],
                  borderRadius: 2
                }
              }
            }
          },
          data: [
            {value: 237, name: 'C盘'},
            {value: 299, name: 'D盘'},
            {value: 299, name: 'E盘'},
            {value: 201, name: 'F盘'}
          ]
        }
      ]
    })
  }
}
</script>

<style scoped>
#disk {
  height: 600px;
  width: 800px;
}
</style>
