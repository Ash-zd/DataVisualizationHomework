<template>
  <div class="parallel">
    <v-header :name="name" :legendArr="legendArr" :myChart="myChart"></v-header>
    <v-filter :myChart="myChart" v-if="myChart._dom"></v-filter>
    <div class="main"></div>
  </div>
</template>

<script>
  import axios from 'axios'
  import echarts from 'echarts'
  import header from 'src/components/header/header'
  import filter from 'src/components/filter/filter'

  export default {
    created() {
      this._getCityData()
    },
    data() {
      return {
        legendArr: [],
        color: this.$store.state.color,
        myChart: {},
        geoCoordMap: {},
        name: 'parallel'
      }
    },
    methods: {
      _init(options) {
        this.myChart = echarts.init(document.querySelector('.parallel .main'), 'light');
        this.myChart.setOption(options);
        this.legendArr = options.series;
        this.legendArr.forEach((data) => {
          data.selected = true;
        });
        this.$root.charts.push(this.myChart);
        window.addEventListener('resize', function() {
          this.myChart.resize()
        }.bind(this))
      },
      _getCityData() {
        axios.get('static/data/parallel/geoCoordMap.json').then((res) => {
          this.geoCoordMap = res.data;
          this.$nextTick(() => {
            this._getMyChart()
          })
        })
      },
      _getMyChart() {
        axios.get('static/data/parallel/schema.json').then((res1) => {
          axios.get('static/data/parallel/rawData.json').then((res2) => {
            let schema = res1.data;
            let rawData = res2.data;
            console.log("schema: " + schema);
            console.log("rawData: " + rawData);
            function makeMapData(rawData) {
              var mapData = [];
              for (var i = 0; i < rawData.length; i++) {
                var geoCoord = geoCoordMap[rawData[i][0]];
                if (geoCoord) {
                  mapData.push({
                    name: rawData[i][0],
                    value: geoCoord.concat(rawData[i].slice(1))
                  });
                }
              }
              return mapData;
            }
            function makeParallelAxis(schema) {
              var parallelAxis = [];
              for (var i = 1; i < schema.length; i++) {
                parallelAxis.push({dim: i, name: schema[i]});
              }
              return parallelAxis;
            }
            let options = {
              backgroundColor: new echarts.graphic.RadialGradient(0.5, 0.5, 0.4, [{
                offset: 0,
                color: '#4b5769'
              }, {
                offset: 1,
                color: '#404a59'
              }]),
              title: {
                text: 'Prices and Earnings 2012',
                subtext: 'data from macrofocus',
                sublink: 'https://www.macrofocus.com/public/products/infoscope/datasets/pricesandearnings/',
                left: 'center',
                top: 5,
                itemGap: 0,
                textStyle: {
                  color: '#eee'
                },
                z: 200
              },
              tooltip: {
                trigger: 'item',
                formatter: function (params) {
                  var value = (params.value + '').split('.');
                  value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,') + '.' + value[1];
                  return params.seriesName + '<br/>' + params.name + ' : ' + value;
                }
              },
              toolbox: {
                show: true,
                left: 'right',
                iconStyle: {
                  normal: {
                    borderColor: '#ddd'
                  }
                },
                feature: {
                },
                z: 202
              },
              brush: {
                geoIndex: 0,
                brushLink: 'all',
                inBrush: {
                  opacity: 1,
                  symbolSize: 14
                },
                outOfBrush: {
                  color: '#000',
                  opacity: 0.2
                },
                z: 10
              },
              geo: {
                map: 'world',
                silent: true,
                label: {
                  emphasis: {
                    show: false,
                    areaColor: '#eee'
                  }
                },
                itemStyle: {
                  normal: {
                    borderWidth: 0.2,
                    borderColor: '#404a59'
                  }
                },
                left: '6%',
                top: 40,
                bottom: '54%',
                right: '14%',
                roam: true
                // itemStyle: {
                //     normal: {
                //         areaColor: '#323c48',
                //         borderColor: '#111'
                //     },
                //     emphasis: {
                //         areaColor: '#2a333d'
                //     }
                // }
              },
              parallelAxis: makeParallelAxis(schema),
              grid: [{
                show: true,
                left: 0,
                right: 0,
                top: '48%',
                bottom: 0,
                borderColor: 'transparent',
                backgroundColor: '#404a59',
                z: 99
              }, {
                show: true,
                left: 0,
                right: 0,
                top: 0,
                height: 28,
                borderColor: 'transparent',
                backgroundColor: '#404a59',
                z: 199
              }],
              parallel: {
                top: '50%',
                left: 60,
                right: 20,
                bottom: 100,
                axisExpandable: true,
                axisExpandCenter: 15,
                axisExpandCount: 10,
                axisExpandWidth: 60,
                axisExpandTriggerOn: 'mousemove',

                z: 100,
                parallelAxisDefault: {
                  type: 'value',
                  nameLocation: 'start',
                  nameRotate: 25,
                  // nameLocation: 'end',
                  nameTextStyle: {
                    fontSize: 12
                  },
                  nameTruncate: {
                    maxWidth: 170
                  },
                  nameGap: 20,
                  splitNumber: 3,
                  tooltip: {
                    show: true
                  },
                  axisLine: {
                    // show: false,
                    lineStyle: {
                      width: 1,
                      color: 'rgba(255,255,255,0.3)'
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  splitLine: {
                    show: false
                  },
                  z: 100
                }
              },
              series: [
                {
                  name: 'Prices and Earnings 2012',
                  type: 'scatter',
                  coordinateSystem: 'geo',
                  symbolSize: 8,
                  data: makeMapData(rawData),
                  activeOpacity: 1,
                  label: {
                    normal: {
                      formatter: '{b}',
                      position: 'right',
                      show: false
                    },
                    emphasis: {
                      show: true
                    }
                  },
                  // symbolSize: function (data) {
                  //     return Math.max(5, data[2] / 5);
                  // },
                  itemStyle: {
                    normal: {
                      borderColor: '#fff',
                      color: '#577ceb'
                    }
                  }
                },
                {
                  name: 'parallel',
                  type: 'parallel',
                  smooth: true,
                  lineStyle: {
                    normal: {
                      color: '#577ceb',
                      width: 0.5,
                      opacity: 0.6
                    }
                  },
                  z: 100,
                  blendMode: 'lighter',
                  data: rawData
                }
              ]
            };
            this._init(options)
          })
        })
      }
    },
    components: {
      'v-header': header,
      'v-filter': filter
    },
    name: "parallel"
  }
</script>

<style lang="stylus" scoped>
  .parallel
    background-size 100% 100%
    .main
      height calc(100% - 120px)
      width 100%
      transition all 0.5s linear
</style>
