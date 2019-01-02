<style lang="stylus" scoped>
  .tree
    height 1000px
    background-size 100% 100%
    .main
      width 100%
      height calc(85% - 100px)
      margin-top -15px
</style>

<template>
  <div class="tree">
    <v-header :name="name" :legendArr="legendArr" :myChart="myChart"></v-header>
    <v-filter :myChart="myChart" v-if="myChart._dom"></v-filter>
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
    let myChart = echarts.init(document.querySelector('.tree .main'), 'light')
    axios.get('static/data/tree/tree1.json').then((res) => {
      var data1;
      var data2;
      data1 = res.data;
      axios.get('static/data/tree/tree2.json').then((res) => {
        data2 = res.data;
        console.log(data1)
        console.log(data2)
        myChart.setOption({
          tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
          },
          legend: {
            top: '2%',
            left: '3%',
            orient: 'vertical',
            data: [{
              name: 'tree1',
              icon: 'rectangle'
            }, {
              name: 'tree2',
              icon: 'rectangle'
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
              name: 'tree1',
              data: [data1],
              top: '5%',
              left: '15%',
              bottom: '2%',
              right: '60%',
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

            },
            {
              type: 'tree',
              name: 'tree2',
              data: [data2],
              top: '20%',
              left: '60%',
              bottom: '22%',
              right: '18%',
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
      })
    })
  }
}
</script>
