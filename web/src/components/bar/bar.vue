<style lang="stylus" scoped>
  .bar
    height 1000px
    background-size 100% 100%
    .main
      width 100%
      height calc(80% - 100px)
      margin-top -15px
</style>

<template>
  <div class="bar">
    <v-header :name="name" :legendArr="legendArr" :myChart="myChart"></v-header>
    <div class="main"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import axios from 'axios'
  import header from 'src/components/header/header'

  export default {
    data () {
      return {
        legendArr: [],
        color: this.$store.state.color,
        styleArr: [],
        myChart: {},
        name: '访问量统计'
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
    name: "bar",
    components: {
      'v-header': header
    },
    mounted() {
      axios.get("http://localhost:8000/api/log/analyze/").then((res) => {
        console.log(res.data)
        this.myChart = echarts.init(document.querySelector('.bar .main'), 'light')
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
          /* dataset: {
            source: [
              ['amount', 'product'],
              [58212, 'Matcha Latte'],
              [78254, 'Milk Tea'],
              [41032, 'Cheese Cocoa'],
              [12755, 'Cheese Brownie'],
              [20145, 'Matcha Cocoa'],
              [79146, 'Tea'],
              [91852, 'Orange Juice'],
              [101852, 'Lemon Juice'],
              [20112, 'Walnut Brownie']
            ]
          }, */
          dataset: {
            source: res.data['resp']
          },
          grid: {containLabel: true},
          xAxis: {
            name: 'amount',
            axisLabel: {
              textStyle: {
                color: 'white',
                fontSize: 14
              }
            }
          },
          yAxis: {
            type: 'category',
            axisLabel: {
              textStyle: {
                color: 'white',
                fontSize: 14
              }
            }
          },
          visualMap: {
            orient: 'horizontal',
            left: 'center',
            min: 10,
            max: 100,
            text: ['High Score', 'Low Score'],
            // Map the score column to color
            dimension: 0,
            inRange: {
              color: ['#D7DA8B', '#E15457']
            }
          },
          series: [
            {
              name: 'ip访问量统计',
              type: 'bar',
              encode: {
                // Map the "amount" column to X axis.
                x: 'amount',
                // Map the "product" column to Y axis
                y: 'product'
              }
            }
          ]
        });
      });
      this.myinit();
    }
  }
</script>
