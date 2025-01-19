// Course Enaring Chart
const courseEarningOptions = {
  chart: {
    type: "area",
    height: 120,
    sparkline: {
      enabled: true,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  series: [
    {
      name: "",
      data: [
        {
          x: "01-01-2023 GMT",
          y: 5,
        },
        {
          x: "01-05-2023 GMT",
          y: 30,
        },
        {
          x: "01-10-2023 GMT",
          y: 10,
        },
        {
          x: "01-15-2023 GMT",
          y: 25,
        },
        {
          x: "01-20-2023 GMT",
          y: 11,
        },
        {
          x: "01-25-2023 GMT",
          y: 30,
        },
        {
          x: "01-30-2023 GMT",
          y: 15,
        },
        {
          x: "02-05-2023 GMT",
          y: 28,
        },
        {
          x: "02-10-2023 GMT",
          y: 10,
        },
      ],
    },
  ],
  xaxis: {
    type: "datetime",
    min: new Date("01 Jan 2023").getTime(),
  },
  colors: ["#795DED"],
  stroke: {
    width: 1.2,
    curve: "smooth",
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.5,
      opacityTo: 0.2,
      stops: [0, 60],
    },
  },
  tooltip: {
    marker: {
      show: false,
    },
    y: {
      formatter: (val) => {
        return val + "k";
      },
    },
  },
};
const courseEaringChart = new ApexCharts(
  document.querySelector("#courseEarning"),
  courseEarningOptions
);
courseEaringChart.render();

// New Enrollment Chart
const newEnrollOptions = {
  chart: {
    type: "area",
    height: 120,
    sparkline: {
      enabled: true,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  series: [
    {
      name: "",
      data: [
        {
          x: "01-01-2023 GMT",
          y: 5,
        },
        {
          x: "01-05-2023 GMT",
          y: 30,
        },
        {
          x: "01-10-2023 GMT",
          y: 10,
        },
        {
          x: "01-15-2023 GMT",
          y: 25,
        },
        {
          x: "01-20-2023 GMT",
          y: 11,
        },
        {
          x: "01-25-2023 GMT",
          y: 30,
        },
        {
          x: "01-30-2023 GMT",
          y: 15,
        },
        {
          x: "02-05-2023 GMT",
          y: 28,
        },
        {
          x: "02-10-2023 GMT",
          y: 10,
        },
      ],
    },
  ],
  xaxis: {
    type: "datetime",
    min: new Date("01 Jan 2023").getTime(),
  },
  colors: ["#795DED"],
  stroke: {
    width: 1.2,
    curve: "smooth",
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.5,
      opacityTo: 0.2,
      stops: [0, 60],
    },
  },
  tooltip: {
    marker: {
      show: false,
    },
    y: {
      formatter: (val) => {
        return val + "k";
      },
    },
  },
};
const newEnrollChart = new ApexCharts(
  document.querySelector("#newEnroll"),
  newEnrollOptions
);
newEnrollChart.render();

// Course Impression Chart
const courseImpressionOptions = {
  chart: {
    type: "area",
    height: 120,
    sparkline: {
      enabled: true,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  series: [
    {
      name: "",
      data: [
        {
          x: "01-01-2023 GMT",
          y: 5,
        },
        {
          x: "01-05-2023 GMT",
          y: 30,
        },
        {
          x: "01-10-2023 GMT",
          y: 10,
        },
        {
          x: "01-15-2023 GMT",
          y: 25,
        },
        {
          x: "01-20-2023 GMT",
          y: 11,
        },
        {
          x: "01-25-2023 GMT",
          y: 30,
        },
        {
          x: "01-30-2023 GMT",
          y: 15,
        },
        {
          x: "02-05-2023 GMT",
          y: 28,
        },
        {
          x: "02-10-2023 GMT",
          y: 10,
        },
      ],
    },
  ],
  xaxis: {
    type: "datetime",
    min: new Date("01 Jan 2023").getTime(),
  },
  colors: ["#76D466"],
  stroke: {
    width: 1.2,
    curve: "smooth",
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.5,
      opacityTo: 0.2,
      stops: [0, 60],
    },
  },
  tooltip: {
    marker: {
      show: false,
    },
    y: {
      formatter: (val) => {
        return val + "k";
      },
    },
  },
};
const courseImpressionChart = new ApexCharts(
  document.querySelector("#courseImpression"),
  courseImpressionOptions
);
courseImpressionChart.render();
