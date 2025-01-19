// Sells Overview Chart
const sellOverviewOption = {
  chart: {
    type: "area",
    height: 340,
    offsetX: -10,
    offsetY: 20,
    toolbar: {
      show: false,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  xaxis: {
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  yaxis: {
    min: 0,
    max: 90,
    tickAmount: 5,
    labels: {
      formatter: (val) => val + "k",
    },
  },
  series: [
    {
      name: "Revenue",
      data: [34, 70, 30, 60, 40, 80, 34, 70, 30, 60, 40, 80],
    },
    {
      name: "Orders",
      data: [0, 60, 21, 50, 30, 70, 5, 60, 21, 50, 30, 70],
    },
  ],
  grid: {
    borderColor: "#EEE",
    strokeDashArray: 5,
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: "smooth",
    colors: ["#795DED", "#76D466"],
    width: 2,
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.4,
      opacityTo: 0.15,
      stops: [0, 60],
    },
  },
  legend: {
    position: "top",
    horizontalAlign: "left",
    offsetX: -30,
    offsetY: 0,
    markers: {
      width: 7,
      height: 7,
      radius: 99,
      fillColors: ["#795DED", "#76D466"],
      offsetX: -3,
      offsetY: -1,
    },
    itemMargin: {
      horizontal: 20,
    },
  },
  tooltip: {
    followCursor: true,
    y: {
      formatter: (val) => {
        return val + "h";
      },
    },
  },
};

const sellOverviewChart = new ApexCharts(
  document.querySelector("#sells-overview-chart"),
  sellOverviewOption
);
sellOverviewChart.render();

// Countries By Sales
const markers = [
  {
    name: "North America",
    coords: [54.52, 105.25],
  },
  {
    name: "China",
    coords: [35.86, 104.19],
  },
  {
    name: "Greenland",
    coords: [71.7, 42.6],
  },
  {
    name: "Germany",
    coords: [51.16, 10.45],
  },
  {
    name: "Australia",
    coords: [25.27, 133.77],
  },
];
new jsVectorMap({
  selector: "#sell-by-country-map",
  map: "world_merc",
  markersSelectable: true,
  // zoomOnScroll: false,
  zoomButtons: false,
  labels: {
    markers: {
      render: function (marker) {
        return marker.name;
      },
    },
  },
  markers: markers,
  markerStyle: {
    initial: {
      image: "assets/images/icons/location.svg",
    },
  },
  regionStyle: {
    initial: {
      fill: "#F4ECFF",
      stroke: "#B39EF9",
      strokeWidth: 1,
      fillOpacity: 1,
    },
  },
  onMarkerSelected(index, isSelected, selectedMarkers) {
    console.log(index, isSelected, selectedMarkers);
  },
});
